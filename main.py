import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data["state"].tolist()
missing_states = []
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What is another state name?").title()
    print(answer_state)

    if answer_state == "Exit":
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)

        df = pd.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data["state"] == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)



