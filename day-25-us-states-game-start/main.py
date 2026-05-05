import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("United States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")

all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput("Guess the State", f"Number of States guessed: {len(guessed_states)}/50\nGuess a State name:").title()

    if answer_state == "Exit" or answer_state is None:
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state in guessed_states:
            screen.textinput("Already Guessed", f"You already guessed {answer_state}.")
        else:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)






"""
# If you want the coordinates where your mouse clicks:
# But we already have the coordinates of the states of map in the file

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

"""

