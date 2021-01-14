# REST APIs Part 2: Making REST API Calls with Postman

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/programming_fundamentals/rest_part_2` directory.  Clone and access it with the following commands: 

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/programming_fundamentals/rest_part_2
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### Postman Setup 
During this lesson the Postman client for making REST API calls is used.  For convenience we have included a `postman_collection.json` file that contains all the REST API calls leveraged in the different lessons, and `postman_environment.json` files for each of the DevNet Sandboxes leveraged across the lessons.  These files are all located in the [postman_config](https://github.com/CiscoDevNet/netprog_basics/tree/master/postman_config) directory in the code repository.  

To leverage them, simply `Import` them into your Postman client.  

1. Collections: Use the **Import** button in the upper left corner of the client. 
2. Environments: Use the **Import** button from the `Manage Environments` interface of the client.  

> Reminder: Many network devices leverage self-signed certificates for `https://` APIs.  Don't forget to turn **OFF** SSL certificate checking within Postman settings.

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
The video and slides for this lab highlight the **Always On: APIC-EM** Sandbox. Cisco DNA Center is a superset of the capabilities of APIC-EM and has replaced it. It is recommended to leverage the Cisco DNA Center Sandbox instead.  The specifics of the API calls for Cisco DNA Center may differ slightly from APIC-EM, however the Postman Collection has the correct DNA Center examples available.

The majority of the exercises in this lab can be completed with the available Always On Cisco DNA Center Sandboxes:

* [Always On: Cisco DNA Center Lab 1](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology)
* [Always On: Cisco DNA Center Lab 2](https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology)

These sandboxes require no reservation **or** VPN connection.  


## Download Slides

You can download the slides for this lesson [here](https://developer.cisco.com/fileMedia/download/8b7d4271-87e4-3e7c-94be-ae06106fc0b2). 

> *Suggestion: Right click, "Open in new tab"*