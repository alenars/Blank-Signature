#Calculate acres after Adding a field Column
#6/6/2014
#Alena Stephens

import arcpy
arcpy.env.overwriteOutput = True

inFC = arcpy.GetParameterAsText (0)

#Add Field

arcpy.AddField_management(inFC, "ACRES", "DOUBLE")

#Calculate Field

arcpy.CalculateField_management(inFC, "ACRES", '!Shape.area@ACRES!', "PYTHON_9.3")

#Add Field

arcpy.AddField_management(inFC, "Percent", "SHORT")


print "Script Completed"

