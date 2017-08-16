#!/bin/ksh

#***********************************************************************************************************
# WAS App Deploy Script
#**********************************************************************************************************
#***********************************************************************************************************

#=====================================================================================
# WebSphere related environment variables
#=====================================================================================


export DM_INSTALL_ROOT=/was/app/usr/WebSphere_v85/AppServer/profiles/dmgr
export AS_INSTALL_ROOT=/was/app/usr/WebSphere_v85/AppServer/profiles/wasqrqa2
export WSADMIN_EXE=${DM_INSTALL_ROOT}/bin/wsadmin.sh
export WS_INSTALLABLEAPPS_DIR=${DM_INSTALL_ROOT}/installableApps
export CELL=wasqrqa2Cell
export NODE=`hostname`
export TEMP_DIR=/tmp
export EAR_DIR=/var/tmp

#=====================================================================================
# Miscelleneous environment variables
#=====================================================================================

export ENV=`hostname|cut -c2`
export SCRIPT_LOGS_DIR=/var/tmp/logs
export DATETIME=`date +"%m%d%Y%H%M%S"`
export SCRIPTS_DIR=/was/app/scripts/WASDEPLOY/scripts
export LOG_DIR=/was/app/scripts/WASDEPLOY/logs


cd $DM_INSTALL_ROOT/bin
./wsadmin.sh -lang jython -f $SCRIPTS_DIR/deployApp.py $1 $2 -host wasqrqa2 -port 30104
