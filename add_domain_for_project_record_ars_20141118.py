#Add Domain Yes or No to Project Record
#A. Stephens
#11/18/2014


import arcpy

arcpy.env.overwriteOutput = True

in_workspace = arcpy.GetParameterAsText (0) #Input Project Record File Geodatabase
inFC = arcpy.GetParameterAsText (1) #Input Project Record Feature Class

doname = "RECERT_NEEDED" #Domain Name 

#Create Domain

arcpy.CreateDomain_management(in_workspace, doname, "No or Yes", "TEXT", "CODED")

# Add Coded Value to Domain

arcpy.AddCodedValueToDomain_management (in_workspace, doname, "Yes", "Yes")

arcpy.AddCodedValueToDomain_management (in_workspace, doname, "No", "No")

#Assign Domain To Field

arcpy.AssignDomainToField_management (inFC, "RECERT_NEEDED", doname)


