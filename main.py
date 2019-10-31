import sys
import threading
import time

from PyQt5 import QtWidgets, uic

import exercise_generator

qtcreator_file = "./ui/mainwindow.ui"  # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    aux_result = 0  # class variable we going to use in order to store exercise result

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start_game)
        self.start_button.clicked.connect(self.update_progress_bar)  # must be in a different thread
        self.check_button.clicked.connect(self.review_answer)

    def start_game(self):
        # we need to disable the difficulty_level selector and the start button
        self.difficulty_level.setEnabled(False)
        self.start_button.setEnabled(False)

        # the difficulty level set the kind of exercises to be solved:
        # 0: 1 digit exercises: addition, subtraction, multiplication
        # 1: 1 and 2 digit exercises: addition, subtraction, multiplication
        # 2: 2 digit exercises: addition, subtraction, multiplication, division
        # 3: 2 and 3 digit exercises: addition, subtraction, multiplication, division
        # 4: 3 digit exercises: addition, subtraction, multiplication, division
        # 5: 3 and 4 digit exercises: addition, subtraction, multiplication, division

        exercise_to_do = exercise_generator.random_exercise(self.difficulty_level.value())
        operando_1 = exercise_to_do[0]
        operando_2 = exercise_to_do[1]
        operador = exercise_to_do[2]

        self.math_problem.setText(str(operando_1) + '<br>' + operador + '<br>' + str(operando_2))

        if operador == '+':
            self.aux_result = operando_1 + operando_2
        if operador == '-':
            self.aux_result = operando_1 - operando_2
        if operador == '*':
            self.aux_result = operando_1 * operando_2
        if operador == '/':
            self.aux_result = operando_1 / operando_2

    def review_answer(self):
        if self.time_left.value() > 0:
            if int(self.answer_provided.text()) != self.aux_result:
                self.user_feedback.setText('Wrong, the correct answer is: ' + str(self.aux_result))
                self.score.setText(str(int(self.score.text()) - 1))
            else:
                self.user_feedback.setText('Right, the correct answer is: ' + str(self.aux_result))
                self.score.setText(str(int(self.score.text()) + 1))
            self.start_game()  # after each answer a new question pops up

    def update_time_left(self, time_to_wait):
        while self.time_left.value() > 0:
            time.sleep(time_to_wait)
            self.time_left.setValue(self.time_left.value() - 1)
        # time is over
        self.user_feedback.setText('Thanks for playing!')

    def update_progress_bar(self):
        x = threading.Thread(target=self.update_time_left, args=(0.5,))
        x.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
