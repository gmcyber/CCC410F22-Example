import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

import getpass

# Disable cert verification for demo purpose. 
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
user = input("Enter username: ")
pw = getpass.getpass("Enter Password:")

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='vcenter02.cyber.local', username=user, password=pw, session=session)

# List all VMs inside the vCenter Server
vsphere_client.vcenter.VM.list()
