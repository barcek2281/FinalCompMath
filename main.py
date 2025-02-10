import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from task_1 import Task1

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi("untitled.ui", self)
        self.task1 = Task1(self)
        self.tab1_verticalLayout.addWidget(self.task1)

        self.tab1_toolButton.clicked.connect(self.do_task1)

    def do_task1(self):

        x_range = tuple(map(int, self.tab1_lineEdit.text().split()))
        self.task1.plot_graph(x_range)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
