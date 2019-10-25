# Learn to CRUD with GET, POST and DELETE using RESTCONF

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/network_device_apis/restconf` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/network_device_apis/restconf
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
This lesson leverages the [IOS XE on CSR Recommended Code AlwaysOn](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology) Sandbox.  This sandbox requires no reservation **or** VPN connection.  

***Note: In the video, a different DevNet Sandbox is used***

Use host address of `ios-xe-mgmt.cisco.com` and port `9443` for all RESTCONF API connections rather than the address of `10.10.20.21` and port `443` that is used in the videos.
