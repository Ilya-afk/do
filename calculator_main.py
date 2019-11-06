import sys
import math
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui_calculator import Ui_MainWindow
from ui_history import Ui_Form


class History(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.cur.execute("""DELETE from history""").fetchall()
        self.con.commit()
        self.show_database()

    def show_database(self):
        self.con = sqlite3.connect("history.db")
        self.cur = self.con.cursor()
        result = self.cur.execute(f"""SELECT expression, answer FROM history""").fetchall()
        self.tableWidget.setRowCount(len(result))
        if len(result) == 0:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setItem(0, 0, QTableWidgetItem('Ничего не найдено'))
        else:
            self.tableWidget.setColumnCount(2)
            for j in range(len(result)):
                for i in range(2):
                    self.tableWidget.setItem(j, i, QTableWidgetItem(str(result[j][i])))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.a = 0
        self.b = 0
        self.operation = ''
        self.open_bracket_number = 0
        self.close_bracket_number = 0
        self.history = History()

        self.pushButton_0.clicked.connect(self.run_0)
        self.pushButton_1.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.run_7)
        self.pushButton_8.clicked.connect(self.run_8)
        self.pushButton_9.clicked.connect(self.run_9)
        self.pushButton_pt.clicked.connect(self.run_pt)
        self.pushButton_plus.clicked.connect(self.run_plus)
        self.pushButton_minus.clicked.connect(self.run_minus)
        self.pushButton_multi.clicked.connect(self.run_multi)
        self.pushButton_split.clicked.connect(self.run_split)
        self.pushButton_stepen.clicked.connect(self.run_stepen)
        self.pushButton_koren.clicked.connect(self.run_koren)
        self.pushButton_factorial.clicked.connect(self.run_factorial)
        self.pushButton_eq.clicked.connect(self.run_eq)
        self.pushButton_back.clicked.connect(self.run_back)
        self.pushButton_open.clicked.connect(self.run_open)
        self.pushButton_close.clicked.connect(self.run_close)
        self.pushButton_clean.clicked.connect(self.run_clean)
        self.pushButton_history.clicked.connect(self.run_history)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.run_0()
        elif event.key() == Qt.Key_1:
            self.run_1()
        elif event.key() == Qt.Key_2:
            self.run_2()
        elif event.key() == Qt.Key_3:
            self.run_3()
        elif event.key() == Qt.Key_4:
            self.run_4()
        elif event.key() == Qt.Key_5:
            self.run_5()
        elif event.key() == Qt.Key_6:
            self.run_6()
        elif event.key() == Qt.Key_7:
            self.run_7()
        elif event.key() == Qt.Key_8:
            self.run_8()
        elif event.key() == Qt.Key_9:
            self.run_9()
        elif event.key() == Qt.Key_Plus:
            self.run_plus()
        elif event.key() == Qt.Key_Backspace:
            self.run_back()
        elif event.key() == Qt.Key_Equal:
            self.run_eq()
        elif event.key() == Qt.Key_Minus:
            self.run_minus()
        elif event.key() == Qt.Key_Slash:
            self.run_split()
        elif event.key() == Qt.Key_Asterisk:
            self.run_multi()
        elif event.key() == Qt.Key_BracketLeft:
            self.run_open()
        elif event.key() == Qt.Key_BracketRight:
            self.run_close()
        elif event.key() == Qt.Key_Comma:
            self.run_pt()
        elif event.key() == Qt.Key_ParenLeft:
            self.run_open()
        elif event.key() == Qt.Key_ParenRight:
            self.run_close()

#
# Добавление цифр в label
    def run_0(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_0.text())

    def run_1(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_1.text())

    def run_2(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_2.text())

    def run_3(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_3.text())

    def run_4(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_4.text())

    def run_5(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_5.text())

    def run_6(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_6.text())

    def run_7(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_7.text())

    def run_8(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_8.text())

    def run_9(self):
        self.main_label.setText(self.main_label.text() + self.pushButton_9.text())

    def run_pt(self):
        if self.main_label.text() != '':
            if self.main_label.text()[-1] != '.':
                self.main_label.setText(self.main_label.text() + self.pushButton_pt.text())

