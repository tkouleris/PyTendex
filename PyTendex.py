#!/usr/bin/python
from Tkinter import *
import Tkinter
import tkMessageBox

def calculateTendex():
	#Exception in case the user inserts string and not a number
	try:
        	pointsVar = float(points.get())
		missedFreeThrowsVar = float(missedFreeThrows.get())
		missedShotsVar = float(missedShots.get())
		reboundsVar = float(rebounds.get())
		assistsVar = float(assists.get())
		stealsVar = float(steals.get())
		blocksVar = float(blocks.get())
		turnoversVar = float(turnovers.get())
		minutesPlayedVar = float(minutesPlayed.get())
        except ValueError:
		tkMessageBox.showinfo("You did something wrong","Only use numbers")
	if (pointsVar < 0) or (missedFreeThrowsVar < 0) or (missedShotsVar < 0) or (reboundsVar < 0) or (assistsVar < 0) or (stealsVar < 0) or (blocksVar < 0) or (turnoversVar < 0):
		tkMessageBox.showinfo("Error","Don't use negative")
	elif minutesPlayedVar > 0:
		tendex = (pointsVar - missedFreeThrowsVar - missedShotsVar + reboundsVar + assistsVar + stealsVar + blocksVar - turnoversVar)/minutesPlayedVar
		tkMessageBox.showinfo("Calculated Tendex", tendex)
	else:
		tkMessageBox.showinfo("Your player didn't play", "Your player didn't play")

	#print tendex;

top = Tkinter.Tk()

top.wm_title("Tendex Calculator")
top.geometry("300x300+5+5")
#points variable 
pointsLabel = Label(top,text="Points").grid(row=0,column=0)
points = Entry(top,bd=3)
points.grid(row=0,column=1)
points.insert(0,"0")


#missed free throws variable
missedFreeThrowsLabel = Label(top,text="Missed Free Throws").grid(row=1,column=0)
missedFreeThrows = Entry(top,bd=3)
missedFreeThrows.grid(row=1,column=1)
missedFreeThrows.insert(0,"0")

#missed Shots
missedShotsLabel = Label(top,text="Missed Shots").grid(row=2,column=0)
missedShots = Entry(top,bd=3)
missedShots.grid(row=2,column=1)
missedShots.insert(0,"0")

#Rebounds
reboundsLabel = Label(top,text="Rebounds").grid(row=3,column=0)
rebounds = Entry(top,bd=3)
rebounds.grid(row=3,column=1)
rebounds.insert(0,"0")

#Assists
assistsLabel = Label(top,text="Assists").grid(row=4,column=0)
assists = Entry(top,bd=3)
assists.grid(row=4,column=1)
assists.insert(0,"0")

#Steals
stealsLabel = Label(top,text="Steals").grid(row=5,column=0)
steals = Entry(top,bd=3)
steals.grid(row=5,column=1)
steals.insert(0,"0")

#Blocks
blocksLabel = Label(top,text="Blocks").grid(row=6,column=0)
blocks = Entry(top,bd=3)
blocks.grid(row=6,column=1)
blocks.insert(0,"0")

#Turnovers
turnoversLabel = Label(top,text="Turnovers").grid(row=7,column=0)
turnovers = Entry(top,bd=3)
turnovers.grid(row=7,column=1)
turnovers.insert(0,"0")

#minutes played
minutesPlayedLabel = Label(top, text="Minutes Played").grid(row=8,column=0)
minutesPlayed = Entry(top,bd=3)
minutesPlayed.grid(row=8,column=1)
minutesPlayed.insert(0,"0")


#Button that does the calculation
w = Tkinter.Button(top, text = "Calculate", command = calculateTendex)
w.grid(row=9,column=0)

top.mainloop()
