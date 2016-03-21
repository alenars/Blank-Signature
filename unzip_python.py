#**********************************************************************
# File name: Unzip.py
# Description:
#    Unzips the contents of a zip file into a new folder, file geodatabase or ArcInfo
#    workspace. If the zip file contains a file geodatabase, the output workspace name should
#    be given a .gdb extension.
# Arguments:
#  0 - Input zip file
#  1 - Output location that will contain the new workspace
#  2 - The name of the new workspace
#
# Created by: ESRI
#**********************************************************************

# Import modules and create the geoprocessor
import sys, zipfile, arcgisscripting, os, traceback
gp = arcgisscripting.create()

# Function for unzipping the contents of the zip file
def unzip(path, zip):
    isdir = os.path.isdir
    join = os.path.join
    norm = os.path.normpath
    split = os.path.split

    # If the output location does not yet exist, create it
    if not isdir(path):
        os.makedirs(path)    

    for each in zip.namelist():
        gp.AddMessage("Extracting " + os.path.basename(each) + " ...")
        # Check to see if the item was written to the zip file with an
        # archive name that includes a parent directory. If it does, create
        # the parent folder in the output workspace and then write the file,
        # otherwise, just write the file to the workspace.
        if not each.endswith('/'):
            root, name = split(each)
            directory = norm(join(path, root))
            if not isdir(directory):
                os.makedirs(directory)
            file(join(directory, name), 'wb').write(zip.read(each))



if __name__ == '__main__':
    try:
        # Get the tool parameter values
        infile = sys.argv[1]
        outloc = sys.argv[2]
        # outname = sys.argv[3]

        outfol = outloc + "\\" # + outname

        # Create the zipfile handle for reading and unzip it
        zip = zipfile.ZipFile(infile, 'r')
        unzip(outfol, zip)
        zip.close()
        # gp.setparameterastext(3, outfol)

    except:
        # Return any python specific errors and any error returned by the geoprocessor
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " + \
                str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        gp.AddError(pymsg)

        msgs = "GP ERRORS:\n" + gp.GetMessages(2) + "\n"
        gp.AddError(msgs)

