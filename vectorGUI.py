from tkinter import *
import math

class Vec2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

class Vector(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = 'a: ').grid(row=1, column=0, sticky=E)
        Label(self, text = 'X: ').grid(row=1, column=1, sticky=W)
        Label(self, text = 'Y: ').grid(row=1, column=3, sticky=W)


        Label(self, text = 'b: ').grid(row=2, column=0, sticky=E)
        Label(self, text = 'X: ').grid(row=2, column=1, sticky=W)
        Label(self, text = 'Y: ').grid(row=2, column=3, sticky=W)


        Label(self, text = 'c: ').grid(row=3, column=0, sticky=E)
        Label(self, text = 'X: ').grid(row=3, column=1, sticky=W)
        Label(self, text = 'Y: ').grid(row=3, column=3, sticky=W)

        Label(self, text = 'd: ').grid(row=4, column=0, sticky=E)
        Label(self, text = 'X: ').grid(row=4, column=1, sticky=W)
        Label(self, text = 'Y: ').grid(row=4, column=3, sticky=W)

        self.a_x = Entry(self, width=3)
        self.a_y = Entry(self, width=3)

        self.b_x = Entry(self, width=3)
        self.b_y = Entry(self, width=3)

        self.c_x = Entry(self, width=3)
        self.c_y = Entry(self, width=3)

        self.d_x = Entry(self, width=3)
        self.d_y = Entry(self, width=3)

        self.a_x.grid(row=1, column=2, sticky=W)
        self.a_y.grid(row=1, column=4, sticky=W)

        self.b_x.grid(row=2, column=2, sticky=W)
        self.b_y.grid(row=2, column=4, sticky=W)

        self.c_x.grid(row=3, column=2, sticky=W)
        self.c_y.grid(row=3, column=4, sticky=W)

        self.d_x.grid(row=4, column=2, sticky=W)
        self.d_y.grid(row=4, column=4, sticky=W)



        Button(self, text="Add", command=self.create, width=13).grid(row=5, column=0, pady=10, padx=10)

        #Button(self, text='Distanse from p1 to p2',command=self.distance12, width = 16).grid(row=6, column=0, pady=10, padx=10)
        #Button(self, text='Distanse from p1 to p3',command=self.distance13, width = 16).grid(row=7, column=0, pady=10, padx=10)
        #Button(self, text='Distanse from p2 to p3',command=self.distance23, width = 16).grid(row=8, column=0, pady=10, padx=10)


        self.answer=Text(self, width=20, height=5, wrap=WORD)
        self.answer.grid(row=5, column=6, pady=10, padx=10, sticky=E)

    def create(self):
        try:
            self.v1 = Vec2D(int(self.a_x.get()),int(self.a_y.get()))
            self.v2 = Vec2D(int(self.b_x.get()),int(self.b_y.get()))
            self.v3 = Vec2D(int(self.c_x.get()),int(self.c_y.get()))
            self.v4 = Vec2D(int(self.d_x.get()),int(self.d_y.get()))

            self.answ = 'Three Vector Added: ' + '\n' + str(self.v1) + '\n' + str(self.v2) + '\n' + str(self.v3) + '\n' + str(self.v4)
        except ValueError:
            self.answ = 'All three Point need added!'
        self.calculate()


    def calculate(self):
        self.answer.delete(0.0,END)
        self.answer.insert(0.0,self.answ)

        self.a_x.delete(0)
        self.a_y.delete(0)

        self.b_x.delete(0)
        self.b_y.delete(0)

        self.c_x.delete(0)
        self.c_y.delete(0)

        self.d_x.delete(0)
        self.d_y.delete(0)

root=Tk()
root.title("Vector")
root.geometry('700x500')
calc=Vector(root)
root.mainloop()
