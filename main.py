import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US. States quiz game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
df = pd.DataFrame(data)

list_of_states = df["state"].to_list()
# print(list_of_states)
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50", "What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in guessed_states]
        # for state in list_of_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # print(missing_states)
        # new_data = pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

print(missing_states)
