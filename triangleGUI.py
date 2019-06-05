from tkinter import *
import math
import numpy as np
from numpy.linalg import norm
from sympy import *
from sympy.abc import x, y, z

class Point(object):

    COUNT = 0

    def __init__(self, x, y, z):
        '''Определим переменные x и y и z'''
        self.X = x
        self.Y = y
        self.Z = z

    def move(self, dx, dy, dz):
        '''Определяет, куда движутся x и y'''
        self.X = self.X + dx
        self.Y = self.Y + dy
        self.Z = self.Z + dz

    def __str__(self):
        return "Point(%s,%s,%s)"%(self.X, self.Y, self.Z)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getZ(self):
        return self.Z

    def distance(self, other):
        dx = self.X- other.X
        dy = self.Y - other.Y
        dz = self.Z - other.Z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def distanceToLine(self, a,b,c,q,p,t):

        def strToInt(n):
            for a in list(n):
                if a == '/':
                    index = list(n).index('/')
                    s = int(n[:index])/int(n[index+1:])
                    return float("%.2f" % s)
            return float(n)

        m0 = (x-self.X)*q + (y-self.Y)*p + (z-self.Z)*t
        m1 = (x+a)/q - (y+b)/(p)
        m2 = (x+a)/q - (z+c)/t
        m3 = (z+c)/t - (y+b)/(p)

        solve = (str(linsolve([m1,m2,m3,m0],(x,y,z)))[2:-2]).split(',')

        H = Point(strToInt(str(solve[0])),strToInt(str(solve[1])),strToInt(str(solve[2])))
        return self.distance(H)

