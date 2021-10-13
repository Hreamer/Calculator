from tkinter import *
import random

def but_1_():
    global math_sol
    math_sol+="1"
    Math.config(text=math_sol)

def but_2_():
    global math_sol
    math_sol+="2"
    Math.config(text=math_sol)

def but_3_():
    global math_sol
    math_sol+="3"
    Math.config(text=math_sol)

def but_4_():
    global math_sol
    math_sol+="4"
    Math.config(text=math_sol)

def but_5_():
    global math_sol
    global math_equals
    math_sol+="5"
    Math.config(text=math_sol)

def but_6_():
    global math_sol
    math_sol+="6"
    Math.config(text=math_sol)

def but_7_():
    global math_sol
    math_sol+="7"
    Math.config(text=math_sol)

def but_8_():
    global math_sol
    math_sol+="8"
    Math.config(text=math_sol)

def but_9_():
    global math_sol
    math_sol+="9"
    Math.config(text=math_sol)

def but_0_():
    global math_sol
    math_sol+="0"
    Math.config(text=math_sol)

def minus_():
    global math_sol
    math_sol+="-"
    Math.config(text=math_sol)

def plus_():
    global math_sol
    math_sol+="+"
    Math.config(text=math_sol)

def equals_():
    global math_sol
    Math.config(text="="+str(eval(math_sol)))

def clear_():
    global math_sol
    math_sol=""
    Math.config(text="")

def Division_():
    global math_sol
    math_sol+="/"
    Math.config(text=math_sol)

def Multiplication_():
    global math_sol
    math_sol+="*"
    Math.config(text=math_sol)

def right_paren():
    global math_sol
    math_sol+="("
    Math.config(text=math_sol)

def left_paren():
    global math_sol
    math_sol+=")"
    Math.config(text=math_sol)

math_sol=""

root=Tk()
root.title("Calculator")
    
Math=Label(root,text="",width=20,bg="light blue")
Math.grid(row=0,column=1)

but_1=Button(root,text="1",width=5,command=but_1_)
but_1.grid(row=1,column=0)

but_2=Button(root,text="2",width=5,command=but_2_)
but_2.grid(row=1,column=1)

but_3=Button(root,text="3",width=5,command=but_3_)
but_3.grid(row=1,column=2)

but_4=Button(root,text="4",width=5,command=but_4_)
but_4.grid(row=2,column=0)

but_5=Button(root,text="5",width=5,command=but_5_)
but_5.grid(row=2,column=1)

but_6=Button(root,text="6",width=5,command=but_6_)
but_6.grid(row=2,column=2)

but_7=Button(root,text="7",width=5,command=but_7_)
but_7.grid(row=3,column=0)

but_8=Button(root,text="8",width=5,command=but_8_)
but_8.grid(row=3,column=1)

but_9=Button(root,text="9",width=5,command=but_9_)
but_9.grid(row=3,column=2)

but_0=Button(root,text="0",width=5,command=but_0_)
but_0.grid(row=4,column=1)

minus=Button(root,text="-",width=5,command=minus_)
minus.grid(row=4,column=0)

plus=Button(root,text="+",width=5,command=plus_)
plus.grid(row=4,column=2)

equals=Button(root,text="=",width=5,command=equals_)
equals.grid(row=5,column=1)

clear=Button(root,text="clear",width=15,command=clear_)
clear.grid(row=6,column=1)

Division=Button(root,text="÷",width=5,command=Division_)
Division.grid(row=5,column=2)

Multiplication=Button(root,text="×",width=5,command=Multiplication_)
Multiplication.grid(row=5,column=0)

left_Paren=Button(root,text=")",command=left_paren)
left_Paren.grid(row=6,column=0)

right_Paren=Button(root,text="(",command=right_paren)
right_Paren.grid(row=6,column=2)

root.mainloop()