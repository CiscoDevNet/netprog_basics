# Programming with NX-API Lessons
* **NX-API Part 1: Get Started with APIs and Nexus**
* **NX-API Part 2: Dive into the Nexus Object Model**

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/network_device_apis/nxapi` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/network_device_apis/nxapi
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
This lesson leverages the [Always On: Open NX-OS Programmability](https://devnetsandbox.cisco.com/RM/Diagram/Index/dae38dd8-e8ee-4d7c-a21c-6036bed7a804?diagramType=Topology) Sandbox.  This sandbox requires no reservation **or** VPN connection.  


## Download Slides

You can download the slides for this lesson here.

* [**NX-API Part 1: Get Started with APIs and Nexus**](https://developer.cisco.com/fileMedia/download/de3355ca-aa6e-398a-9c09-5eedb28a957e)
* [**NX-API Part 2: Dive into the Nexus Object Model**](https://developer.cisco.com/fileMedia/download/baf5bda7-1337-330e-bcf6-a2b72cc6e65d)

> *Suggestion: Right click, "Open in new tab"*