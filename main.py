import turtle
import pandas
from functools import partial


def exit_quiz():
    screen.bye()


def quiz(bg, database):
    writer.clear()
    screen.bgpic("backgrounds/" + bg)
    data = pandas.read_csv("data/" + database)
    guessed_answers = []
    answers = data["answer"].to_list()
    number_of_answers = len(answers)
    game_is_on = True
    while game_is_on:
        answer = screen.textinput(title=f"{len(guessed_answers)}/{number_of_answers} Correct",
                                  prompt="Type your answer").capitalize()

        if answer in answers and answer not in guessed_answers:
            writer.color("black")
            db_line = data[data.answer == answer].to_dict('list')
            writer.goto(db_line['x_cord'][0], db_line['y_cord'][0])
            writer.write(db_line['answer'][0], font=('Arial', 16, 'normal'))
            guessed_answers.append(answer)

        if len(guessed_answers) == number_of_answers:
            break
        if answer == "Stop":
            for answer in answers:
                if answer not in guessed_answers:
                    db_line = data[data.answer == answer].to_dict('list')
                    writer.goto(db_line['x_cord'][0], db_line['y_cord'][0])
                    writer.color("red")
                    writer.write(db_line['answer'][0], font=('Arial', 16, 'normal'))

        if answer == "Exit":
            screen.bgpic("backgrounds/bg.png")
            guessed_answers.clear()
            writer.clear()
            screen.listen()
            break


writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

screen = turtle.Screen()
screen.setup(940, 788)
screen.title("JetPunk Clone | Jakub Olszak")
screen.bgpic("backgrounds/bg.png")

screen.onkeypress(partial(quiz, "cities_bg.png", "cities_db.csv"), "1")
screen.onkeypress(partial(quiz, "coldest_bg.png", "coldest_db.csv"), "2")
screen.onkeypress(partial(quiz, "oil_bg.png", "oil_db.csv"), "3")
screen.onkeypress(partial(quiz, "pork_bg.png", "pork_db.csv"), "4")
screen.onkeypress(partial(quiz, "development_bg.png", "development_db.csv"), "5")

screen.onkeypress(writer.clear, "c")
screen.onkeypress(exit_quiz, '0')

screen.listen()
screen.mainloop()
