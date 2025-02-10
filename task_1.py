import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Task1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a Figure and Canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Layout to add Matplotlib canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Plot something
        self.plot_graph()

    def plot_graph(self, x_range=(-2, 2)):
        """Generate a simple sine wave plot"""
        self.ax.clear()
        x = np.linspace(*x_range, 100)
        y = self.f(x)
        self.ax.plot(x, y, label="")
        self.ax.grid(True)
        self.canvas.draw()  # Refresh the canvas

    def f(self, x):
        return x ** 3 - 3 * x + 2