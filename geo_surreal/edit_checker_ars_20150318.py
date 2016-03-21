
#works if the sortFC is in the TOC
#3/18/2015

import arcpy
import os

arcpy.env.overwriteOutput = True

inFC = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)

arcpy.env.workspace = workspace

#Dissolve
arcpy.Dissolve_management (inFC, "disFC",["AREASYMBOL", "MUSYM", "ORIG_MUSYM", "Creator_Field", "Creation_Date_Field", "Editor_Field", "Last_Edit_Date_Field"],
                           "","MULTI_PART", "DISSOLVE_LINES") 

#Sort ~ 
arcpy.Sort_management ("disFC", "sortFC", [["Creator_Field", "DESCENDING"], ["Creation_Date_Field", "ASCENDING"], ["Editor_Field", "DESCENDING"], ["Last_Edit_Date_Field", "ASCENDING"],
                                           ["AREASYMBOL","ASCENDING"],["MUSYM","ASCENDING"], ["ORIG_MUSYM", "ASCENDING"]]  )

#Add Field
arcpy.AddField_management("sortFC", "EDITS", "TEXT", "20" )
#Selection
arcpy.SelectLayerByAttribute_management ("sortFC", "NEW_SELECTION", " MUSYM <> ORIG_MUSYM ")

#Calculate in editing session
with arcpy.da.Editor(workspace) as edit:arcpy.CalculateField_management("sortFC", "EDITS", ' "ATTRIBUTE" ')

#Selection
arcpy.SelectLayerByAttribute_management ("sortFC", "NEW_SELECTION", " Creator_Field LIKE '%' ")

#Calculate in editing session
with arcpy.da.Editor(workspace) as edit:arcpy.CalculateField_management("sortFC", "EDITS", ' "SPATIAL" ')
#Clear Selection
arcpy.SelectLayerByAttribute_management ("sortFC", "CLEAR_SELECTION")

#Clear Selection
arcpy.SelectLayerByAttribute_management ("sortFC", "CLEAR_SELECTION")

#Export the selected features to a new feature class
arcpy.CopyFeatures_management("sortFC", workspace+'\\'+"Edit_Checks")

#try:
    #Selection
    #arcpy.SelectLayerByAttribute_management ("sortFC", "NEW_SELECTION", "Creator_Field LIKE '%' OR Editor_Field LIKE '%' OR MUSYM <> ORIG_MUSYM ")

    #Add Field
    #arcpy.AddField_management("sortFC", "EDITS", "TEXT", "20" )

    #Selection
    #arcpy.SelectLayerByAttribute_management ("sortFC", "REMOVE_FROM_SELECTION", "MUSYM <> ORIG_MUSYM ")
    
    #Calculate in editing session
    #with arcpy.da.Editor(workspace) as edit:arcpy.CalculateField_management("sortFC", "EDITS", ' "SPATIAL" ')
    
    #Select by Layer
    #arcpy.SelectLayerByAttribute_management ("sortFC", "SWITCH_SELECTION", "MUSYM <> ORIG_MUSYM ")
    
    #Calculate in editing session
    #with arcpy.da.Editor(workspace) as edit:arcpy.CalculateField_management("sortFC", "EDITS", ' "ATTRIBUTE" ')
    
    #Clear Selection
    #arcpy.SelectLayerByAttribute_management ("sortFC", "CLEAR_SELECTION")

    #Export the selected features to a new feature class
    #arcpy.CopyFeatures_management("sortFC", workspace+'\\'+"Edit_Checks")

    


#except arcpy.ExecuteError:
    #print (arcpy.GetMessages (2))

#Delete Features
arcpy.Delete_management("disFC")
#arcpy.Delete_management("sortFC")
    