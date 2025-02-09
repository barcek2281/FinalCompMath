import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def f(x):
    return x ** 3 - 3 * x + 2

class GraphicalMethodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphical Method - Variant 7 Task 1")

        self.create_widgets()
        self.plot_function()

    def create_widgets(self):
        frame = Frame(self.root)
        frame.pack()

        Label(frame, text="Enter Numerical Root:").grid(row=0, column=0)
        self.entry_root = Entry(frame)
        self.entry_root.grid(row=0, column=1)

        Button(frame, text="Calculate Absolute Error", command=self.calculate_error).grid(row=1, columnspan=2)

        self.result_var = StringVar()
        Label(frame, textvariable=self.result_var).grid(row=2, columnspan=2)

    def plot_function(self):
        x = np.linspace(-2, 2, 400)
        y = f(x)

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, y, label="f(x) = x³ - 3x + 2")
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid()
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def calculate_error(self):
        try:
            numerical_root = float(self.entry_root.get())
            actual_root = 1  # One of the roots (can be refined numerically)
            abs_error = abs(numerical_root - actual_root)
            self.result_var.set(f"Absolute Error: {abs_error:.6f}")
        except ValueError:
            self.result_var.set("Invalid Input!")


if __name__ == "__main__":
    root = Tk()
    app = GraphicalMethodApp(root)
    root.mainloop()
