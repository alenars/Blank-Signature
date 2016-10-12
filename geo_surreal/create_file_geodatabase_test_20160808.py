#
#

import arcpy
from arcpy import env

arcpy.env.overwriteOutput = True

#CreateFileGDB_management (out_folder_path, out_name, {out_version})
#arcpy.CreateFileGDB_management (r'E:\geodata\soils\FY2016\test', "testfgb_20160808.gdb","CURRENT")
arcpy.CreateFileGDB_management( , , CURRENT)

#Create Feature Dataset
#CreateFeatureDataset_management (out_dataset_path, out_name, {spatial_reference})
arcpy.CreateFeatureDataset_managment( , , )

#CreateTopology_management (in_dataset, out_name, {in_cluster_tolerance})
arcpy.CreateTopology_managment( , )

#AddFeatureClassToTopology_management (in_topology, in_featureclass, xy_rank, z_rank)
arcpy.AddFeatureClassToTopology_management()

#AddRuleToTopology_management (in_topology, rule_type, in_featureclass, {subtype}, {in_featureclass2}, {subtype2})
arcpy.AddRuleToTopology_management () 