import turtle
import pandas

states_data = []
correct_ans = 0

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "Day_25/us-states-game-start/states_img.gif"
screen.addshape(image)

turtle.shape(image)


def name_tra(name_state, x_cor, y_cor):
    i = turtle.Turtle()
    i.penup()
    i.goto(x_cor, y_cor)
    i.hideturtle()
    i.write(str(name_state))


while len(states_data) < 50:
    ans_state = screen.textinput(
        title=f"{correct_ans}/50 State Correct", prompt="Whats another state name?").title()
    state = pandas.read_csv("Day_25\\us-states-game-start\\50_states.csv")
    new_state = state[state["state"] == ans_state]
    if ans_state == "Exit":
        for i in states_data:
            state_now = state[state["state"] != i]
        pandas.DataFrame(state_now["state"]).to_csv(
            "Day_25\\us-states-game-start\\states_to-learn.csv")
        break
    if not new_state.empty:
        correct_ans += 1
        states_data.append(ans_state)
        name_tra(ans_state, new_state['x'].item(), new_state['y'].item())
    else:
        pass


turtle.mainloop()
