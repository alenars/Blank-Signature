 #Mark Gully
 #
 #4/13/2015

import arcpy

arcpy.env.overwriteOutput = True

inFC = arcpy.GetParametAsText (0) #Input Feature Class


#Calculate Areas
arcpy.CalculateAreas_Stats (inFC, "C:\HEL\Gullies.shp")

#Add Field
arcpy.AddField_management("C:\HEL\Gullies.shp", "Acres", "FLOAT")

#Calculate Field

arcpy.CalculateField_management ("C:\HEL\Gullies.shp", "Acres", [Shape_Area]/4046.8564, "VB")