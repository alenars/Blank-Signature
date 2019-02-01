#A. Stephens
#2/1/2016
#Update 2/1/2019

import arcpy
import os

arcpy.env.overwriteOutput = True

#Output Folder
outputFolder = arcpy.GetParameterAsText(0)
#Location where SSURGO datassets reside
#sdmLibrary = arcpy.GetParameterAsText(1)
#SSURGO Datasets import county boundaries
#surveyList = arcpy.GetParameter(2)
#Import 1st Soil Feature Class
inFC = arcpy.GetParameterAsText (1)
#Import 2nd Soil Feature Class
inFC2 = arcpy.GetParameterAsText (2)

arcpy.env.workspace = out_folder 

#Intersect
#Intersect_analysis (in_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})
arcpy.Intersect_analysis ('inFC, inFC2', outputFolder+'//'+ 'inFC_INT', ALL, LINE)

#Select Layer By Attribute
arcpy.SelectLayerByAttribute_management ('inFC_INT', "NEW_SELECTION", "MUSYM"<> "MUSYM_1")

#Feature To Point 
arcpy.FeatureToPoint_management ('inFC_INT', 'inFC_INT_pt', "INSIDE")

#Spatial Joins 
#SpatialJoin_analysis (target_features, join_features, out_feature_class, {join_operation}, {join_type}, {field_mapping},
#{match_option}, {search_radius}, {distance_field_name})
arcpy.SpatialJoin_analysis('inFC, inFC2', 'out_sj', "JOIN_ONE_TO_ONE"", "KEEP_ALL", "SHARE_A_LINE_SEGMENT_WITH"")


#Make Feature Layer
#MakeFeatureLayer_management (in_features, out_layer, {where_clause}, {workspace}, {field_info})
arcpy.MakeFeatureLayer_management ('inFC', )

#Select Layer By Attribute
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})

#Make Feature Layer
#MakeFeatureLayer_management (in_features, out_layer, {where_clause}, {workspace}, {field_info})

#Select Layer By Attribute
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})

#Select Layer By Attribute
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})

# Copy Features
#CopyFeatures_management (in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})


#Spatial Joins
#SpatialJoin_analysis (target_features, join_features, out_feature_class, {join_operation}, {join_type}, {field_mapping},
#{match_option}, {search_radius}, {distance_field_name})

#Make Feature Layer
#MakeFeatureLayer_management (in_features, out_layer, {where_clause}, {workspace}, {field_info})

#Select Layer By Attributes
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})

#Make FEature Layer
#MakeFeatureLayer_management (in_features, out_layer, {where_clause}, {workspace}, {field_info})

#Select Layer By Attribute
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})

#Select Layer By Attribute
#SelectLayerByAttribute_management (in_layer_or_view, {selection_type}, {where_clause})

#Copy Features
#CopyFeatures_management (in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

#Merge
#Merge_management (inputs, output, {field_mappings})

#Table to Excel
#TableToExcel_conversion (Input_Table, Output_Excel_File, {Use_field_alias_as_column_header}, {Use_domain_and_subtype_description})
