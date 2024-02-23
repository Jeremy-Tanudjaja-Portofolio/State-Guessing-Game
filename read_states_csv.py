import pandas
import turtle


class Read_States():

    def __init__(self, filepath):
        self.right_state = {
            "States": [],
            "X": [],
            "Y": []
        }
        self.file_data = pandas.read_csv(filepath)
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()

    def check_answer(self, answer):
        if answer == None:
            self.write_states_to_learn()
            return False
        states = self.file_data["state"].to_list()
        for state in states:
            if state.lower() == answer.lower():
                data = self.file_data[self.file_data["state"] == state]
                coor_x = int(data["x"])
                coor_y = int(data["y"])
                self.right_state["States"].append(state)
                self.right_state["X"].append(str(coor_x))
                self.right_state["Y"].append(str(coor_y))
                self.write_state(coor_x, coor_y, state)
                return True
        print("No States Named that")

    def write_state(self, x, y, state_name):
        self.writer.goto(x, y)
        self.writer.pendown()
        self.writer.write(state_name, font=("Verdana", 8, "normal"))
        self.writer.penup()

    def write_states_to_learn(self):
        states_dataframe = pandas.DataFrame(self.right_state)
        states_dataframe.to_csv("right_states.csv")

    def check_win(self):
        states = self.file_data["state"].to_list()
        if len(self.right_state["States"]) == len(states):
            return True
