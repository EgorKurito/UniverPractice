"""from tkinter import *

window = Tk()

window.title("Triangle square")
window.geometry('350x200')

lbl1 = Label(window, text="Add first point: ")
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="Add second point: ")
lbl2.grid(column=1, row=1)

p1 = Entry(window, width=10)
p1.grid(column=1, row=0)

p2 = Entry(window, width=10)
p2.grid(column=1, row=0)

def clickedOne():
    res = "Point 1 added: " + p1.get()
    lbl1.configure(text= res)

def clickedTwo():
    res = "Point 2 added: " + p2.get()
    lbl2.configure(text= res)

btn1 = Button(window, text="Click Me", command=clickedOne)
btn1.grid(column=2, row=0)

btn2 = Button(window, text="Click Me", command=clickedTwo)
btn2.grid(column=2, row=0)

window.mainloop()
"""

from tkinter import *

class Triangle(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = 'First:      Add X: ').grid(row=1, column=0, sticky=W)
        Label(self, text = 'Add Y: ').grid(row=1, column=2, sticky=W)

        Label(self, text = 'Second: Add X: ').grid(row=2, column=0, sticky=W)
        Label(self, text = 'Add Y: ').grid(row=2, column=2, sticky=W)

        Label(self, text = 'Third:     Add X: ').grid(row=3, column=0, sticky=W)
        Label(self, text = 'Add Y: ').grid(row=3, column=2, sticky=W)

        self.first_x = Entry(self, width=5)
        self.first_y = Entry(self, width=5)

        self.second_x = Entry(self, width=5)
        self.second_y = Entry(self, width=5)

        self.third_x = Entry(self, width=5)
        self.third_y = Entry(self, width=5)

        self.first_x.grid(row=1, column=1)
        self.first_y.grid(row=1, column=4)

        self.second_x.grid(row=2, column=1)
        self.second_y.grid(row=2, column=4)

        self.third_x.grid(row=3, column=1)
        self.third_y.grid(row=3, column=4)
