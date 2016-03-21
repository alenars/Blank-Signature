#A. Stephens
#2/1/2016

import arcpy

#Output Folder
outputFolder = arcpy.GetParameterAsText(0)
#Location where SSURGO datassets reside
sdmLibrary = arcpy.GetParameterAsText(1)
#SSURGO Datasets import county boundaries
surveyList = arcpy.GetParameter(2)

#Spatial Joins 
#SpatialJoin_analysis (target_features, join_features, out_feature_class, {join_operation}, {join_type}, {field_mapping},
#{match_option}, {search_radius}, {distance_field_name})

#Make Feature Layer
#MakeFeatureLayer_management (in_features, out_layer, {where_clause}, {workspace}, {field_info})

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

#Intersect
#Intersect_analysis (in_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})

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