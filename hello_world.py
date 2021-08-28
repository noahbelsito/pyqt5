import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    # creating an application object of QApplication class
    app = QApplication(sys.argv)
    # a QWidget object creates top level window
    w = QWidget()
    # add a QLabel object in it
    b = QLabel(w)
    # set the caption of label as "hello world"
    b.setText("Hello World!")
    # define the size and position of window
    w.setGeometry(100, 100, 200, 50)
    # move the caption
    b.move(50, 20)
    # set the title of window
    w.setWindowTitle("PyQt5")
    # shows the widget
    w.show()
    # enter the mainloop of application by app.exec_() method
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()


# Object oriented solution
# creates a class definition using the QWidget cass
class Window(QWidget):
    # when this class is initialized
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.resize(200, 50)
        self.setWindowTitle("PyQt5")
        self.label = QLabel(self)
        self.label.setText("Hello World")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50, 20)


def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
