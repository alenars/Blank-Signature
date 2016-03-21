#Project
#11/23/2015
#Project_management (in_dataset, out_dataset, out_coor_system, {transform_method}, {in_coor_system})

import arcpy
arcpy.env.overwriteOutput = True

inFC = arcpy.GetParameterAsText (0)
outFC = arcpy.GetParameterAsText (1)
out_coor_system = arcpy.GetParameterAsText (2)

Project_management (inFC, outFC, out_coor_system)

