#### Generic Oracle WebLogic 11g Start Script
#### Created by Michel Schildmeijer
####
#### Completely rewritten and simplified by L.J. van der Starre
#### Yeah yeah yeah, I know ... Won't work on a domain with multiple
#### machines. At least we don't need bloody sleep-commands in osb_rc.sh
#

# Set some constants
#
MS1Name = 'soa_server2'
MS2Name = 'bam_server2'
#
# Set some constants
from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py'  # load domain specific constants

nmConnect(NMAdminUser, NMAdminUserPW, hostname, nmPort, WL_DOMAIN, WL_DOMAIN_DIR, nmType)

try:
  nmStart(MS1Name)
except:
  pass

nmDisconnect()

