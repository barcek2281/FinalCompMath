import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def f(x):
    return x ** 4 - 5 * x ** 2 + 4


def bisection_method(a, b, tol=1e-6):
    iterations = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return c, iterations


def false_position_method(a, b, tol=1e-6):
    iterations = 0
    c = a
    while abs(f(c)) > tol:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return c, iterations


class RootFindingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Root Finding - Variant 7 Task 2")

        self.create_widgets()
        self.plot_function()

    def create_widgets(self):
        frame = Frame(self.root)
        frame.pack()

        Label(frame, text="Choose Method:").grid(row=0, column=0)
        self.method_var = StringVar(value="Bisection")
        self.method_menu = ttk.Combobox(frame, textvariable=self.method_var, values=["Bisection", "False Position"])
        self.method_menu.grid(row=0, column=1)

        Button(frame, text="Find Root", command=self.calculate_root).grid(row=1, columnspan=2)

        self.result_var = StringVar()
        Label(frame, textvariable=self.result_var).grid(row=2, columnspan=2)

    def plot_function(self):
        x = np.linspace(0, 3, 400)
        y = f(x)

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, y, label="f(x) = x⁴ - 5x² + 4")
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid()
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def calculate_root(self):
        a, b = 0, 3
        if self.method_var.get() == "Bisection":
            root, iterations = bisection_method(a, b)
        else:
            root, iterations = false_position_method(a, b)

        actual_root = 2  # One of the roots (for comparison)
        rel_error = abs((root - actual_root) / actual_root)

        self.result_var.set(f"Root: {root:.6f}, Iterations: {iterations}, Relative Error: {rel_error:.6f}")


if __name__ == "__main__":
    root = Tk()
    app = RootFindingApp(root)
    root.mainloop()
