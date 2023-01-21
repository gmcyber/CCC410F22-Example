from django.http import HttpResponse
from django.shortcuts import render
from rc_django import secure_settings


from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl
import getpass
import json  


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


def listvm(request):
    s = ssl._create_unverified_context()
    si= SmartConnect(host=secure_settings.VCENTER_SERVER, user=secure_settings.VCENTER_USER, pwd=secure_settings.VCENTER_PASSWORD, sslContext=s)
    datacenter = si.content.rootFolder.childEntity[0]

    f = get_obj(si.content, [vim.Folder], secure_settings.TARGET_FOLDER)
    vms = f.childEntity
    return render(request, 'vms.html', {'vms':vms})
