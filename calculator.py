import tkinter as tk
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.iconbitmap("D:\Python\Calculator\icon.ico")
        self.bind("<Key>", self.on_key_press)
        self.geometry("300x400")
        self.resizable(False, False)
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        # Define color scheme
        btn_bg = "#f0f0f0"
        btn_fg = "#222"
        op_bg = "#d1e7dd"
        op_fg = "#0f5132"
        eq_bg = "#ffe066"
        eq_fg = "#7c4700"
        clr_bg = "#f8d7da"
        clr_fg = "#842029"
        disp_bg = "#e9ecef"
        disp_fg = "#212529"

        self.display.configure(bg=disp_bg, fg=disp_fg, insertbackground=disp_fg)

        for (text, row, col, *span) in buttons:
            colspan = span[0] if span else 1
            if text in {'+', '-', '*', '/'}:
                bg, fg = op_bg, op_fg
            elif text == '=':
                bg, fg = eq_bg, eq_fg
            elif text == 'C':
                bg, fg = clr_bg, clr_fg
            else:
                bg, fg = btn_bg, btn_fg
            btn = tk.Button(
            self,
            text=text,
            font=("Arial", 18),
            command=lambda t=text: self.on_button_click(t),
            bg=bg,
            fg=fg,
            activebackground="#dee2e6",
            activeforeground=fg,
            borderwidth=0,
            highlightthickness=0
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def on_key_press(self, event):
        char = event.char
        if char in '0123456789.+-*/':
            self.on_button_click(char)
        elif event.keysym == 'Return':
            self.on_button_click('=')
        elif event.keysym in ('BackSpace', 'Delete'):
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        elif char.lower() == 'c':
            self.on_button_click('C')

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()