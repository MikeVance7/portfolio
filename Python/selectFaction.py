#There are a few playable factions on a game I
#play, and I wanted to write a script just to pick one.
#While it would be possible to do this one one or two lines,
#I wanted to try and make one with a GUI.

#Import GUI library TKinter
import tkinter
from tkinter import *
import random

#Create the window
mainWindow=tkinter.Tk()
mainWindow.title("RollRandomFaction")
mainWindow.geometry('600x600')

choice = ""
textColor = "white"
#add Widgets

#label for end result
randLabel = Label(mainWindow, text =choice,fg=textColor)

#Return a random choice from a list of posible factions
def chooseRand():
    factionList = ["Aeon", "UEF", "Cybran"]
    choice = random.choice(factionList)
    randLabel.config(text=choice)
    # randLabel = Label(mainWindow, text=f"Chosen Faction: {random.choice(factionList)}").pack()

RandBtn=Button(mainWindow, text="Get Random Faction",command=chooseRand)


#Place the various elements
RandBtn.pack()
randLabel.pack()




mainWindow.mainloop()