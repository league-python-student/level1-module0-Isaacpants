from tkinter import messagebox, simpledialog, Tk
import tkinter as tk


# 4. Create an app like the one show in the pictures in this package, 'guest_book_add.png'
# and 'guest_book_print'
from tkinter import messagebox, simpledialog, Tk


class GuestBook(tk.Tk):


    def __init__(self, parent):
        super().__init__(parent)
        self.guest_list = list()

        self.add_guest_button = tk.Button(self, text='Add guest', command=lambda: self.add_guest_button_pressed())
        self.view_guests_button = tk.Button(self, text='View guests', command=lambda: self.view_guests_button_pressed())
        self.ok_button = tk.Button(self, text='Ok', command=lambda: self.ok_button_pressed())
        self.cancel_button = tk.Button(self, text='Cancel', command=lambda: self.cancel_button_pressed())
        self.guest_name = tk.Entry(self)

        self.add_guest_button.place(x=0, y=75)
        self.view_guests_button.place(x=125, y=75)
        #self.ok_button.place(x=250, y=75)
        #self.cancel_button.place(x=375, y=75)
        self.guest_name.place(x=50, y=25)

    def add_guest_button_pressed(self):

        guest_name_entry = self.guest_name.get()
        list_len = len(self.guest_list)
        self.guest_list.insert(list_len, guest_name_entry)
        self.guest_name.delete(0, len(self.guest_name.get()))


    def view_guests_button_pressed(self):
        guest_string = ''
        print(self.guest_list)
        for i, element in enumerate(self.guest_list):
            guest_string += str(i+1) + ': '+ element + '\n'
        messagebox.showinfo(title="Guest List", message=guest_string)



if __name__ == '__main__':
    # 1. Make a new GuestBook
    gb = GuestBook(None)

    # 2. Set the title
    gb.title('Guest Book')
    gb.geometry('300x200')
    # 3. Run your game's mainloop
    gb.mainloop()
