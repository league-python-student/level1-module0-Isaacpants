import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, title='hello')
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        self.plus_button = tk.Button(self, text='Plus(+)')
        self.plus_button.place(x=100,y=100)
        self.minus_button = tk.Button(self, text='Minus(-)')
        self.plus_button.place(x=200, y=100)
        self.multiply_button = tk.Button(self, text='Multiply(x,*)')
        self.plus_button.place(x=300, y=100)
        self.divide_button = tk.Button(self, text='Divide(/)')
        self.plus_button.place(x=400, y=100)


if __name__ == '__main__':
    app = Calculator()
    app.title('hello')
    app.geometry('500x200')
    # Make a calculator app like the one shown in the calculator.png image
    # HINT: you'll need:
    # 1. a new class
    # 2. a StringVar variable
    # 3. Two tk.Entry widgets, four tk.Button widgets, and one tl.Label widget
    app.maintainloop
    pass