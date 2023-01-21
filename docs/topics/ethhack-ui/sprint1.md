# Sprint 1

## Deliverable Statement

Sprint 1 will be used to develop the secure build and code deployment process for a new server called Ethhack UI. Django will become an https application and the django server will be fronted by either an apache or nginx reverse proxy server. I'm interested in deploying via git triggers and will investigate that.

* [Milestone](https://github.com/gmcyber/CCC410F22-Example/milestone/3)

## Objectives

* Create an ansible playbook to deploy a Django Server with the dependencies discovered during the design phase
* Select and Integrate an SSL reverse proxy so that Django's SSL performance is backed by a production web server as opposed to the development server shipped in the Django project
* Automate the build process via script or CI/CD pipeline

## Sprint 1 Reflections

### Week 1

I really wished, I'd name the project something other than range control.  It was such a great name, that I decided to use it on an project I just opensourced https://github.com/gmcyber/rangecontrol.  Refactoring by changing names broke a lot of links.  I also spent some time reorganizing my milestones and tasks.  No new things were learned but I did brush up on my ansible skills that will be needed in the upcoming week.