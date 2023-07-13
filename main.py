import tkinter as tk
from tkinter import messagebox


class TipCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Tip Calculator")

        # Change the root background color
        root.config(bg='#FFD1DC')  # Pastel pink

        self.total_label = tk.Label(root, text="Total bill:", bg='#FFD1DC')
        self.total_entry = tk.Entry(root)

        self.tip_label = tk.Label(root, text="Tip (10, 12, or 15):", bg='#FFD1DC')
        self.tip_entry = tk.Entry(root)

        self.split_label = tk.Label(root, text="Split (Number of people):", bg='#FFD1DC')
        self.split_entry = tk.Entry(root)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_tip,
                                          bg='#D0F0C0')  # Pastel green

        self.total_label.pack()
        self.total_entry.pack()

        self.tip_label.pack()
        self.tip_entry.pack()

        self.split_label.pack()
        self.split_entry.pack()

        self.calculate_button.pack()

    def calculate_tip(self):
        total = float(self.total_entry.get())
        tip = int(self.tip_entry.get())
        split = int(self.split_entry.get())

        bill_per_person = total * (1 + (tip / 100)) / split

        final_amount = "{:.2f}".format(bill_per_person, 2)

        if tip in [10, 12, 15]:
            messagebox.showinfo("Bill", f"Each person should pay: ${final_amount}")
        else:
            messagebox.showinfo("Error", "Tip should be 10, 12 or 15.")


root = tk.Tk()
my_tip_calculator = TipCalculator(root)
root.mainloop()
