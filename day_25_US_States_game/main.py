import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another states's name")
    final_answer = answer_state.title()
    if final_answer == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        #alternative code version---------------------------
        # states_to_learn = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        states_to_learn_table=pandas.DataFrame(states_to_learn)
        states_to_learn_table.to_csv("states_to_learn.csv")
        break
    if final_answer in all_states:
        guessed_states.append(final_answer)
        zolw = turtle.Turtle()
        zolw.hideturtle()
        zolw.penup()
        state_coordinates = data[data["state"] == final_answer]
        zolw.goto(int(state_coordinates.x.iloc[0]), int(state_coordinates.y.iloc[0]))
        zolw.write(answer_state)







