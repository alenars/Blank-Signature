#MLRA Check Topology
#09/23/2016
#Alena Stephens
#works best if the spatial data resides in TOC

import arcpy
import os

arcpy.env.overwriteOutput = True

out_folder = arcpy.GetParameterAsText (0)#Output Folder, Workspace, Required
inprname = arcpy.GetParameterAsText (1)#Input Project Name, String, Required
incoord = arcpy.GetParameterAsText (2)#Input Coordinate System, Spatial Reference
inFC = arcpy.GetParameterAsText (3) #Input soil polygons, Feature Layer or Raster Cataglo Layer or Mosaic Layer, Required

arcpy.env.workspace = out_folder

inprname = inprname.replace ('-',' ') #replace hyphens and space with underscores
inprname = inprname.replace (',',' ')
inprname =inprname.replace ('  ','_')
inprname =inprname.replace ('__','_')
inprname =inprname.replace (' ','_')

#Input Project Name
prjname = inprname+'_'

#Input File Geodatabase Name
fdname = out_folder+'\\'+inprname+'.gdb'+'\\'+ prjname+'FD'

#Input Topology Name
inprname_topology = out_folder+'\\'+inprname+'.gdb'+ '\\'+ prjname+'FD'+ '\\' + prjname+'topology'

#Create File Geodatabase
arcpy.CreateFileGDB_management(out_folder, inprname, "10.0")

#Create Feature Dataset
arcpy.CreateFeatureDataset_management(out_folder+'\\'+inprname+'.gdb', prjname+'FD', incoord)

#Feature Class to Feature Class ~ Soils
arcpy.FeatureClassToFeatureClass_conversion(inFC, fdname, prjname+'a')

#Create Topology
arcpy.CreateTopology_management(fdname, prjname+'topology',".01")

#Add Feature Class To Topology ~ MLRA
arcpy.AddFeatureClassToTopology_management(inprname_topology, fdname+'\\'+prjname+'a')

#Add Topology Rule ~ Must Not Have Gaps (Poly)
arcpy.AddRuleToTopology_management (inprname_topology, "Must Not Have Gaps (Area)", fdname+'\\'+prjname+'a')
#Add Topology Rule ~ Must Not Overlap (Poly)
arcpy.AddRuleToTopology_management (inprname_topology, "Must Not Overlap (Area)", fdname+'\\'+prjname+'a')



#Validate Topology
arcpy.ValidateTopology_management(inprname_topology, "FULL_EXTENT")


print ("Script Completed")
