import numpy as np
import tkinter as tk
from tkinter import messagebox


class MatrixInversionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Iterative Matrix Inversion")
        self.root.geometry("350x300")

        # Instruction Label
        self.instruction_label = tk.Label(root, text="Enter 3x3 matrix:")
        self.instruction_label.grid(row=0, columnspan=3, pady=5)

        # Labels and Entry Fields with Default Values
        default_values = [[1, 2, 3], [0, -1, 4], [5, 6, -1]]
        self.entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(root, width=5, justify='center')
                entry.insert(0, str(default_values[i][j]))  # Insert default values
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Solve Button
        self.solve_button = tk.Button(root, text="Compute Inverse", command=self.compute_inverse, bg="lightblue",
                                      font=("Arial", 10, "bold"))
        self.solve_button.grid(row=4, columnspan=3, pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="Inverse Matrix:", font=("Arial", 10, "bold"))
        self.result_label.grid(row=5, columnspan=3, pady=5)

    def compute_inverse(self):
        try:
            # Read the input from GUI
            A = np.zeros((3, 3))
            for i in range(3):
                for j in range(3):
                    A[i][j] = float(self.entries[i][j].get())

            # Compute inverse using iterative method
            A_inv = self.iterative_matrix_inversion(A)

            # Display result
            inverse_text = "\n".join([" ".join(f"{val:.4f}" for val in row) for row in A_inv])
            self.result_label.config(text=f"Inverse Matrix:\n{inverse_text}")
        except Exception as e:
            messagebox.showerror("Input Error", "Please enter valid numbers")

    def iterative_matrix_inversion(self, A, tol=1e-6, max_iter=100):
        n = A.shape[0]
        I = np.eye(n)
        X = np.eye(n) / np.trace(A)  # Initial guess based on trace

        for _ in range(max_iter):
            R = I - np.dot(A, X)
            X = X + np.dot(X, R)
            if np.linalg.norm(R, ord=np.inf) < tol:
                break

        return X


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixInversionApp(root)
    root.mainloop()
