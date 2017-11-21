# Programming ACI Lessons

* **Got SDN? Understanding the ACI Programmability Options**
* **ACI Programmability Part 1: The ACI Object Model**
* **ACI Programmability Part 2: Using the ACI Toolkit**

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/network_controllers/aci` directory.  Clone and access it with the following commands: 

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/network_controllers/aci
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### Postman Setup 
During this lesson the Postman client for making REST API calls is used.  For convenience we have included a `postmane_collection.json` file that contains all the REST API calls leveraged in the different lessons, and `postman_environment.json` files for each of the DevNet Sandboxes leveraged across the lessons.  These files are all located in the [postman_config](https://github.com/CiscoDevNet/netprog_basics/postman_config) directory in the code repository.  

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

#### Install Python Requirements **NOT** Available on PyPi
This lesson leverages some Python libraries that are **not** currently available on PyPi and able to be installed through `pip install`.  Follow these steps to download and install them.  

##### ACI Toolkit 
**Be sure to have the Python Virtual Environment Activated**

```bash
git clone https://github.com/datacenter/acitoolkit
cd acitoolkit/
python setup.py install
```

##### ACI Python SDK: Cobra
The Python SDK for ACI is typically downloaded from the APIC Controller itself at `https://<APIC IP>/cobra/_downloads/`, however the SDK files are **not** included with the APIC Simulator used for this lesson.  Instead you can download them from DevNet directly using the following steps.  

1. Visit [developer.cisco.com](https://developer.cisco.com) and log into the site.  
2. Download [ACI Cobra](https://developer.cisco.com/fileMedia/download/36cca44f-aa74-42c1-a0ea-c915abf37d38) *Version 2.1-1h* 
3. Download [ACI Model](https://developer.cisco.com/fileMedia/download/b0fb085c-215b-4ba1-a493-2a67c08efba4) *Version 2.1-1h*

***Note: If you click the links before logging into DevNet you will be prompted to login, but the file download will NOT start automatically***

Once downloaded install the Cobra SDK with the following commands.  
**Be sure to have the Python Virtual Environment Activated**

```bash
easy_install -Z acicobra-2.1_1h-py2.7.egg
easy_install -Z acimodel-2.1_1h-py2.7.egg
```

#### Install Python Requirements for Lesson 
With the Virtual Environment activated, use pip to install the necessary requirements.  

```bash
# From the code directory for this lesson
pip install -r requirements.txt
```

#### graphviz & pygraphviz
In **ACI Programmability Part 2: Using the ACI Toolkit**, one exercise involves running the `aci-diagram` application included with the ACI Toolkit.  This application uses the open source diagramming application `graphviz` and the related Python library `pygraphviz`.  Installing these on a Linux or OS X system is straightforward and can be completed with the following steps.  

Install graphviz 

```bash
# On OS X using homebrew 
brew install graphviz

# With yum on Enterprise Linux
yum install graphviz

# With apt-get on Debian
apt-get install graphviz
```

The pygraphviz library is included in the `requirements.txt` file included with the lesson code, however on OS X the installation with pip may miss some needed files.  Use this command to install it fully.  

```bash
pip install pygraphviz \
    --install-option="--include-path=/usr/local/include/graphviz/" \
    --install-option="--library-path=/usr/local/lib/graphviz"
```

***Installation of graphviz on a Windows workstation is more challenging and currently beyond the scope of this lesson and setup.***

## DevNet Sandbox
This lesson leverages the [Always On: ACI APIC](https://devnetsandbox.cisco.com/RM/Diagram/Index/5a229a7c-95d5-4cfd-a651-5ee9bc1b30e2?diagramType=Topology) Sandbox.  This sandbox requires no reservation **or** VPN connection.  