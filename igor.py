
# coding: utf-8

# In[90]:


from math import cos, sin, sqrt, atan2
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


# In[115]:


#всякие проверки
print('(1+i)^5 = ', Complex(1,1)**5)
si = Complex(3.1415).csin(6)
print('sin(pi) =' ,si)
si = Complex(1.57085).csin(6)
print('sin(pi/2) =' ,si)
