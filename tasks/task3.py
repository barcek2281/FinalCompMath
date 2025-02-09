import numpy as np
import tkinter as tk
from tkinter import messagebox


class GaussianEliminationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gaussian Elimination with Partial Pivoting")
        self.root.geometry("400x350")

        # Instruction Label
        self.instruction_label = tk.Label(root, text="Enter coefficients and constants:")
        self.instruction_label.grid(row=0, columnspan=4, pady=5)

        self.numberOfColumns = 3
        self.numberOfRows = 3

        # Labels and Entry Fields with Default Values
        default_values = [[2, 1, -1, 8],
                          [-3, 1, 2, -11],
                          [-2, 1, 3, -3]]

        self.entries = []
        for i in range(3):
            row_entries = []
            for j in range(4):
                entry = tk.Entry(root, width=5, justify='center')
                entry.insert(0, str(default_values[i][j]))  # Insert default values
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Solve Button
        self.solve_button = tk.Button(root, text="Solve", command=self.solve_system, bg="lightblue",
                                      font=("Arial", 10, "bold"))
        self.solve_button.grid(row=4, columnspan=4, pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="Solution: ", font=("Arial", 10, "bold"))
        self.result_label.grid(row=5, columnspan=4, pady=5)

    def solve_system(self):
        try:
            # Read the input from GUI
            A = np.zeros((self.numberOfColumns, self.numberOfColumns))
            B = np.zeros(self.numberOfColumns)
            for i in range(self.numberOfColumns):
                for j in range(self.numberOfColumns):
                    A[i][j] = float(self.entries[i][j].get())
                B[i] = float(self.entries[i][3].get())

            # Solve using Gaussian elimination with partial pivoting
            x = self.gaussian_elimination(A, B)

            # Display result
            self.result_label.config(text=f"Solution: x = {x[0]:.2f}, y = {x[1]:.2f}, z = {x[2]:.2f}")
        except Exception as e:
            messagebox.showerror("Input Error", "Please enter valid numbers")

    def gaussian_elimination(self, A, B):
        n = len(B)

        for i in range(n):
            # Partial Pivoting: Find the maximum element in the current column
            max_row = i + np.argmax(abs(A[i:n, i]))
            if i != max_row:
                A[[i, max_row]] = A[[max_row, i]]  # Swap rows in A
                B[i], B[max_row] = B[max_row], B[i]  # Swap corresponding values in B

            # Make leading coefficient 1 and eliminate below rows
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                A[j] = A[j] - factor * A[i]
                B[j] = B[j] - factor * B[i]

        # Back substitution
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (B[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        return x


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = GaussianEliminationApp(root)
    root.mainloop()
