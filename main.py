from turtle import Turtle, Screen
import pandas


screen = Screen()



image = r'blank_states_img.gif'




write_turtle = Turtle()
tim = Turtle()

screen.addshape(image)

tim.shape(image)





data = pandas.read_csv(r"50_states.csv")


list_of_states = data["state"].to_list()





score = 0



guessed_states = []

game_is_on = True
while game_is_on:
    user_answer = screen.textinput(title=f"{score}/50 states correct",
                                   prompt=" what's another state name!: ").title()
    if user_answer == "Exit":
        should_revise_state = [item for item in list_of_states if item not in guessed_states]
        second_data = pandas.DataFrame(should_revise_state)
        second_data.to_csv(r"states_to_learn.csv")
        break

    if user_answer in list_of_states:
        guessed_states.append(user_answer)
        write_turtle.penup()
        write_turtle.hideturtle()
        state = data[data["state"] == user_answer]
        x_cor = int(state.x)
        y_cor = int(state.y)
        write_turtle.goto(x_cor, y_cor)
        write_turtle.write(user_answer, align='center', font=('Arial', 7, 'normal'))
        score += 1









