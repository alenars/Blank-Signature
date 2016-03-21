#####################################################################################
# Script to sublaunch a Python script from an ArcGIS tool.
# The tool will create a linear regression graph in ArcGIS using a shapefile.
# To test the tool:
# - Create a folder at "C:/Temp" for a working folder
# - Save the associated "California_Climate" shapefile into the folder
# - Make sure the paths below point to the appropriate versions of Python 
#   and the associated Python script to call R.
#
# Authors: Jim Graham and Andy Larkin
# Date: 4/22/2014
#####################################################################################

#####################################################################################
# Import standard packages
import subprocess

# Add a path to the reusable code
import sys  
sys.path.append("E:/Documents/GIS/python/ars_scripts")
import shapefile

#####################################################################################
# Setup the paths
WorkingFolder="E:/Temp/"
PathToScripts="E:/Documents/GIS/python/ars_scripts"
PathToPython="C:/Python27/ArcGISx6410.2/python.exe"
PathToPython="C:/Python27/python.exe"

# Variable to switch when we are running as a tool in ArcGIS
RunningAsATool=False

# Setup the default parameters (when running without being a tool)
TheShapefile=WorkingFolder+"CA_Redwood_MaxHeight.shp"
Field1="Height"
Field2="AnnualPrec"

#####################################################################################
# Get the parameters from the ArcGIS tool

if (RunningAsATool):
   import arcpy
   # The the user (and us!) know we are running)
   arcpy.AddMessage("Running Tools")
   
   # Get the parameters from the tool
   TheShapefile=arcpy.GetParameterAsText(0)
   Field1=arcpy.GetParameterAsText(1)
   Field2=arcpy.GetParameterAsText(2)
   
   # Print the parameters back to the tool for debugging
   arcpy.AddMessage("TheShapefile="+TheShapefile)
   arcpy.AddMessage("Field1="+Field1)
   arcpy.AddMessage("Field2="+Field2)
   
#####################################################################################
# Write out two of the attributes from the shapefile into an "Inputs" file for R

# Open the file for the Input data to R and write out the header
TheFile=open(WorkingFolder+"Inputs.csv","w")
TheFile.write("X,Y\n")

# Open the shapefile 
TheShapefile=shapefile.Reader(TheShapefile)

# get the list of fields (attribute column headings) from the file
TheFields=TheShapefile.fields

# find the index to each of the selected fields
FieldIndex=0
for TheField in TheFields:
   if (TheField[0]==Field1): FieldIndex1=FieldIndex
   if (TheField[0]==Field2): FieldIndex2=FieldIndex
   FieldIndex+=1

# get the records (attribute rows) from the shapefiles dbf file
TheRecords=TheShapefile.records()

# Loop through each row in the attributes    
for TheRecord in TheRecords:
    Value1=TheRecord[FieldIndex1]
    Value2=TheRecord[FieldIndex2]
    TheFile.write(format(Value1)+","+format(Value2)+"\n")

# Close the file
TheFile.close()
   
#####################################################################################
# Call the R script to create the chart and display it in a window

# Setup the labels for the title and axis
Title="Linear Regression"
XAxisLabel=Field1
YAxisLabel=Field2

# Create a parameter string for the command
Parameters=" \""+Title+"\" \""+XAxisLabel+"\" \""+YAxisLabel+"\""

# Create the command that will be sent to python to run R
Command="\""+PathToPython+"\" "+PathToScripts+"RRegression.py"+Parameters+ " >"+WorkingFolder+"PythonConsoleOutput.txt"

# Show the command for debugging
if (RunningAsATool): arcpy.AddMessage("Command="+Command)

# Open the process and wait for it to finish
TheProcess=subprocess.Popen(Command)
return_code = TheProcess.wait()
   
#####################################################################################
# Let the user know we are done

# Let the user know that this script finished successfully
if (RunningAsATool): arcpy.AddMessage("Done")
