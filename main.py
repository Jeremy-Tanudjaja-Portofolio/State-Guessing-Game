import turtle
from read_states_csv import Read_States

game_is_on = True
image_path = "blank_states_img.gif"
states_data = "50_states.csv"

screen = turtle.Screen()
screen.title("US States Game")


screen.addshape(image_path)
turtle.shape(image_path)

checker = Read_States(states_data)

while game_is_on:
    answer_state = screen.textinput(title="Question", prompt="What States?")
    if (checker.check_answer(answer= answer_state)) == False or (checker.check_win() == True):
        game_is_on = False


screen.exitonclick()
