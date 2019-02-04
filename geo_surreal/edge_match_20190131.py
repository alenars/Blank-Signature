#Edge Match
#A. Stephens
#1/31/2019


import arcpy
import os

arcpy.env.overwriteOutput = True

#Output Folder
out_folder = arcpy.GetParameterAsText (0)
#Input Feature Class
inFC = arcpy.GetParameterAsText (1)
#Input Feature Class
inFC1 = arcpy.GetParameterAsText (2)


inFC2 = [inFC, inFC1]

inFC3 = out_folder + 'sjfla_copy'

# sjf2a_copy

arcpy.env.workspace = out_folder

#Intersect
arcpy.Intersect_analysis (inFC2, out_folder +'\\' +'inFC2_INT', "ALL", "", "LINE")

#Select Layer By Attribute
#arcpy.SelectLayerByAttribute_management (out_folder + '\\' +'inFC2_INT', "NEW_SELECTION", ' "MUSYM"<> "MUSYM_1" ')
arcpy.SelectLayerByAttribute_management("inFC2_INT","NEW_SELECTION",  ' "MUSYM" <> "MUSYM_1" ' )

#Feature To Point 
#arcpy.FeatureToPoint_management (out_folder + '\\' +'inFC2_INT', 'inFC_INT_pt', "INSIDE")
arcpy.FeatureToPoint_management("inFC2_INT", "inFC_INT_pt", "INSIDE")


#Spatial Join
#arcpy.SpatialJoin_analysis("IN023", "IN159", "spatial_join1", "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "SHARE_A_LINE_SEGMENT_WITH", "", "")
arcpy.SpatialJoin_analysis (inFC, inFC1, out_folder + '\\' +'spatial_join1', "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "SHARE_A_LINE_SEGMENT_WITH", "", "")

#Make Feature Layer
#arcpy.MakeFeatureLayer_management (out_folder + 'spatial_join1', out_folder +'sj_f1', "", "", "")
#arcpy.MakeFeatureLayer_management("spatial_join1", "sj_f1", ' "MUSYM" <> "MUSYM_1" ', r'E:\geodata\project_data\11IND\FY2019\test')
arcpy.MakeFeatureLayer_management (out_folder + '\\' +'spatial_join1.shp', out_folder + '\\' +'sj_f1', '"MUSYM"<>"MUSYM_1"', out_folder )

#Select Layer By Attributes
#arcpy.SelectLayerByAttribute_management (out_folder + '\\' +'sj_f1', "NEW_SELECTION", '"MUSYM"<>"MUSYM_1"')

#Make Feature Layer
#arcpy.MakeFeatureLayer_management( "sj_f1", "sj_f1a", " 'MUSYM_1'<> '' ", r'E:\geodata\project_data\11IND\FY2019\test')
arcpy.MakeFeatureLayer_management (out_folder + '\\' +'sj_f1', out_folder +'\\' + 'sj_f1a', ' "MUSYM_1"<> '' ', out_folder)

#Save Layer File
#arcpy.SaveToLayerFile_management (out_folder +'\\' + 'sj_f1a', out_folder +'\\' + 'sj_f1a.lyr', "")

#Select Layer By Attributes
#arcpy.SelectLayerByAttribute_management (out_folder + '\\' + 'sj_f1a', 'NEW_SELECTION', '"MUSYM_1"= ''')

#Select Layer By Attributes
#arcpy.SelectLayerByAttribute_management (out_folder + '\\' +'sj_f1a', "SWITCH_SELECTION", "")

#Copy Features
arcpy.CopyFeatures_management(out_folder + '\\' +'sj_f1a', out_folder +'\\' +'sjf1a_copy')

#Spatial Join
arcpy.SpatialJoin_analysis (inFC1, inFC, out_folder +'\\' + 'outspatial_join2', "JOIN_ONE_TO_ONE", "KEEP_ALL", "","SHARE_A_LINE_SEGMENT_WITH", "", "")

#Make Feature Layer
arcpy.MakeFeatureLayer_management (spatial_join2, out_folder +'\\' + 'sj_f2', "", "", "")

#Select Layer By Attributes
arcpy.SelectLayerByAttribute_management (sj_f2, "NEW_SELECTION", '"MUSYM"<>"MUSYM_1"')

#Make Feature Layer
arcpy.MakeFeatureLayer_management (sj_f2, out_folder +'\\' + 'sj_f2a', "", "", "")

#Select Layer By Attributes
arcpy.SelectLayerByAttribute_management (sj_f2a, "NEW_SELECTION", '"MUSYM_1"=" "')

#Select Layer By Attributes
arcpy.SelectLayerByAttribute_management (sj_f2a, "SWITCH_SELECTION", "")

#Copy Features
arcpy.CopyFeatures_management(sj_f2a, out_folder +'\\' + 'sjf2a_copy')


#Merge
arcpy.Merge_management (inFC3, out_folder + '\\' +'EM_Merge', "")

#print(arcpy.GetMessages((Done))
