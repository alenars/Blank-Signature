

#Compare Data by joining MUAGGATT table and Rename Feature Classes
#03/23/2015

import arcpy

arcpy.env.overwriteOutput = True

inuFC = arcpy.GetParameterAsText (0) #input UPDATE Layer
inutable = arcpy.GetParameterAsText (1) #input UPDATE MUAGGATT table from access database
insFC = arcpy.GetParameterAsText (2) #Input SSURGO Layer
instable = arcpy.GetParameterAsText (3) #Input SSURGO MUAGGATT from access database
inFC = arcpy.GetParameterAsText (4) #Workspace
#Select Coordiante System
#Input Compare Name

#Join muname Field Update

arcpy.JoinField_management(inuFC, "mukey", inutable, "mukey", ["muname"])

#Join muname Field SSURGO

arcpy.JoinField_management(insFC, "mukey", instable, "mukey", ["muname"])

#Union

#Make Feature Layer

#Copy Features



