import turtle
import pandas
import random

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

# Select a state, at random, to be guessed
random_location = random.choice(states)
print(random_location)

# Save data frame data for random_location to a variable
row_data = data[data.state == random_location]
print(row_data)

# Extract coordinates from row_data for turtle as ints
x = row_data.x.item()
y = row_data.y.item()

t = turtle.Turtle()
t.shape("arrow")
t.setheading(270)
# t.color("red")
t.penup()
t.goto(x, y)
t.write("What state is this?", align='left', font=('Arial', 12, 'normal'))
answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter this state's name:").title()

if answer_state == row_data.state.item():
    print("Correct!")

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
#
#     if answer_state == "Exit":
#         missing_states = []
#         for state in states:
#             missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#
#     if answer_state in states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)