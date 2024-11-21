# Task 2: Calculator
import tkinter as tk
from tkinter import Label, Entry, Button, LabelFrame, messagebox


class Calculator:

    def __init__(self):
        # Creating window(root)
        self.root = tk.Tk()
        self.root.title("Calculator Experiment")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")

        # Labeling for the first number
        self.num1_entry_label = Label(
            self.root, text="Enter the first number : ", fg="white"
        )
        self.num1_entry_label.grid(row=0, column=0, padx=10, pady=10)

        # Creating first number entry
        self.num1_entry = Entry(self.root, bg="white", fg="black")
        self.num1_entry.grid(row=0, column=1)
        self.num1_entry_label.config(font=("Arial", 10))

        # Labeling for the second number
        self.num2_entry_label = Label(
            self.root, text="Enter the second number : ", fg="white"
        )
        self.num2_entry_label.grid(row=1, column=0, padx=10, pady=10)

        # Creating second number entry
        self.num2_entry = Entry(self.root, bg="white", fg="black")
        self.num2_entry.grid(row=1, column=1)
        self.num2_entry_label.config(font=("Arial", 10))

        # Creating frame for the operations
        self.operations_frame = LabelFrame(self.root, text="Operations\n ")
        self.operations_frame.grid(row=2, column=0, columnspan=6, pady=10)
        self.operations_frame.config(bg="green", font=("Arial", 12, "bold"))

        # Creating Addition operation button
        self.add_button = Button(self.operations_frame, text="+", command=self.add)
        self.add_button.grid(row=0, column=0)

        # Creating Subtraction operation button
        self.difference_button = Button(
            self.operations_frame, text="-", command=self.subtract
        )
        self.difference_button.grid(row=0, column=1)

        # Creating Multiplication operation button
        self.product_button = Button(
            self.operations_frame, text="*", command=self.multiply
        )
        self.product_button.grid(row=0, column=2)

        # Creating Division operation button
        self.quotient_button = Button(
            self.operations_frame, text="/", command=self.divide
        )
        self.quotient_button.grid(row=0, column=3)

        # Creating result label, where the result will be displayed
        self.result_label = Label(self.root, text=" ")
        self.result_label.grid(row=3, column=0, columnspan=6)
        self.result_label.config(font=("Arial", 12, "bold"), fg="white", bg="black")

        self.root.mainloop()

    # Method that performs addition operation
    def add(self):
        num1, num2 = self.get_inputs()
        self.show_result(f"Summation Result : {num1+num2}")

    # Method that performs subtraction operation
    def subtract(self):
        num1, num2 = self.get_inputs()
        self.show_result(f"Difference Result : {num1-num2}")

    # Method that performs multiplication operation
    def multiply(self):
        num1, num2 = self.get_inputs()
        self.show_result(f"Multiplication Result : {num1*num2}")

    # Method that performs division operation
    def divide(self):
        num1, num2 = self.get_inputs()

        # Exception handling (Error: Division by zero not possible)
        try:
            self.show_result(f"Quotient Result : {round(num1 / num2, 3)}")
        except ZeroDivisionError:
            self.show_error("Division by zero is not allowed.")
            return None

    # Method that get inputs from the user
    def get_inputs(self):
        # Exception handling when the user enters non integer value or str
        try:
            if self.num1_entry.get() and self.num2_entry.get() != "":
                num1, num2 = float(self.num1_entry.get()), float(self.num2_entry.get())
                return num1, num2
            else:
                self.show_error("Please enter value")
        except ValueError:
            self.show_error("Please, Enter number only")

    # Method that displays message
    def show_result(self, message):
        self.result_label.config(text=message)

    # Method that displays error messages
    def show_error(self, message):
        messagebox.showerror("Error", message)


Calculator()
