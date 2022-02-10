#Create a simple Calculator with a GUI
#This is a work in progress!


#Import GUI library TKinter
import tkinter
from tkinter import *

#Create the window
win=tkinter.Tk()
win.title("SimpleCalc")
win.geometry('600x600')



#---------------------
#Global Variables
#---------------------
calc = 0


#---------------------
#Classes
#---------------------



#add Widgets
but0 = Button(win, text=0,height=1,width=6)
but1 = Button(win, text=1)
but2 = Button(win, text=2)
but3 = Button(win, text=3)
but4 = Button(win, text=4)
but5 = Button(win, text=5)
but6 = Button(win, text=6)
but7 = Button(win, text=7)
but8 = Button(win, text=8)
but9 = Button(win, text=9)
butC = Button(win, text="C", width=1)

viewLabel = Label(win, text=calc)

#Row Values for buttons
r1 = 10
r2 = 40
r3 = 70
r4 = 100

#Column values for buttons
c1 = 5
c2 = 40
c3 = 75


#place Widgets
viewLabel.pack()
butC.place(x=c3,y=r4)
but0.place(x=c1,y=r4)

but1.place(x=c1,y=r3)
but2.place(x=c2,y=r3)
but3.place(x=c3,y=r3)

but4.place(x=c1,y=r2)
but5.place(x=c2,y=r2)
but6.place(x=c3,y=r2)

but7.place(x=c1,y=r1)
but8.place(x=c2,y=r1)
but9.place(x=c3,y=r1)

win.mainloop()
