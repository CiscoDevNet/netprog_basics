# Package, Deploy and Run Applications in the Network with IOx

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/application_hosting/iox` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/application_hosting/iox
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

### Docker Client Installation
In this lab, you will package and deploy a containerized application to IOx using Docker Tooling.  To do so, you'll need Docker version 1.11 or higher installed for your workstation.  Docker is supported across Linux, OS X, and Windows operating systems.  

Visit [www.docker.com/get-docker](https://www.docker.com/get-docker), download and install the client for your platform.  

### IOx Client Installation
IOx Client is an application you'll run use to package, deploy and install applications to IOx devices.  

Download and install version 1.4 or higher from [Cisco Downloads](https://software.cisco.com/download/release.html?mdfid=286306005&softwareid=286306762&release=1.4.0&relind=AVAILABLE&rellifecycle=&reltype=latest).  

Save ioxclient into one of the following locations:

* The `netprog_basics/application_hosting/iox` directory on your workstation
* A directory that exists within your `PATH` environment variable.  
    * *Example: `/usr/local/bin` on OS X or Linux*

## DevNet Sandbox
This lesson leverages the [IOx](https://devnetsandbox.cisco.com/RM/Diagram/Index/864622c2-24bd-47ca-867d-015dbe44e185?diagramType=Topology) Sandbox.  

You will need to reserve an instance of the sandbox, and establish a VPN connection to your individual Sandbox to complete this lab.


## Download Slides

You can download the slides for this lesson [here](https://developer.cisco.com/fileMedia/download/517a487c-4442-3408-a066-fe17c3795e07). 

> *Suggestion: Right click, "Open in new tab"*