import sys
from PyQt4 import QtCore, QtGui
from ui import main


class Calculator_Class(main.Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self):
        super(Calculator_Class, self).__init__()
        self.setupUi(self)

        self.pb_0.clicked.connect(lambda: self.display_screen('0'))
        self.pb_1.clicked.connect(lambda: self.display_screen('1'))
        self.pb_2.clicked.connect(lambda: self.display_screen('2'))
        self.pb_3.clicked.connect(lambda: self.display_screen('3'))
        self.pb_4.clicked.connect(lambda: self.display_screen('4'))
        self.pb_5.clicked.connect(lambda: self.display_screen('5'))
        self.pb_6.clicked.connect(lambda: self.display_screen('6'))
        self.pb_7.clicked.connect(lambda: self.display_screen('7'))
        self.pb_8.clicked.connect(lambda: self.display_screen('8'))
        self.pb_9.clicked.connect(lambda: self.display_screen('9'))
        self.pb_dot.clicked.connect(lambda: self.display_screen('.'))

        self.pb_add.clicked.connect(lambda: self.display_screen(' + '))
        self.pb_minus.clicked.connect(lambda: self.display_screen(' - '))
        self.pb_divide.clicked.connect(lambda: self.display_screen(' / '))
        self.pb_multiply.clicked.connect(lambda: self.display_screen(' * '))

        self.pb_clear.clicked.connect(self.screen_LE.clear)
        self.pb_back.clicked.connect(self.screen_LE.backspace)
        self.pb_equal.clicked.connect(self.calculation)

        self.screen_LE.setReadOnly(True)


    def display_screen(self, value):
        """
        this functions inserts data to screen
        """
        self.screen_LE.insert(value)

    def calculation(self):
        """
        Calculation function that takes valuses from screen and passes to maths function
        """
        screen_value = str(self.screen_LE.text()).split(' ')
        val1 = float(screen_value[0])
        operator = screen_value[1]
        val2 = float(screen_value[2])
        result = self.maths(val1, val2, operator)
        self.screen_LE.setText(str(result))

    def maths(self, val1, val2, operator):
        """
        Maths functions takes arguements and returns output
        """
        val1 = float(val1)
        val2 = float(val2)
        if operator is '+':
            return val1+val2
        elif operator is '-':
            return val1-val2
        elif operator is '/':
            return val1/val2
        elif operator is '*':
            return val1 * val2


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    calc = Calculator_Class()
    calc.show()
    app.exec_()
