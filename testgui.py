from tkinter import *
class Calcul(Frame):
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


    def addition(self):
        try:
            self.answ=int(self.num_1.get())+int(self.num_2.get())
            self.answ=str(self.num_1.get())+"+"+str(self.num_2.get())+"="+str(self.answ)
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()

    def substraction(self):
        try:
            self.answ=int(self.num_1.get())-int(self.num_2.get())
            self.answ=str(self.num_1.get())+"-"+str(self.num_2.get())+"="+str(self.answ)
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()

    def multiplication(self):
        try:
            self.answ=int(self.num_1.get())*int(self.num_2.get())
            self.answ=str(self.num_1.get())+"*"+str(self.num_2.get())+"="+str(self.answ)
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()

    def division(self):
        try:
            self.answ=int(self.num_1.get())/int(self.num_2.get())
            self.answ=str(self.num_1.get())+"/"+str(self.num_2.get())+"="+str(self.answ)
        except ZeroDivisionError:
            self.answ="Деление на ноль невозможно"
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()

    def calculate(self):
        self.answer.delete(0.0,END)
        self.answer.insert(0.0,self.answ)
        self.num_1.delete(0, END)
        self.num_2.delete(0, END)

root=Tk()
root.title("Калькулятор")
root.geometry('500x500')
calc=Calcul(root)
root.mainloop()
