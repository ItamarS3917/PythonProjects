import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_list = []
states_to_learn = []

while len(states_list) < 50:
    answer_state = screen.textinput(title=f"{len(states_list)}/50", prompt="What's another state name").title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        states_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

if len(states_list) < 50:
    for state in all_states:
        if state not in states_list:
            states_to_learn.append(state)

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")
