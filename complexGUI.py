from math import cos, sin, sqrt, atan2
from tkinter import *

def factorial(n):           #факториал (нужен для синуса)
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
class Complex: #Класс комплексных чисел
    def __init__(self, real, imag = 0):
        self.real = real       # Поля
        self.imag = imag
    def __str__(self): # Строковое представление числа
        sign = '+' if self.imag >= 0 else ''
        if self.imag == 0:
            return '{}'.format(self.real)
        else:
            return '{}{}{}i'.format(self.real, sign, self.imag)
    def __add__(self, c2): # сложение
        real = self.real + c2.real
        imag = self.imag + c2.imag
        return Complex(real, imag)
    def __sub__(self, c2): # вычитание
        real = self.real - c2.real
        imag = self.imag - c2.imag
        return Complex(real, imag)
    def __mul__(self, c2): # умножение
        real = self.real * c2.real - self.imag * c2.imag
        imag = self.imag * c2.real + self.real * c2.imag
        return Complex(real, imag)
    def div(self, c2): # деление
        real = (self.real * c2.real - self.imag * c2.imag) / ((c2.real ** 2) + (c2.imag ** 2))
        imag = (self.real * c2.imag + self.imag * c2.real) / ((c2.real ** 2) + (c2.imag ** 2))
        return Complex(real, imag)
    def abs(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    def __pow__(self, n):  # степень
        phi = atan2(self.imag, self.real)
        r = sqrt(self.real * self.real + self.imag * self.imag)
        R = r ** n
        Phi = n * phi
        real = R * cos(Phi)
        imag = R * sin(Phi)
        return Complex(real, imag)
    def csin(self,n):   #синус порядка аппроксимации 2n+1
        i = 0
        s = Complex(0,0)
        while i <= n:
            #s += ((-1)**i)*(self**(2*i+1))/factorial(2*i+1)
            s += (Complex(((-1)**i))*(self**(2*i+1))).div(Complex(factorial(2*i+1)))
            i+=1
        return s


class Comp(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = 'Complex num: ').grid(row=1, column=0, sticky=W)
        Label(self, text = 'Re: ').grid(row=1, column=1, sticky=W)
        Label(self, text = 'Im: ').grid(row=1, column=3, sticky=W)
        Label(self, text = 'Синус порядка аппроксимации 2n+1: ').grid(row=2, column=0, sticky=W)


        self.Re_num = Entry(self, width=3)
        self.Im_num = Entry(self, width=3)
        self.sin = Entry(self, width=3)

        self.Re_num.grid(row=1, column=2, sticky=W)
        self.Im_num.grid(row=1, column=4, sticky=W)
        self.sin.grid(row=2, column=2, sticky=W)


        Button(self, text="Add", command=self.create, width=13).grid(row=3, column=0, pady=10, padx=10)
        Button(self, text="Add sin", command=self.createsin, width=13).grid(row=4, column=0, pady=10, padx=10)

        Button(self, text="sin num: ", command=self.multi, width=13).grid(row=6, column=0, pady=10, padx=10)

        self.answer=Text(self, width=20, height=5, wrap=WORD)
        self.answer.grid(row=5, column=7, pady=10, padx=10, sticky=E)

    def create(self):
        self.num = Complex(float(self.Re_num.get()),float(self.Im_num.get()))

        self.answ = 'Complex Num Added: ' + '\n' + str(self.num)
        self.calculate()

    def createsin(self):
        self.sinn = int(self.sin.get())

        self.answ = 'Sin Added: ' + '\n' + str(self.sinn)
        self.calculate()

    def multi(self):
        self.solve = self.num.csin(self.sinn)

        self.answ = 'Solve: ' + '\n' + str(self.solve)
        self.calculate()

    def calculate(self):
        self.answer.delete(0.0,END)
        self.answer.insert(0.0,self.answ)

        self.Re_num.delete(0)
        self.Im_num.delete(0)


root=Tk()
root.title("Complex")
root.geometry('700x500')
calc=Comp(root)
root.mainloop()
