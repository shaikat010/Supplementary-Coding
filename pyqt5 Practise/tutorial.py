from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200, 200, 300, 300)  # from the top left
        self.setWindowTitle("Shaikat's Tutorial")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My First Label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You clicked the button")
        self.update()

    def update(self):
        self.label.adjustSize()



# def clicked():
#     print("click it")


def window():
    app = QApplication(sys.argv)
    #win = QMainWindow()
    win = MyWindow()

    # label = QtWidgets.QLabel(win)
    # label.setText("My First Label")
    # label.move(50,50)
    #
    # b1 = QtWidgets.QPushButton(win)
    # b1.setText("Click Me")
    # b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec())

window()


