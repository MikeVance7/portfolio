#Create a simple Calculator with a GUI

#Import GUI library TKinter
import tkinter
from tkinter import *


win=tkinter.Tk()
win.title("SimpleCalc")
win.geometry('600x600')
testBtn=Button(win, text="TestButton", width=10,height=10)
testBtn.place(x=1,y=1)


win.mainloop()
