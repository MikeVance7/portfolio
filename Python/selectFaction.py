#There are a few playable factions on a game I
#play, and I wanted to write a script just to pick one.
#While it would be possible to do this one one or two lines,
#I wanted to try and make one with a GUI.

#Import GUI library TKinter
from json.tool import main
import tkinter
from tkinter import *
import random

#Create the window
mainWindow=tkinter.Tk()
mainWindow.title("RollRandomFaction")
mainWindow.geometry('600x600')

#Create global values for labels and such.
choice = "Click below"
textColor = "black"

#Create class for factions
class Faction:
    def __init__(self,name,color):
        self.name = name
        self.color = color



class Count:
    def __init__(self):
        self.c = 0

    def addCount(self):
        self.c = self.c + 1
    

#Create the factions
uef = Faction("UEF", "blue")
aeon = Faction("Aeon","green")
cybran = Faction("Cybran","red")
seraphim = Faction("Seraphim","yellow")

Counter = Count()

#add Widgets

#label for end result
randLabel = Label(mainWindow, text =choice,fg=textColor)
rollLabel = Label(mainWindow, text =Counter.c)


#Return a random choice from a list of posible factions
def chooseRand():
    factionList = [uef,aeon,cybran,seraphim]
    choice = random.choice(factionList)
    randLabel.config(text=choice.name)
    randLabel.config(fg=choice.color)
    Counter.addCount()
    rollLabel.config(text=Counter.c)
    
    

RandBtn=Button(mainWindow, text="Get Random Faction",command=chooseRand)


#Place the various elements
RandBtn.place(x=5,y=30)
randLabel.place(x=5,y=1)
rollLabel.pack()




mainWindow.mainloop()