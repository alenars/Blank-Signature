#Attribute Conversion Test
#A. Stephens
#11/20/2014

import arcpy
import os

arcpy.env.overwriteOutput = True

in_table = arcpy.GetParameterAsText (0)
inFC = arcpy.GetParameterAsText (1)
workspace = arcpy.GetParameterAsText (2)


#Select Feature
#arcpy.SelectLayerByAttribute_management (inFC, "NEW_SELECTION", " MUSYM = 'W' ")

#value_table = in_table

#value_table.loadFromString(arcpy.GetParameterAsText (0))

#with arcpy.da.Editor(workspace) as edit:arcpy.CalculateField_management(inFC, "ACRES", '!Shape.area@ACRES!', "PYTHON_9.3", )

fields = ['Old', 'MUSYM']
field1 = ['Old']
field2 = ['MUSYM']
#ufield = ['MUSYM']

edit = arcpy.da.Editor(workspace)

edit.startEditing(False,True)

edit.startOperation()

with arcpy.da.UpdateCursor(inFC, (field1) as ucur:
                           ucur.updateRow(field2)

#arcpy.da.SearchCursor(in_table, fields)

#rows = arcpy.da.UpdateCursor (inFC, ufield)

#cursor = arcpy.UpdateCursor (inFC)
#row = cursor.next ()

#while row:
 #       row.setValue(field2, row.getValue(field1))
  #      cursor.updateRow(row)
   #     row = cursor.next()

edit.stopOperation()

edit.stopEditing(True)

#row=inFC.next()

#with arcpy.da.UpdateCursor (inFC, ufield) as cursor:
 #   for rows in cursor:
        #for row in cursor:
  #      rows.setValue(field1, ufield, field2)
   #     cursor.updateRow(ufield)
        #rows = updaterow(ufield)
#row = inFC.next()