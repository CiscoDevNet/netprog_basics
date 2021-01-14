# Ansible Part 2: Using Ansible for Network Configuration

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/netdevops/ansible_part_2` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/netdevops/ansible_part_2
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### Ansible Version Information
Like many automation tools, Ansible is a rapidly evolving and updating tool. With each release some key parts of Ansible have evolved. Elements such as inventory management, device connections, and playbook/module structure evolve.

The videos, slides, and labs in this module were created using the version of Ansible that was current at the time, but much has changed since then. The examples included in the repository have been tested with the version of Ansible listed in the [requirements.txt](https://github.com/CiscoDevNet/netprog_basics/blob/master/netdevops/ansible_part_2/requirements.txt) files that accompany each lab. 

> You may find slight differences in the playbooks, variables files, configuration, etc from the video. These differences reflect updates to Ansible since the video was recorded. 

***It is highly recommended you leverage the listed version of Ansible initially.  If you wish to explore and test newer versions of Ansible, be aware you may run into problems.*** 

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

## DevNet Sandbox
This lesson leverages the [Open NX-OS with Nexus 9Kv On VIRL](https://devnetsandbox.cisco.com/RM/Diagram/Index/1e9b57ff-9e64-4c68-93e5-f0f0a8c6f22c?diagramType=Topology) Sandbox.  

You will need to reserve an instance of the sandbox, and establish a VPN connection to your individual Sandbox to complete this lab.


## Download Slides

You can download the slides for this lesson [here](https://developer.cisco.com/fileMedia/download/c4892148-75c1-3771-9bfd-c7f9281ae509). 

> *Suggestion: Right click, "Open in new tab"*