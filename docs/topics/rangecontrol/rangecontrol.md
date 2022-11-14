# Range Control

> Range control will be a secure web application that abstracts the details of vcenter traditionally used for SEC335 from students.  The idea is to emulate some of the key features used in commercial range platforms like HackTheBox and others.

## Why?

VCenter's web client is overkill for the low interaction needs of a cyber security range.  The student needs a client such as kali and windows 10 desktop and they need the networking to reach their assigned set of targets.  That is it.  Using the vcenter webui, ties us to vcenter, esxi and vmware based products.  A web interface would allow us to swap out the backend virtualization layer should we want to later.

This project will also allow me to exercise programming, system administration and security skills to develop an open source offering that has similar functionality to commercial for profit range and ctf platforms.

## Features/Objectives

* Single Signon (SSO) will use Active Directory as the authentication (accounts) and authorization (AD security groups)
* The application backend will integrate with vcenter such that available target VMs are displayed to the student.
* Students will be able to perform the following actions
  * Reset the target
  * Enter *n* flags where a key represents a flag (user or root) flag found on the system.  The user will received feedback on whether the flag is correct.  The application will also track the user's progress through the set of range targets.
  * Metadata such as the following will be displayed
    * uptime
    * powerstate
    * public IP address
    * hostname
  * A user will be able to restore the target to "target ready state" in the case where they need to restart the exercise from scratch.
  * Students will be able to retrieve target hints, in a manner similar to CTF platforms.  The number of hints used during target interaction will also be stored.

## Constraints

* Very likely going to be a python or python web framework based application.  Pyvmomi libraries are relatively mature but will likely require far more work than the powershell frameworks I'm used to.
* We are a vmware shop, so the back end is known.

## Design Projects (Fall 2022)

*  [Design 1](design-project1.md) 
*  [Design 2](design-project2.md) 
*  Final Presentation and Demonstration :construction:

## Implementation Sprints (Spring 2023)

* Sprint 1 :construction:
* Sprint 2 :construction:
* Sprint 3 :construction:
* Sprint 4 :construction:
* Capstone Presentation :construction: