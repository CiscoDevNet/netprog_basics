# Python at the Edge: Super Charged Network Event Management

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/application_hosting/python_onbox` directory.  Clone and access it with the following commands: 

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/application_hosting/python_onbox
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### Python Environment Setup 
It is recommended that this lesson be completed using Python 3.6.  A recent version of Python 2.7 or Python 3.5 should also work.  

It is highly recommended to leverage Python Virtual Environments for completing exercises in this course.  

*There is no need to create independent venv for each lesson, but you can if you choose.  At a minimum you should create 2 venvs, one for Python 2 and one for Python 3.*  

Follow these steps to create and activate a venv.  

***Note: If you are leveraging a shared venv across all lessons simply activate it.***

```bash
# OS X or Linux 
virtualenv venv --python=python3
source venv/bin/activate
```

```bash
# Windows (assumes Python 3 is default)
virtualenv venv 
venv/Scripts/activate 
```

#### Install Python Requirements for Lesson 
With the Virtual Environment activated, use pip to install the necessary requirements.  

```bash
# From the code directory for this lesson
pip install -r requirements.txt
```

## DevNet Sandbox
This lesson leverages the [IOS XE Programmability](https://devnetsandbox.cisco.com/RM/Diagram/Index/7fd27b24-7034-477d-9ad2-e2c8096dd1a5?diagramType=Topology) Sandbox.  

You will need to reserve an instance of the sandbox, and establish a VPN connection to your individual Sandbox to complete this lab.

### Post Reservation Setup 
This lesson assumes the following about the Sandbox:

* Guest Shell has already been enabled on the IOS XE Sandbox instance 
* `git` has been installed within the running Guest Shell container  

If you have already completed the exercises within the **Linux at the Edge: Introduction to Guest Shell** lesson using your Sandbox instance then you are all set and ready to go.  If not, you will need to complete the following additional steps.  

1. Enable Guest Shell: Use the commands and information from [iosxe\_guestshell\_setup.txt](iosxe_guestshell_setup.txt).  

**Clone Code Repo to Guest Shell**

With Guest Shell setup, now clone the code for the labs into Guest Shell in your Sandbox Instance.

```
! From Enable mode on your Sandbox Device
guestshell run git clone https://github.com/CiscoDevNet/netprog_basics /flash/netprog_basics    
```