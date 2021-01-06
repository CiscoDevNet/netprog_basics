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
It is recommended that this lesson be completed using Python 3.8.  Other versions of Python 3 should also work.

> **Note about Python 2:** Python 2 was [sunset](https://www.python.org/doc/sunset-python-2/) by Python Software Foundation on January 1, 2020. This means that no more updates to Python 2 are being worked on, including security updates.  Python 3 is now the recommended version of Python for everyone to use. Most Python developers of software, packages, and scripts have migrated to Python 3 already, however you may find some older scripts and tools that are no longer maintained that only work with Python 2. 
> 
> You may see/hear references to Python 2 within the videos in this course from before January 2020, however all examples scripts and demos available in the GitHub repo to run have been updated to leverage Python 3.

It is highly recommended to leverage Python Virtual Environments for completing exercises in this course.  

*There is no need to create independent venv for each lesson, but you can if you choose.*  

Follow these steps to create and activate a venv.  

***Note: If you are leveraging a shared venv across all lessons simply activate it.***

```bash
# OS X or Linux
python3 -m venv venv
source venv/bin/activate
```

```bash
# Windows
python -m venv venv
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

Download and install version 1.4 or higher from [Cisco Downloads](https://software.cisco.com/download/home/286306005/type/286306762/release).  

Save ioxclient into one of the following locations:

* The `netprog_basics/application_hosting/iox` directory on your workstation
* A directory that exists within your `PATH` environment variable.  
    * *Example: `/usr/local/bin` on OS X or Linux*

## DevNet Sandbox
This lesson leverages the [IOx](https://devnetsandbox.cisco.com/RM/Diagram/Index/856d2943-eded-4f45-a76b-e50ee3dc9c02?diagramType=Topology) Sandbox.  

You will need to reserve an instance of the sandbox, and establish a VPN connection to your individual Sandbox to complete this lab.


## Download Slides

You can download the slides for this lesson [here](https://developer.cisco.com/fileMedia/download/517a487c-4442-3408-a066-fe17c3795e07). 

> *Suggestion: Right click, "Open in new tab"*
