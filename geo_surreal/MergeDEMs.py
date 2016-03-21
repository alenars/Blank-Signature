#Purpose: Merge together a number of elevation .img files, all residing in a
#common directory, based on a selection set or definition query of IU's index
#shapefile.
#Author: Bruce Nielsen
#Last Update: 2007 05 15
#-Changed geoprocessor call to comply with ArcGIS 9.2 syntax

#Parameters:
#*ArcMap layer of tiles (0)
#*State Plane Zone: East or West (1)
#*Source folder of tiles (2)
#*Output image file (3)

#Outline:
#*Set up search cursor on tile layer
#*Add LABEL for each selected tile to a list
#*Feed list, source folder, and output file name to 'Mosaic to New Raster' tool

import arcgisscripting, string
from os.path import basename, dirname, join
#gp = win32com.client.Dispatch("esriGeoprocessing.GPDispatch.1")
gp = arcgisscripting.create()

TileList = []
#Set variables based on if we're working in State Plane East, or West
if gp.GetParameterAsText(1) == "East":
    EastWest = "spe"
    ##TheProjection = "NAD_1983_StatePlane_Indiana_East_FIPS_1301_Feet"
    gp.AddMessage("Working in State Plane East...")
else:
    EastWest = "spw"
    ##TheProjection = "NAD_1983_StatePlane_Indiana_West_FIPS_1302_Feet"
    gp.AddMessage("Working in State Plane West...")
    
#Make the folder containing the source tiles the default workspace
gp.Workspace = gp.GetParameterAsText(2)

#Create a list of all of the selected tiles
SourceTiles = gp.SearchCursor(gp.GetParameterAsText(0))
ATile = SourceTiles.Next()
while ATile:
    #gp.AddMessage(ATile.LABEL)
    TileList.append("%s_dem_%s.img" % (ATile.LABEL, EastWest))
    ATile = SourceTiles.Next()
    
if len(TileList) > 0:
    #Convert the list into a semicolon-delimited string
    TileString = string.join(TileList, ";")
    gp.AddMessage("Creating %s" % gp.GetParameterAsText(3))
    gp.AddMessage("Mosaicing %s" % TileList)
    #Create the new mosaic
    gp.MosaicToNewRaster_management(TileString, dirname(gp.GetParameterAsText(3)), basename(gp.GetParameterAsText(3)), "#", "32_BIT_FLOAT", "5", "1", "FIRST", "MATCH")
    

else:
    gp.AddMessage("No tiles selected.")

#gp.AddMessage(gp.GetMessages())
