

def GetDownload(areasym, surveyDate, importDB):
    # download survey from Web Soil Survey URL and return name of the zip file
    # want to set this up so that download will retry several times in case of error
    # return empty string in case of complete failure. Allow main to skip a failed
    # survey, but keep a list of failures
    #
    # Only the version of zip file without a Template database is downloaded. The user
    # must have a locale copy of the Template database that has been modified to allow
    # automatic tabular imports.

    # create URL string from survey string and WSS 3.0 cache URL
    baseURL = "http://hazards.fema.gov/femaportal/NFHL/Download/"

    #ProductsDownLoadServlet?DFIRMID=17055C&state=Illinois&county=Franklin County&fileName=17055C_20091118...

    try:
        # List of states that use a Template database other than US_2003.
        # This list will have to be updated in the future if it is used to
        # get downloads with the Template database included in the zipfile.
        dbInfo = {'AK':'AK', 'CT':'CT', 'FL':'FL', 'GA':'GA', 'HI':'HI', 'IA':'IA', \
        'ID':'ID', 'IN':'IN', 'ME':'ME', 'MI':'MI', 'MN':'MN', 'MT':'MT', 'NC':'NC', \
        'NE':'NE', 'NJ':'NJ', 'OH':'OH', 'OR':'OR', 'PA':'PA', 'SD':'SD', 'UT':'UT', \
        'VT':'VT', 'WA':'WA', 'WI':'WI', 'WV':'WV', 'WY':'WY', 'FM':'HI', 'PB':'HI'}

        # Incorporate the name of the Template database into the URL
        st = areaSym[0:2]
        if st in dbInfo:
            db = "_soildb_" + dbInfo[st] + "_2003"
        else:
            db = "_soildb_US_2003"

        # Use this zipfile for downloads without the Template database
        zipName = "wss_SSA_" + areaSym + "_[" + surveyDate + "].zip"

        # Use this URL for downloads with the state or US_2003 database
        #zipName = "wss_SSA_" + areaSym + db + "_[" + surveyDate + "].zip"

        zipURL = baseURL + zipName

        PrintMsg("\tDownloading survey " + areaSym + " from Web Soil Survey...", 0)

        # Open request to Web Soil Survey for that zip file
        request = urlopen(zipURL)

        # set the download's output location and filename
        local_zip = os.path.join(outputFolder, zipName)

        # make sure the output zip file doesn't already exist
        if os.path.isfile(local_zip):
            os.remove(local_zip)

        # save the download file to the specified folder
        output = open(local_zip, "wb")
        output.write(request.read())
        output.close()
        del request
        del output

        # if we get this far then the download succeeded
        return zipName

    except URLError, e:
        if hasattr(e, 'reason'):
            PrintMsg("\t\t" + areaSym + " - URL Error: " + str(e.reason), 1)

        elif hasattr(e, 'code'):
            PrintMsg("\t\t" + areaSym + " - " + e.msg + " (errorcode " + str(e.code) + ")", 1)

        return ""

    except socket.timeout, e:
        PrintMsg("\t\t" + areaSym + " - server timeout error", 1)
        return ""

    except socket.error, e:
        PrintMsg("\t\t" + areasym + " - Web Soil Survey connection failure", 1)
        return ""

    except:
        # problem deleting partial zip file after connection error?
        # saw some locked, zero-byte zip files associated with connection errors
        PrintMsg("\tFailed to download zipfile", 0)
        return ""
        sleep(1)
        return ""