2
class Triangle(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = 'First: ').grid(row=1, column=0, sticky=W)
        Label(self, text = 'X: ').grid(row=1, column=1, sticky=W)
        Label(self, text = 'Y: ').grid(row=1, column=3, sticky=W)
        Label(self, text = 'Z: ').grid(row=1, column=5, sticky=W)

        Label(self, text = 'Second: ').grid(row=2, column=0, sticky=W)
        Label(self, text = 'X: ').grid(row=2, column=1, sticky=W)
        Label(self, text = 'Y: ').grid(row=2, column=3, sticky=W)
        Label(self, text = 'Z: ').grid(row=2, column=5, sticky=W)

        Label(self, text = 'Third: ').grid(row=3, column=0, sticky=W)
        Label(self, text = 'X: ').grid(row=3, column=1, sticky=W)
        Label(self, text = 'Y: ').grid(row=3, column=3, sticky=W)
        Label(self, text = 'Z: ').grid(row=3, column=5, sticky=W)

        Label(self, text = 'Add direct coefficients in format \n "(x+a)/q = (y+b)/p = (z+c)/t": ').grid(row=9, column=0, sticky=E)

        Label(self, text = 'a: ').grid(row=10, column=1, sticky=W)
        Label(self, text = 'q: ').grid(row=10, column=3, sticky=W)

        Label(self, text = 'b: ').grid(row=11, column=1, sticky=W)
        Label(self, text = 'p: ').grid(row=11, column=3, sticky=W)

        Label(self, text = 'c: ').grid(row=12, column=1, sticky=W)
        Label(self, text = 't: ').grid(row=12, column=3, sticky=W)

        self.first_x = Entry(self, width=3)
        self.first_y = Entry(self, width=3)
        self.first_z = Entry(self, width=3)

        self.second_x = Entry(self, width=3)
        self.second_y = Entry(self, width=3)
        self.second_z = Entry(self, width=3)

        self.third_x = Entry(self, width=3)
        self.third_y = Entry(self, width=3)
        self.third_z = Entry(self, width=3)

        self.dir_a = Entry(self, width=3)
        self.dir_q = Entry(self, width=3)

        self.dir_b = Entry(self, width=3)
        self.dir_p = Entry(self, width=3)

        self.dir_c = Entry(self, width=3)
        self.dir_t = Entry(self, width=3)

        self.first_x.grid(row=1, column=2, sticky=W)
        self.first_y.grid(row=1, column=4, sticky=W)
        self.first_z.grid(row=1, column=6, sticky=W)

        self.second_x.grid(row=2, column=2, sticky=W)
        self.second_y.grid(row=2, column=4, sticky=W)
        self.second_z.grid(row=2, column=6, sticky=W)

        self.third_x.grid(row=3, column=2, sticky=W)
        self.third_y.grid(row=3, column=4, sticky=W)
        self.third_z.grid(row=3, column=6, sticky=W)

        self.dir_a.grid(row=10, column=2, sticky=W)
        self.dir_q.grid(row=10, column=4, sticky=W)

        self.dir_b.grid(row=11, column=2, sticky=W)
        self.dir_p.grid(row=11, column=4, sticky=W)

        self.dir_c.grid(row=12, column=2, sticky=W)
        self.dir_t.grid(row=12, column=4, sticky=W)

        Button(self, text="Add", command=self.createPoint, width=13).grid(row=4, column=0, pady=10, padx=10)
        Button(self, text="Add", command=self.createLine, width=13).grid(row=13, column=0, pady=10, padx=10)

        Button(self, text='Triangle Square', command=self.triangleSquare, width = 13).grid(row=5, column=0, pady=10, padx=10)

        Button(self, text='Distanse from p1 to p2',command=self.distance12, width = 18).grid(row=6, column=0, pady=10, padx=10)
        Button(self, text='Distanse from p1 to p3',command=self.distance13, width = 18).grid(row=7, column=0, pady=10, padx=10)
        Button(self, text='Distanse from p2 to p3',command=self.distance23, width = 18).grid(row=8, column=0, pady=10, padx=10)

        Button(self, text='Distanse from p1 to line',command=self.distance1line, width = 18).grid(row=10, column=0, pady=10, padx=10)
        Button(self, text='Distanse from p2 to line',command=self.distance2line, width = 18).grid(row=11, column=0, pady=10, padx=10)
        Button(self, text='Distanse from p3 to line',command=self.distance3line, width = 18).grid(row=12, column=0, pady=10, padx=10)


        self.answer=Text(self, width=20, height=5, wrap=WORD)
        self.answer.grid(row=4, column=6, pady=10, padx=10, sticky=E)

    def createPoint(self):
        try:
            self.p1 = Point(int(self.first_x.get()),int(self.first_y.get()),int(self.first_z.get()))
            self.p2 = Point(int(self.second_x.get()),int(self.second_y.get()),int(self.second_z.get()))
            self.p3 = Point(int(self.third_x.get()),int(self.third_y.get()),int(self.third_z.get()))

            self.answ = 'Three Point Added: ' + '\n' + str(self.p1) + '\n' + str(self.p2) + '\n' + str(self.p3)
        except ValueError:
            self.answ = 'All three Point need added!'
        self.calculate()

    def createLine(self):
        try:
            self.a = int(self.dir_a.get())
            self.b = int(self.dir_b.get())
            self.c = int(self.dir_c.get())
            self.q = int(self.dir_q.get())
            self.p = int(self.dir_p.get())
            self.t = int(self.dir_t.get())

            self.answ = 'Three Line Added: ' + '\n' + str(self.a) + ',' + str(self.b) + ',' + str(self.c)+ ',' + str(self.q) + ',' + str(self.p) + ',' + str(self.t)
        except ValueError:
            self.answ = 'All three Point need added!'
        self.calculate()

    def triangleSquare(self):
        try:
            A = math.sqrt((self.p3.X - self.p2.X)**2 + (self.p3.Y-self.p2.Y)**2 + (self.p3.Z-self.p2.Z)**2)
            B = math.sqrt((self.p2.X-self.p1.X)**2 + (self.p2.Y-self.p1.Y)**2 + (self.p2.Z-self.p1.Z)**2)
            C = math.sqrt((self.p3.X-self.p1.X)**2 + (self.p3.Y-self.p1.Y)**2 + (self.p3.Z-self.p1.Z)**2)
            P = (A +B +C)/2
            S = math.sqrt(P*(P-A)*(P-B)*(P-C))

            self.answ = "Sqaure of triangle: " + "\n" + str(("%.2f" % S))
        except ValueError:
            self.answ = 'All three Point need added!'
        self.calculate()

    def distance12(self):
        try:
            dist = self.p1.distance(self.p2)
            self.answ = dist
        except ValueError:
            self.answ = 'All three Point need added!'
        self.calculate()

    def distance13(self):
        try:
            dist = self.p1.distance(self.p3)
            self.answ = dist
        except ValueError:
            self.answ = 'All three Point need added!'
        self.calculate()

    def distance23(self):
        try:
            dist = self.p2.distance(self.p3)
            self.answ = dist
        except ValueError:
            self.answ = 'All three Point need added!'
        self.calculate()

    def distance1line(self):
            #distanceToLine(int(self.dir_a.get()),int(self.dir_b.get()),int(self.dir_c.get()),int(self.dir_q.get()),int(self.dir_p.get()),int(self.dir_t.get()))
        dist = self.p1.distanceToLine(self.a,self.b,self.c,self.q,self.p,self.t)
        self.answ = dist

        self.calculate()

    def distance2line(self):
        dist = self.p2.distanceToLine(self.a,self.b,self.c,self.q,self.p,self.t)
        self.answ = dist

        self.calculate()

    def distance3line(self):
        dist = self.p3.distanceToLine(self.a,self.b,self.c,self.q,self.p,self.t)
        self.answ = dist

        self.calculate()
#distanceToLine(self.a,self.b,self.c,self.q,self.p,self.t)
    def calculate(self):
        self.answer.delete(0.0,END)
        self.answer.insert(0.0,self.answ)

        self.first_x.delete(00)
        self.first_y.delete(00)
        self.first_z.delete(00)

        self.second_x.delete(00)
        self.second_y.delete(00)
        self.second_z.delete(00)

        self.third_x.delete(00)
        self.third_y.delete(00)
        self.third_z.delete(00)

        self.dir_a.delete(00)
        self.dir_q.delete(00)

        self.dir_b.delete(00)
        self.dir_p.delete(00)

        self.dir_c.delete(00)
        self.dir_t.delete(00)

root=Tk()
root.title("Triangle")
root.geometry('600x800')
calc=Triangle(root)
root.mainloop()
