#!/usr/bin/env python

from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl
import getpass
import json  
#from tools import tasks          

def get_obj(content, vimtype, name):
    """
     Get the vsphere object associated with a given text name
    """    
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return obj

config_file = open('range-control.json')
config = json.load(config_file)
config_file.close
vcenter = config["vcenter"]
username = config["username"]
targetfolder = config['target-folder']


print("%s@%s" % (username, vcenter))
password = getpass.getpass("password: ")

s = ssl._create_unverified_context()


si= SmartConnect(host=vcenter, user=username, pwd=password, sslContext=s)
datacenter = si.content.rootFolder.childEntity[0]




f = get_obj(si.content, [vim.Folder], targetfolder)
print("VMS Found Under %s" % (f.name))
index=1
vms = f.childEntity
for vm in vms:
    print("[%d] - %s" %( index, vm.name))
    index += 1
