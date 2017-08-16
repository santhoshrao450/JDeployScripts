import sys, java
from time import sleep
lineSeparator = java.lang.System.getProperty('line.separator')
#----------------------------------------------------------------
# set up globals
#----------------------------------------------------------------
global AdminConfig
global AdminControl
global AdminApp

def deployApp (appName, earLocation):
    print "updating the application..."
    appOptions         = []
    appNameOption      = ["-appname", appName]
    updateOption       = ["-update"]
    updateIgnoreOption = ["-update.ignore.new"]

    appOptions.extend(appNameOption)
    appOptions.extend(updateOption)
    appOptions.extend(updateIgnoreOption)

    AdminApp.install(earLocation, appOptions)

    #----------------------------------------------------------------
    # Save and Sync
    #----------------------------------------------------------------
    print "Performing Save and Synchronize of the changes ......"
    AdminConfig.save()

    nodesInCell = AdminConfig.list("Node")
    nodeList    = nodesInCell.split(lineSeparator)
    
    for nodeId in nodeList:
        node = (nodeId.split('('))[0]
        print "Synchronizing Node " + node + " now ..."
        nodeSync = AdminControl.completeObjectName("type=NodeSync,node=" + node + ",*")
        if len(nodeSync) == 0:
            print "Warning -- NodeSync MBean not found for node " + node
            print "No action required for " + node
        else:
            AdminControl.invoke(nodeSync, "sync")
            sleep(15)

    print "Completed the Save and Sync operation."


#----------------------------------------------------------------
# Main
#----------------------------------------------------------------

if (len (sys.argv) != 2):
        print "deployApp: This script requires 2 parameters -"
        print "Application name and ear file location"
else:
        appName = sys.argv[0]
        earLocation = sys.argv[1]

        print "Starting deployment of the application...."
        deployApp(appName, earLocation)
        print "Deployment of application " + appName + " completed."
