import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")

        expression = QLineEdit(self)
        expression.setPlaceholderText("Enter an expression")
        expression.setAlignment()
        layout = QVBoxLayout()
        widgets = [
            QLabel,
            QLineEdit,
            QPushButton,
            QRadioButton,
        ]

        for w in widgets:
            layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
