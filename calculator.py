from tkinter import *
import math

def setnumber(num):
    equation.set(equation.get()+num)

def calculate():
    equation.set(eval(equation.get()))

def sign(x):
    a = equation.get()[-1]
    if a =="*" or a =="/" or a =="-" or a=="+":
        equation.set(equation.get()[:-1] + x)
    else:
        equation.set(equation.get() + x)

def sin_calc():
    value = float(equation.get())
    result = math.sin(math.radians(value))
    equation.set(str(result))

def cos_calc():
    value = float(equation.get())
    result = math.cos(math.radians(value))
    equation.set(str(result))

def sqrt_calc():
    value = float(equation.get())
    result = math.sqrt(value)
    equation.set(str(result))

def square_calc():
    value = float(equation.get())
    result = math.pow(value, 2)
    equation.set(str(result))

root = Tk()

equation = StringVar()


lbl = Label(root,textvariable=equation , font = ("akt",16,"bold"), fg = "#C6ADF0", padx=15 , pady= 10)
lbl.grid(columnspan=4)

dokme1 = Button(root,text= "1", font=("akt",16,"bold"), fg= "#C6ADF0", bg="pink", width=5 , height=2, command=lambda :setnumber("1"))
dokme1.grid(row=1, column=0)
dokme2 = Button(root,text= "2", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda  :setnumber("2"))
dokme2.grid(row=1, column=1)
dokme3 = Button(root,text= "3", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2,command=lambda :setnumber("3"))
dokme3.grid(row=1, column=2)

dokme4 = Button(root,text= "4", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :setnumber("4"))
dokme4.grid(row=2, column=0)
dokme5 = Button(root,text= "5", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :setnumber("5"))
dokme5.grid(row=2, column=1)
dokme6 = Button(root,text= "6", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :setnumber("6"))
dokme6.grid(row=2, column=2)

dokme7 = Button(root,text= "7", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :setnumber("7"))
dokme7.grid(row=3, column=0)
dokme8 = Button(root,text= "8", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :setnumber("8"))
dokme8.grid(row=3, column=1)
dokme9 = Button(root,text= "9", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :setnumber("9"))
dokme9.grid(row=3, column=2)

dokme0 = Button(root,text= "0", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :setnumber("0"))
dokme0.grid(row=4, column=1)

dokmeclear = Button(root,text= "c", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :equation.set(''))
dokmeclear.grid(row=4, column=0)

dokmeeq = Button(root,text= "=", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=calculate)
dokmeeq.grid(row=4, column=2)

dokmeplus = Button(root,text= "+", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :sign("+"))
dokmeplus.grid(row=1, column=3)
dokmemin = Button(root,text= "-", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :sign("-"))
dokmemin.grid(row=2, column=3)
dokmemul = Button(root,text= "*", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :sign("*"))
dokmemul.grid(row=3, column=3)
dokmediv = Button(root,text= "/", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=lambda :sign("/"))
dokmediv.grid(row=4, column=3)

dokmesin = Button(root,text= "sin", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=sin_calc)
dokmesin.grid(row=1, column=4)
dokmecos = Button(root,text= "cos", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=cos_calc)
dokmecos.grid(row=2, column=4)
dokmejazr = Button(root,text= "√ ", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=sqrt_calc)
dokmejazr.grid(row=3, column=4)
dokmesquare = Button(root,text= "x² ", font=("akt",16,"bold"), fg= "#C6ADF0", width=5 , height=2, command=square_calc)
dokmesquare.grid(row=4, column=4)




mainloop()