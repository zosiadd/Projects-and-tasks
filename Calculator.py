import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("303x252")

        self.calculation = ""
        self.text_result = tk.Text(root, height=2, width=16, font=("Times New Roman", 24))
        self.text_result.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=10)
        self.create_buttons()


    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.update_display()


    def set_operation(self, op):
        if self.calculation != "" and self.calculation[-1] not in "+-*/":
            self.calculation += str(op)
            self.update_display()


    def evaluate(self):
        try:
            result = eval(self.calculation)
            full_equation = f"{self.calculation}={result}"
            
            self.text_result.delete(1.0, "end")
            self.text_result.insert(1.0, full_equation)
            self.calculation = str(result)
        except:
            self.clear_field()
            self.text_result.insert(1.0, "Error")


    def clear_field(self):
        self.calculation = ""
        self.text_result.delete(1.0, "end")


    def update_display(self):
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)


    def create_buttons(self):
        # Przyciski numeryczne
        buttons = [
            ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
            ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
            ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
            ("0", 5, 2),
        ]

        for (text, row, col) in buttons:
            tk.Button(self.root, text=text,
                      command=lambda t=text: self.add_to_calculation(t),
                      width=6, font=("Times New Roman", 15),fg="#362602", bg="navajo white",activebackground="#fffdf0").grid(row=row, column=col)

        tk.Button(self.root, text="+", command=lambda: self.set_operation("+"), width=6, font=("Times New Roman",15),fg="#362602",bg="cornsilk",activebackground="#fffdf0").grid(row=2, column=4)
        tk.Button(self.root, text="-", command=lambda: self.set_operation("-"), width=6, font=("Times New Roman",15),fg="#362602",bg="cornsilk",activebackground="#fffdf0").grid(row=3, column=4)
        tk.Button(self.root, text="*", command=lambda: self.set_operation("*"), width=6, font=("Times New Roman",15),fg="#362602",bg="cornsilk",activebackground="#fffdf0").grid(row=4, column=4)
        tk.Button(self.root, text="/", command=lambda: self.set_operation("/"), width=6, font=("Times New Roman",15),fg="#362602",bg="cornsilk",activebackground="#fffdf0").grid(row=5, column=4)
        tk.Button(self.root, text="=", command=self.evaluate, width=6, font=("Times New Roman", 15),fg="#362602", bg="NavajoWhite2",activebackground="#fffdf0").grid(row=5, column=3)
        tk.Button(self.root, text="C", command=self.clear_field, width=6, font=("Times New Roman", 15),fg="#362602", bg="NavajoWhite2",activebackground="#fffdf0").grid(row=5, column=1)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()