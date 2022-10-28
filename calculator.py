from tkinter import *

window = Tk()

window.title("Calculator")
window.resizable(0, 0)
window.attributes('-toolwindow', True)

global equal_flag
equal_flag = 0

global operation_lock
operation_lock = 0

def add():
    global equal_flag
    global operation_lock
    if operation_lock == 1:
        return
    if equal_flag == 1:
        clear()
        equal_flag = 0
        operation_lock = 0
    if txt.get().count('+') == 1:
        return
    if txt.get() == "":
        return
    txt.insert("end", "+")
    operation_lock = 1

def subtract():
    global equal_flag
    global operation_lock
    if operation_lock == 1:
        return
    if equal_flag == 1:
        clear()
        equal_flag = 0
        operation_lock = 0
    if txt.get().count('-') == 1:
        return
    if txt.get() == "":
        return
    txt.insert("end", "-")
    operation_lock = 1

def multiply():
    global equal_flag
    global operation_lock
    if operation_lock == 1:
        return
    if equal_flag == 1:
        clear()
        equal_flag = 0
        operation_lock = 0
    if txt.get().count('x') == 1:
        return
    if txt.get() == "":
        return
    txt.insert("end", "x")
    operation_lock = 1

def divide():
    global equal_flag
    global operation_lock
    if operation_lock == 1:
        return
    if equal_flag == 1:
        clear()
        equal_flag = 0
        operation_lock == 0
    if txt.get().count('/') == 1:
        return
    if txt.get() == "":
        return
    txt.insert("end", "/") 
    operation_lock == 1

def clear():
    txt.delete(0, last=len(txt.get()))
    global operation_lock
    operation_lock = 0

def equal():
    i = 0
    global equal_flag
    for i, value in enumerate(txt.get()):
        if value.count('+') == 1:
            firstNum = int(txt.get()[0:i])
            secondNum = int(txt.get()[i+1:len(txt.get())])
            clear()
            txt.insert("end", firstNum + secondNum)
            global equal_flag
            equal_flag = 1
            break
        if value.count('-') == 1:
            firstNum = int(txt.get()[0:i])
            secondNum = int(txt.get()[i+1:len(txt.get())])
            clear()
            txt.insert("end", firstNum - secondNum)
            equal_flag = 1
            break
        if value.count('x') == 1:
            firstNum = int(txt.get()[0:i])
            secondNum = int(txt.get()[i+1:len(txt.get())])
            clear()
            txt.insert("end", firstNum * secondNum)
            equal_flag = 1
            break
        if value.count('/') == 1:
            firstNum = int(txt.get()[0:i])
            secondNum = int(txt.get()[i+1:len(txt.get())])
            if secondNum == 0:
                clear()
                txt.insert("end", "Error")
                equal_flag = 1
                return
            clear()
            txt.insert("end", firstNum / secondNum)
            equal_flag = 1
            break

def num_seven():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "7")

def num_eight():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "8")

def num_nine():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "9")

def num_four():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "4")

def num_five():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "5")

def num_six():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "6")

def num_one():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "1")

def num_two():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "2")

def num_three():
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "3")

def num_zero():
    if txt.get() == "":
        return
    global equal_flag
    if equal_flag == 1:
        clear()
        equal_flag = 0
    txt.insert("end", "0")

plus_btn = Button(window, text="+",
    fg = "black", command=add, height=2, width=5)
plus_btn.grid(column=0, row=1, sticky="e")

clear_btn = Button(window, text="C",
    fg = "black", command=clear, height=2, width=5)
clear_btn.grid(column=2, row=1, sticky="w")

equal_btn = Button(window, text="=",
    fg = "black", command=equal, height=2, width=5)
equal_btn.grid(column=2, row=7, sticky="w")

subtract_btn = Button(window, text="-",
    fg = "black", command=subtract, height=2, width=5)
subtract_btn.grid(column=1, row=1)

multiply_btn = Button(window, text="x",
    fg = "black", command=multiply, height=2, width=5)
multiply_btn.grid(column=0, row=7, sticky="e")

divide_btn = Button(window, text="/",
    fg = "black", command=divide, height=2, width=5)
divide_btn.grid(column=1, row=7)

#7
seven_btn = Button(window, text="7",
    fg = "black", command=num_seven, height=2, width=5)
seven_btn.grid(column=0, row=3, sticky="e")

#8
eight_btn = Button(window, text="8",
    fg = "black", command=num_eight, height=2, width=5)
eight_btn.grid(column=1, row=3)

#9
nine_btn = Button(window, text="9",
    fg = "black", command=num_nine, height=2, width=5)
nine_btn.grid(column=2, row=3, sticky="w")

#4
four_btn = Button(window, text="4",
    fg = "black", command=num_four, height=2, width=5)
four_btn.grid(column=0, row=4, sticky="e")

#5
five_btn = Button(window, text="5",
    fg = "black", command=num_five, height=2, width=5)
five_btn.grid(column=1, row=4)

#6
six_btn = Button(window, text="6",
    fg = "black", command=num_six, height=2, width=5)
six_btn.grid(column=2, row=4, sticky="w")

#1
one_btn = Button(window, text="1",
    fg = "black", command=num_one, height=2, width=5)
one_btn.grid(column=0, row=5, sticky="e")

#2
two_btn = Button(window, text="2",
    fg = "black", command=num_two, height=2, width=5)
two_btn.grid(column=1, row=5)

#3
three_btn = Button(window, text="3",
    fg = "black", command=num_three, height=2, width=5)
three_btn.grid(column=2, row=5, sticky="w")

#0
zero_btn = Button(window, text="0",
    fg = "black", command=num_zero, height=2, width=5)
zero_btn.grid(column=1, row=6)
#zero_btn.place(relx=.6, rely=.6, anchor=CENTER)

txt = Entry(window, width=20)
#txt.place(relx=.5, rely=.5, anchor=CENTER)
txt.grid(column=0, row=0, columnspan=3, padx = 20, pady = 20)

window.mainloop()