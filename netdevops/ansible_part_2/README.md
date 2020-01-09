# Ansible Part 2: Using Ansible for Network Configuration

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/netdevops/ansible_part_2` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/netdevops/ansible_part_2
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### Python Environment Setup
It is recommended that this lesson be completed using Python 2.7.   

It is highly recommended to leverage Python Virtual Environments for completing exercises in this course.  

*There is no need to create independent venv for each lesson, but you can if you choose.  At a minimum you should create 2 venvs, one for Python 2 and one for Python 3.*  

Follow these steps to create and activate a venv.  

***Note: If you are leveraging a shared venv across all lessons simply activate it.***

```bash
# OS X or Linux
virtualenv venv --python=python2.7
source venv/bin/activate
```

```bash
# Windows (Explicitly Provide Path to Python2.7 installation)
virtualenv venv --python=c:\Python27\python.exe
venv/Scripts/activate
```

#### Install Python Requirements for Lesson
With the Virtual Environment activated, use pip to install the necessary requirements.  

```bash
# From the code directory for this lesson
pip install -r requirements.txt
```

## DevNet Sandbox
This lesson leverages the [Open NX-OS with Nexus 9Kv On VIRL](https://devnetsandbox.cisco.com/RM/Diagram/Index/1e9b57ff-9e64-4c68-93e5-f0f0a8c6f22c?diagramType=Topology) Sandbox.  

You will need to reserve an instance of the sandbox, and establish a VPN connection to your individual Sandbox to complete this lab.


## Download Slides

You can download the slides for this lesson [here](https://developer.cisco.com/fileMedia/download/c4892148-75c1-3771-9bfd-c7f9281ae509). 

> *Suggestion: Right click, "Open in new tab"*