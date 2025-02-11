import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import uic

class PolynomialCurveFitting(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.input_field = QLineEdit(self)
        self.button = QPushButton("Plot", self)
        self.button.clicked.connect(self.plot_curve)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter x values separated by space:"))
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def plot_curve(self):
        self.ax.clear()
        x = np.array(list(map(float, self.input_field.text().split())))
        y = x ** 2
        coeffs = np.polyfit(x, y, 2)
        poly = np.poly1d(coeffs)
        x_range = np.linspace(min(x) - 1, max(x) + 1, 100)
        self.ax.plot(x_range, poly(x_range), label='Fitted Quadratic Curve')
        self.ax.scatter(x, y, color='red', label='Data Points')
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()
