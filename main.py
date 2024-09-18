import turtle
import pandas
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read in data on states from file
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# Declare some variables
guessed_states = []
incorrect_guesses = 0
player = input("Enter your name - for the record books: ").title()

# Get current high score
high_score = pandas.read_csv("high_score.csv")
high_score_dict = {row[0]:row[1] for (index, row) in high_score.iterrows()}
print(high_score_dict)

for key in high_score_dict:
    # print(f"All time leader: {key}.  Score: {high_score_dict[key]} wrong.")
    leader = key
    score = high_score_dict[key]
    # print(f"{key} only got {high_score_dict[key]} wrong.")

# Create a turtle that presents the current high score
    hi = turtle.Turtle()
    hi.hideturtle()
    hi.setheading(270)
    hi.shapesize(0.5, 0.5)
    # t.color("red")
    hi.penup()
    hi.goto(-200, 250)
    hi.write(f"All time leader: {key}  Score: {high_score_dict[key]} (wrong)", align='left', font=('Arial', 16, 'normal'))







# Game loop
while len(guessed_states) < 50:

    # DEBUG:  print(f"Available choices: {states}")

    # Pretty-print available choices to console
    print("\n" * 100)
    print("Available choices:")
    for _ in range(0, len(states)):
        print(f"{states[_]}, ", end='')
        if _/10 == 1: print("")
        elif _/ 10 == 2: print("")
        elif _ / 10 == 3: print("")
        elif _ / 10 == 4: print("")

    # Select a state, at random, to be guessed
    random_location = random.choice(states)

    # Save data frame data for random_location to a variable
    row_data = data[data.state == random_location]
    # DEBUG:  print(row_data)

    # Extract coordinates from row_data for turtle as ints
    x = row_data.x.item()
    y = row_data.y.item()

    # Create a turtle that roams the US
    t = turtle.Turtle()
    t.shape("arrow")
    t.setheading(270)
    t.shapesize(0.5, 0.5)
    # t.color("red")
    t.penup()
    t.goto(x, y)
    t.write("What state is this?", align='left', font=('Arial', 8, 'normal'))

    # https://stackoverflow.com/questions/77208847/how-can-i-customize-the-placement-or-position-of-the-text-input-window-in-the-tu <- Tried, seems to be missing a click event
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter this state's name:").title()

    # Evaluate if the guess is correct
    if answer_state == row_data.state.item():
        guessed_states.append(answer_state)
        t.clear()
        t.color("green")
        t.write(f"{answer_state}", align='left', font=('Arial', 8, 'normal'))
        states.remove(answer_state)
    else:
        t.clear()
        t.color("red")
        incorrect_guesses += 1
        t.write(f"Not {answer_state}, {row_data.state.item()}", align='left', font=('Arial', 8, 'normal'))
        time.sleep(3)
        t.clear()
        print(f"Sorry, that's not correct.  The correct answer is {row_data.state.item()}")
    t.color("black")

print(f"Here are the states you got correct: {guessed_states}")
print(f"You made {incorrect_guesses} incorrect guesses.")
print(f"End_Leader: {leader}")
print(f"End_score: {score}")








screen.exitonclick()