#
# Добавление операций в label
    def add_operation_in_label(self, operation):
        if self.main_label.text() != '':
            if self.main_label.text()[-1] not in ['+', '-', '*', '/', '^']:
                self.main_label.setText(self.main_label.text() + operation)
                self.operation = operation

    def run_plus(self):
        self.add_operation_in_label('+')

    def run_minus(self):
        self.add_operation_in_label('-')

    def run_multi(self):
        self.add_operation_in_label('*')

    def run_split(self):
        self.add_operation_in_label('/')

    def run_stepen(self):
        self.add_operation_in_label('^')

    def run_open(self):
        self.main_label.setText(self.main_label.text() + '(')
        self.operation = '('
        self.open_bracket_number += 1

    def run_close(self):
        if self.open_bracket_number - self.close_bracket_number > 0:
            self.main_label.setText(self.main_label.text() + ')')
            self.operation = ')'
            self.close_bracket_number += 1

# всплывающее окно с ошибкой
    def show_message(self, name_error):
        self.run_clean()
        message = QMessageBox(self)
        message.setText(name_error)
        message.exec_()

# Корень и факториал удобнее считать сразу, для этого мы запоминали последнюю операцию.
    def run_koren(self):
        try:
            if self.main_label.text() != '':
                if self.operation == '':
                    total = float(self.main_label.text())
                    all_before = ''
                else:
                    for i in range(-1, -len(self.main_label.text()), -1):
                        if self.operation == self.main_label.text()[i]:
                            ans = i
                            break
                    total = float(self.main_label.text()[ans + 1:])
                    all_before = self.main_label.text()[:ans + 1]
                self.main_label.setText(all_before + str(total**0.5))
                self.operation = ''
        except Exception as e:
            a = str(e)
            self.show_message(a)

    def run_factorial(self):
        try:
            if self.main_label.text() != '':
                if self.operation == '':
                    total = float(self.main_label.text())
                    all_before = ''
                else:
                    for i in range(-1, -len(self.main_label.text()), -1):
                        if self.operation == self.main_label.text()[i]:
                            ans = i
                            break
                    total = float(self.main_label.text()[ans + 1:])
                    all_before = self.main_label.text()[:ans + 1]
                self.main_label.setText(all_before + str(math.factorial(total)))
                self.operation = ''
        except Exception as e:
            a = str(e)
            self.show_message(a)

# Очистить label
    def run_clean(self):
        self.main_label.setText('')
        self.operation = ''
        self.open_bracket_number = 0
        self.close_bracket_number = 0

#
# Удаление последнего элемента
    def run_back(self):
        if self.main_label.text() != '':
            if self.main_label.text()[-1] == '(':
                self.open_bracket_number -= 1
            if self.main_label.text()[-1] == ')':
                self.close_bracket_number -= 1
            self.main_label.setText(self.main_label.text()[:-1])
            if self.main_label.text() != '':
                if self.main_label.text()[-1] in ['+', '-', '*', '/', '^', '(', ')']:
                    self.operation = self.main_label.text()[-1]

# открывает отдельное окно с историей ответов из базы данных
    def run_history(self):
        self.history.show()
        self.history.show_database()

# Вывод выражения в label
    def run_eq(self):
        try:
            expression = self.main_label.text()
            self.main_label.setText(self.main_label.text().replace('^', '**'))
            self.main_label.setText(str(eval(self.main_label.text())))
            answer = self.main_label.text()
            con = sqlite3.connect('history.db')
            cur = con.cursor()
            cur.execute(f"""INSERT INTO history(expression, answer) VALUES('{expression}', '{answer}')""").fetchall()
            con.commit()
        except Exception as e:
            a = str(e)
            self.show_message(a)


#
#
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
