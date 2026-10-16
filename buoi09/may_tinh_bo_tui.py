import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy tính bỏ túi")
        self.root.geometry("320x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Bỏ viền đen cho tất cả Button
        root.option_add("*Button.borderWidth", 0)
        root.option_add("*Button.relief", "flat")
        root.option_add("*Button.highlightThickness", 0)

        self.expression = ""

        # ===== Ô hiển thị (bỏ viền đen) =====
        self.entry = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=0,
            relief="flat",
            highlightthickness=0,
            bg="#f0f0f0",
            fg="#000000"
        )
        self.entry.grid(row=0, column=0, columnspan=4,
                        padx=10, pady=10, ipady=10, sticky="nsew")

        # ===== Định nghĩa các nút =====
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('⌫', 5, 2), ('=', 5, 3),
        ]

        for (text, row, col) in buttons:
            color = "#e0e0e0"
            if text in ('+', '-', '*', '/'):
                color = "#e0e0e0"
            elif text == '=':
                color = "#e0e0e0"
            elif text == 'C':
                color = "#e0e0e0"

            btn = tk.Button(
                root,
                text=text,
                font=("Arial", 18, "bold"),
                bg=color,
                activebackground="#c0c0c0",
                width=5,
                height=2,
                bd=0,
                relief="flat",
                highlightthickness=0,
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

        root.bind("<Return>", lambda e: self.on_button_click('='))
        root.bind("<BackSpace>", lambda e: self.on_button_click('⌫'))
        root.bind("<Key>", self.on_key_press)

    def on_button_click(self, value):
        if value == 'C':
            self.expression = ""
        elif value == '⌫':
            self.expression = self.expression[:-1]
        elif value == '=':
            self.calculate()
            return
        else:
            self.expression += value
        self.update_display()

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def calculate(self):
        if not self.expression:
            return
        try:
            allowed = set("0123456789+-*/(). ")
            if not all(c in allowed for c in self.expression):
                raise ValueError("Ký tự không hợp lệ")
            result = eval(self.expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Lỗi", "Không thể chia cho 0!")
            self.expression = ""
            self.update_display()
        except Exception:
            messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
            self.expression = ""
            self.update_display()

    def on_key_press(self, event):
        char = event.char
        if char in "0123456789+-*/().":
            self.expression += char
            self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()