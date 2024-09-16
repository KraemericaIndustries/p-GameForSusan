import turtle
import pandas
import random
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    # print(f"Available choices: {states}")

    # Pretty-print available choices to console
    print("\n" * 100)
    print("Available choices:")
    for _ in range(0, len(states) - 1):
        print(f"{states[_]}, ", end='')
        if _/10 == 1: print("")
        elif _/ 10 == 2: print("")
        elif _ / 10 == 3: print("")
        elif _ / 10 == 4: print("")

    # Select a state, at random, to be guessed
    random_location = random.choice(states)
    # print(random_location)

    # Save data frame data for random_location to a variable
    row_data = data[data.state == random_location]
    # print(row_data)

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

    # https://stackoverflow.com/questions/77208847/how-can-i-customize-the-placement-or-position-of-the-text-input-window-in-the-tu
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter this state's name:").title()

    # Evaluate if the guess is correct
    if answer_state == row_data.state.item():
        guessed_states.append(answer_state)
        t.clear()
        t.color("green")
        t.write(f"{answer_state}", align='left', font=('Arial', 8, 'normal'))
        # print("Correct!")
        states.remove(answer_state)
    else:
        t.clear()
        t.color("red")
        t.write(f"Not {answer_state}, {row_data.state.item()}", align='left', font=('Arial', 8, 'normal'))
        time.sleep(3)
        t.clear()


        # states.remove(row_data.state.item())
        print(f"Sorry, that's not correct.  The correct answer is {row_data.state.item()}")
        # break
    t.color("black")
print(f"Here are the states you got correct: {guessed_states}")

screen.exitonclick()