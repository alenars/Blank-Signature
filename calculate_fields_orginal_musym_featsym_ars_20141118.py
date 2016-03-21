#Calculate Fields
#A. Stephens
#11/18/2014

import arcpy

arcpy.env.overwriteOutput = True

inFC = arcpy.GetParameterAsText (0) #Input polygon Feature Class
sfpinFC = arcpy.GetParameterAsText (1) #Input special feature point feature class
sflinFC = arcpy.GetParameterAsText (2) # Input special feature line feature class

arcpy.CalculateField_managment(inFC, "ORIG_MUSYM", 'ORIG_MUSYM' = '!MUSYM!', "PYTHON_9.3" )

arcpy.CalculateField_managment(sfpinFC, "ORIG_FEATSYM",'ORIG_FEATSYM' = '!FEATSYM!', "PYTHON_9.3" )

arcpy.CalculateField_managment(sflinFC, "ORIG_FEATSYM",'ORIG_FEATSYM' = '!FEATSYM!',"PYTHON_9.3" )