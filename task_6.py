import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import uic

class LagrangeInterpolation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.x_input = QLineEdit(self)
        self.y_input = QLineEdit(self)
        self.target_input = QLineEdit(self)
        self.button = QPushButton("Interpolate", self)
        self.button.clicked.connect(self.plot_interpolation)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter x values:"))
        layout.addWidget(self.x_input)
        layout.addWidget(QLabel("Enter y values:"))
        layout.addWidget(self.y_input)
        layout.addWidget(QLabel("Enter target x:"))
        layout.addWidget(self.target_input)
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def lagrange(self, x, y, x_target):
        n = len(x)
        result = 0
        for i in range(n):
            term = y[i]
            for j in range(n):
                if i != j:
                    term *= (x_target - x[j]) / (x[i] - x[j])
            result += term
        return result

    def plot_interpolation(self):
        self.ax.clear()
        x = np.array(list(map(float, self.x_input.text().split())))
        y = np.array(list(map(float, self.y_input.text().split())))
        x_target = float(self.target_input.text())
        interpolated_value = self.lagrange(x, y, x_target)
        self.ax.scatter(x_target, interpolated_value, color='green', label='Interpolated Point')
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()
