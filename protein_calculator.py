import tkinter as tk
from tkinter import ttk, messagebox

class ProteinCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Protein Calculator")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(
            main_frame,
            text="Daily Protein Calculator",
            font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Weight input
        weight_label = ttk.Label(main_frame, text="Enter your weight (kg):")
        weight_label.grid(row=1, column=0, pady=10)

        self.weight_entry = ttk.Entry(main_frame, width=20)
        self.weight_entry.grid(row=1, column=1, pady=10)

        # Calculate button
        calculate_button = ttk.Button(
            main_frame,
            text="Calculate Protein Needs",
            command=self.calculate_protein
        )
        calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Result label
        self.result_label = ttk.Label(
            main_frame,
            text="",
            font=("Helvetica", 12)
        )
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_protein(self):
        try:
            weight = float(self.weight_entry.get())
            if weight <= 0:
                raise ValueError("Weight must be positive")
            
            # Calculate protein needs (0.8-1.0g per kg)
            min_protein = weight * 0.8
            max_protein = weight * 1.0
            
            result_text = f"Daily protein needs: {min_protein:.1f}g - {max_protein:.1f}g"
            self.result_label.config(text=result_text)
            
        except ValueError as e:
            messagebox.showerror("Error", "Please enter a valid weight in kilograms")
            self.result_label.config(text="")

def main():
    root = tk.Tk()
    app = ProteinCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 