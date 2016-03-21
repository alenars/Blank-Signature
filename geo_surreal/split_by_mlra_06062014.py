#Split Soils by MLRA
#6/6/2014

import arcpy
arcpy.env.overwriteOutput = True
inFC = arcpy.GetParameterAsText(0)
split = arcpy.GetParameterAsText (1)
splitfield = arcpy.GetParameterAsText (2)
outworkspace = arcpy.GetParameterAsText(3)

#Split Tool

arcpy.Split_analysis(inFC, split, splitfield, outworkspace)
