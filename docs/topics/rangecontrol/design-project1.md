# Design Project 1 - Range Control

> This topic will be used mitigate risk from the areas in my scope that are questionable.  These include django as a web framework and pyvmomi as an API.

## [Project Kanban](https://github.com/users/gmcyber/projects/2)

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

## Design Project 1 Demonstration

* [Design Topic 1 Demo](https://drive.google.com/file/d/1nzJTZuIw7Mhy0ji56sDOTJIFiLN5JYpG/view?usp=sharing)



## Reflection

> Weeks 1 and 2 tasks went well, The Django pyvmomi integration is on on hold while I investigate using the VMWare Python SDK.  Django integration with LDAP and LDAPs is not straight forward and involved some trial an error debugging.