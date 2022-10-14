# Design Project 1 - Range Control

> This topic will be used mitigate risk from the areas in my scope that are questionable.  These include django as a web framework and pyvmomi as an API.

Week 1 - Set up a Development Environment

* vcenter/esxi/active directory setup (will use vcenter02)
* create a range control service user and a set of "test range users" in AD.
* development workstation [range-control-dev.md](range-control-dev.md) 
  * pyvmomi
  * django

Week 2 - Django AD integration 

* [Active Directory Integration](ad-configuration.md)

* Login to  [django](django.md) using AD credentials and AD security group

Week 3 and 4 - Django pyvmomi integration

* On a Django page, list the VMs that the test user has access to.