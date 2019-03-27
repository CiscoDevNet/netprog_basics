# Programming Cisco DNA Center Platform Lessons

* **Introducing Cisco DNA Center Platform APIs and Programmability**
* **Cisco DNA Center Platform APIs Part 1: Exploring Apps and Tools**
* **Cisco DNA Center Platform APIs Part 2: Network Troubleshooting**

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/network_controllers/dnac` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/network_controllers/dnac
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### Postman Setup
During this lesson the Postman client for making REST API calls is used.  For convenience we have included a `postman_collection.json` file that contains all the REST API calls leveraged in the different lessons, and `postman_environment.json` files for each of the DevNet Sandboxes leveraged across the lessons.  These files are all located in the [postman_config](https://github.com/CiscoDevNet/netprog_basics/postman_config) directory in the code repository.  

To leverage them, simply `Import` them into your Postman client.  

1. Collections: Use the **Import** button in the upper left corner of the client.
2. Environments: Use the **Import** button from the `Manage Environments` interface of the client.  

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
The majority of the exercises in this lab can be completed with the available Always On Cisco DNA Center Sandboxes:

    * [Always On: Cisco DNA Center Lab 1](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology)
    * [Always On: Cisco DNA Center Lab 2](https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology)

These sandboxes require no reservation **or** VPN connection.  

To complete the exercises related to the Path Trace API, you'll need to leverage a reservable Cisco DNA Center Sandbox where you'll have administrative access.  

    * [Reservable: Cisco DNA Center Lab 1](https://devnetsandbox.cisco.com/RM/Diagram/Index/b8d7aa34-aa8f-4bf2-9c42-302aaa2daafb?diagramType=Topology)
    * [Reservable: Cisco DNA Center Lab 2](https://devnetsandbox.cisco.com/RM/Diagram/Index/2db69bce-66ca-44cb-9b51-05c2d5b4868d?diagramType=Topology)
    * [Reservable: Cisco DNA Center Lab 3](https://devnetsandbox.cisco.com/RM/Diagram/Index/8076fc05-a818-4bb4-aae1-477680bc2211?diagramType=Topology)
