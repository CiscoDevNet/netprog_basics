# Linux at the Edge: Introduction to Guest Shell

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/application_hosting/guestshell` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/application_hosting/guestshell
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

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
This lesson leverages the [IOS XE on CSR Recommended Code](https://devnetsandbox.cisco.com/RM/Diagram/Index/cae403c2-27af-4c7d-b1e1-99b7d42f1504?diagramType=Topology) Sandbox.  

You will need to reserve an instance of the sandbox, and establish a VPN connection to your individual Sandbox to complete this lab.

***Note: In the video, an older version of IOS XE was used.***

The commands to enable GuestShell have changed slightly, be sure to refer to the [sample configuration in the code samples](https://github.com/CiscoDevNet/netprog_basics/blob/master/application_hosting/guestshell/iosxe_guestshell_setup.txt#L40) for the latest command syntax. 



## Download Slides

You can download the slides for this lesson [here](https://developer.cisco.com/fileMedia/download/587b59b9-6b7b-3b7b-bce4-ce3acf182e16). 

> *Suggestion: Right click, "Open in new tab"*