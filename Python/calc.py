#Create a simple Calculator with a GUI
#This is a work in progress!


#Import GUI library TKinter
import tkinter
from tkinter import *

#Create the window
win=tkinter.Tk()
win.title("SimpleCalc")
win.geometry('600x600')

#add Widgets
testBtn=Button(win, text="TestButton", width=10,height=10)
testBtn.place(x=1,y=1)


win.mainloop()

