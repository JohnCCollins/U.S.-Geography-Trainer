import turtle
import pandas

screen = turtle.Screen()
screen.title("Unites States Geography Trainer")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_map = pandas.read_csv("50_states.csv")
states = states_map.state.to_list()
states_found = []
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
first_state = True
while len(states_found) < 50:
    if first_state:
        answer_state = screen.textinput(f"{len(states_found)}/50 States Correct",
                                        "Name a state...").title()
    else:
        answer_state = screen.textinput(f"{len(states_found)}/50 States Correct",
                                    "Name another state...").title()
    first_state = False
    current_state = answer_state
    while answer_state in states_found:
        answer_state = screen.textinput(f"{len(states_found)}/50 States Correct",
                                        f"You already found {current_state}; try another").title()
    if answer_state == "Exit":
        states_remaining = [state for state in states if state not in states_found]
        states_to_learn = pandas.DataFrame(states_remaining)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        states_found.append(answer_state)
        correct_state = states_map[states_map.state == answer_state]
        pen.goto(int(correct_state.x), int(correct_state.y))
        pen.write(answer_state, align="center")
