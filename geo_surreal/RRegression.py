#####################################################################################
# Script to sublaunch R from Python and create a linear regression model from
# a file with x and y values in it.
# To run the script, create a "CSV" file with an "X" and a "Y" column with values
# to be used for the linear regression.
#
# Authors: Jim Graham and Andy Larkin
# Date: 4/22/2014
#####################################################################################

# Import the standard libraries
import os.path
import subprocess
import time # bring in the time library so we can "wait" between drawing
import sys

# Import tkinter for a window to display the graph and the file dialog
from Tkinter import *
import tkFileDialog

#Import the Python Image Library to read image file formats like PNG
import Image, ImageTk

# Paths
WorkingFolder="C:/Temp/"
RPath="\"C:/Program Files/R/R-3.1.1/bin/R.exe\""
#RPath="\"C:/Program Files/R/R-2.14.1/bin/R.exe\""

# This is the R Script that will be saved to a file and then executed with a subprocess
RScript="""
########################################################### 
# Setup global variables 
FolderPath = 'E:/Temp/' 

InputFilePath = paste(FolderPath,'Inputs.csv',sep='') 
PlotFilePath = paste(FolderPath,'OutputPlot.gif',sep='') 
ResultsFilePath = paste(FolderPath,'OutputResults.txt',sep='') 

########################################################### 
# Read the data into R 
TheData = read.csv(InputFilePath) 

# Create a linear model for Y, Given X 
LinearModel=lm(TheData$Y~TheData$X) 
 
########################################################### 
# Direct plot output to a png file 
png(PlotFilePath) 

# Draw the points in the plot 
plot(TheData$X,TheData$Y, main=PlotTitle, xlab=XAxisLabel, ylab=YAxisLabel) 

# Add the model output to the plot 
abline(LinearModel) 

# Finalize output to the png file 
dev.off() 
 
########################################################### 
# Direct output of the model results to a text file 
sink(ResultsFilePath, append=FALSE, split=FALSE) 

# Print the model reuslts 
LinearModel 

# Return output to the console  
sink()	  """

try:
	# Setup some dummy variables for when we are debugging this script
	PlotTitle="Title"
	XAxisLabel="X Axis"
	YAxisLabel="Y Axis"
	
	# Get the title and labels from the command line
	TheArguments=sys.argv
	if (len(TheArguments)>1):
		PlotTitle=TheArguments[1]
		XAxisLabel=TheArguments[2]
		YAxisLabel=TheArguments[3]
	
	# Add the title and labels to the start of the R Script
	RScript="PlotTitle <- '"+PlotTitle+"' \n " + \
		"XAxisLabel <- '"+XAxisLabel+"' \n " + \
		"YAxisLabel <- '"+YAxisLabel+"' \n " + \
	        RScript
	
	# Setup Tkinter
	root = Tk()
	root.title("Blobs")
	root.resizable(0, 0)
	
	# Write out the R script to the working folder
	TheFile=open(WorkingFolder+"RScript.R","w")
	TheFile.write(RScript)
	TheFile.close()
	
	# Launch the subprocess to run the R script to do regression
	subprocess.call(RPath+" --no-save <"+WorkingFolder+"RScript.R >"+WorkingFolder+"RConsoleOutput.txt")
	
	# Setup the canvas for the image
	canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0)
	canvas.pack()
	
	# Add the photo to the canvas and wait for the user to click the close box
	image = Image.open(WorkingFolder+"OutputPlot.gif")
	photo = ImageTk.PhotoImage(image)    
	#photo = PhotoImage(file=WorkingFolder+"OutputPlot.gif")
	item = canvas.create_image(10, 10, anchor=NW, image=photo)

	# read the line with the parameters from the output text file
	TheFile=open(WorkingFolder+"OutputResults.txt")
	for i in range(6):
		TheFile.readline()
	TheLine=TheFile.readline()
	TheFile.close()
	
	# parse the line to get the A and B parameters
	TheTokens=TheLine.split()
	B=float(TheTokens[0].strip())
	A=float(TheTokens[1].strip())
	
	# create the equation for the regression to add to the chart
	Equation="y="+format(A)+"x"
	if (B>=0): Equation=Equation+"+"
	Equation=Equation+format(B)
	
	# add a label with the equation
	w = Label(root, text=Equation)
	w.pack()	

	# display the window and wait for the user to close it
	while True:
		root.update_idletasks() # redraw
		root.update() # process events
		time.sleep(.01)

except TclError: # called when the user presses the close button
	pass # to avoid errors when the window is closed

