#CODIGO PARA EL DESARROLLO DE UNA CALCULADORA EN PYTHON
from tkinter import *

root =Tk()

mainFrame = Frame(root)
mainFrame.pack()
root.title("Calculator by Juanma")
# DISPLAY
display = Entry(mainFrame)
display.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
display.config(background="black" ,justify ="right")

# BUTTONS ON ROW2
button7 = Button(mainFrame,text="7",width=3)
button7.grid(row=2,column=1)
button8 = Button(mainFrame,text="8",width=3)
button8.grid(row=2,column=2)
button9 = Button(mainFrame,text="9",width=3)
button9.grid(row=2,column=3)
buttonDivide = Button(mainFrame,text="/",width=3)
buttonDivide.grid(row=2,column=4)

# BUTTONS ON ROW3
button4 = Button(mainFrame,text="4",width=3)
button4.grid(row=3,column=1)
button5 = Button(mainFrame,text="5",width=3)
button5.grid(row=3,column=2)
button6 = Button(mainFrame,text="6",width=3)
button6.grid(row=3,column=3)
buttonMultiply = Button(mainFrame,text="X",width=3)
buttonMultiply.grid(row=3,column=4)

root.mainloop()


