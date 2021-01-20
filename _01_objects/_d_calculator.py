import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.final_value = 'h'
        self.label_text = tk.StringVar()
        self.label_text.set('hello')
        self.label = tk.Label(self, textvariable=self.label_text, bg='white', fg='black', font=('arial', 25), relief='solid')

        self.plus_button = tk.Button(self, text='Plus(+)', command=lambda: self.plus_button_pressed())
        self.minus_button = tk.Button(self, text='Minus(-)', command=lambda: self.minus_button_pressed())
        self.multiply_button = tk.Button(self, text='Multiply(x,*)', command=lambda: self.multiply_button_pressed())
        self.divide_button = tk.Button(self, text='Divide(/)', command=lambda: self.divide_button_pressed())
        self.value_one = tk.Entry(self)
        self.value_two = tk.Entry(self)

        self.label.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)
        #self.label.place(x=100, y=125)
        self.plus_button.place(x=0, y=75)
        self.minus_button.place(x=125, y=75)
        self.multiply_button.place(x=250, y=75)
        self.divide_button.place(x=375, y=75)
        self.value_one.place(x=50, y=25)
        self.value_two.place(x=250, y=25)

    def plus_button_pressed(self):
        text_in_text_field_one = self.value_one.get()
        text_in_text_field_two = self.value_two.get()
        value_one_float = float(text_in_text_field_one)
        value_two_float = float(text_in_text_field_two)
        final_float_value = value_one_float+value_two_float
        print(value_one_float+value_two_float)
        # Update the text in the label
        self.label_text.set(final_float_value)

    def minus_button_pressed(self):
        text_in_text_field_one = self.value_one.get()
        text_in_text_field_two = self.value_two.get()
        value_one_float = float(text_in_text_field_one)
        value_two_float = float(text_in_text_field_two)
        final_float_value = value_one_float-value_two_float
        print(value_one_float+value_two_float)
        # Update the text in the label
        self.label_text.set(final_float_value)

    def multiply_button_pressed(self):
        text_in_text_field_one = self.value_one.get()
        text_in_text_field_two = self.value_two.get()
        value_one_float = float(text_in_text_field_one)
        value_two_float = float(text_in_text_field_two)
        final_float_value = value_one_float * value_two_float
        print(value_one_float * value_two_float)
        #Update the text in the label
        self.label_text.set(final_float_value)

    def divide_button_pressed(self):
        text_in_text_field_one = self.value_one.get()
        text_in_text_field_two = self.value_two.get()
        value_one_float = float(text_in_text_field_one)
        value_two_float = float(text_in_text_field_two)
        final_float_value = value_one_float / value_two_float
        print(value_one_float / value_two_float)
        # Update the text in the label
        self.label_text.set(final_float_value)


if __name__ == '__main__':
    app = Calculator()
    app.title('Calculator')
    app.geometry('500x200')
    # Make a calculator app like the one shown in the calculator.png image
    # HINT: you'll need:
    # 1. a new class
    # 2. a StringVar variable
    # 3. Two tk.Entry widgets, four tk.Button widgets, and one tl.Label widget
    app.mainloop()
    pass