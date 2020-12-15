#CODIGO PARA EL DESARROLLO DE UNA CALCULADORA EN PYTHON
from tkinter import *

root =Tk()

mainFrame = Frame(root)
mainFrame.pack()
root.title("Calculator by Juanma")
#ELEMENTS TO DO THE OPERATIONS
number1 = ""
number2 = ""
operation = ""
result = 0


# DISPLAY
numerDisplay = StringVar()
number1 = StringVar()
number2 = StringVar()
operation = StringVar()


display = Entry(mainFrame, text="0",textvariable=numerDisplay)
display.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
display.config(background="black" ,fg="white", justify ="right")

#----------------PUSH BUTTON
def push_number(num):

    global operation
    if operation != "":
        numerDisplay.set(num)
        operation=""
    else:
        numerDisplay.set( numerDisplay.get() + str(num) )
#----------------PUSH ADD
def push_add(num):
    global operation
    global result
    result+=int(num)
    operation="add"
    numerDisplay.set(result)
#----------------BUTTONS ON ROW2
button7 = Button(mainFrame,text="7",width=3, command=lambda:push_number(7))
button7.grid(row=2,column=1)
button8 = Button(mainFrame,text="8",width=3, command=lambda:push_number(8))
button8.grid(row=2,column=2)
button9 = Button(mainFrame,text="9",width=3, command=lambda:push_number(9))
button9.grid(row=2,column=3)
buttonDivide = Button(mainFrame,text="/",width=3)
buttonDivide.grid(row=2,column=4)

# BUTTONS ON ROW3
button4 = Button(mainFrame,text="4",width=3, command=lambda:push_number(4))
button4.grid(row=3,column=1)
button5 = Button(mainFrame,text="5",width=3, command=lambda:push_number(5))
button5.grid(row=3,column=2)
button6 = Button(mainFrame,text="6",width=3, command=lambda:push_number(6))
button6.grid(row=3,column=3)
buttonMultiply = Button(mainFrame,text="X",width=3)
buttonMultiply.grid(row=3,column=4)

# BUTTONS ON ROW4
button1 = Button(mainFrame,text="1",width=3, command=lambda:push_number(1))
button1.grid(row=4,column=1)
button2 = Button(mainFrame,text="2",width=3, command=lambda:push_number(2))
button2.grid(row=4,column=2)
button3 = Button(mainFrame,text="3",width=3, command=lambda:push_number(3))
button3.grid(row=4,column=3)
buttonMinus = Button(mainFrame,text="-",width=3)
buttonMinus.grid(row=4,column=4)

# BUTTONS ON ROW5
button0 = Button(mainFrame,text="0", width=3, command=lambda :push_number(0))
button0.grid(row=5,column=1)
buttonComma = Button(mainFrame,text=".", width=3, command=lambda :push_number("."))
buttonComma.grid(row=5,column=2)
buttonEqual = Button(mainFrame,text="=", width=3)
buttonEqual .grid(row=5,column=3)
buttonADD = Button(mainFrame,text="+", width=3, command = lambda:push_add(numerDisplay.get()))
buttonADD.grid(row=5,column=4)

root.mainloop()


