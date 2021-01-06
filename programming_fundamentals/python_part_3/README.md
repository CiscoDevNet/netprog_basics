# Python Part 3: Useful Python Libraries for Network Engineers

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/programming_fundamentals/python_part_3` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/programming_fundamentals/python_part_3
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### Python YAML Loading Note
In the video and slides you'll see the use of `yaml.load()` to process YAML data.  The `load` function of the pyyaml library is/was an unsafe method that could be exploited.  You can read about this at [https://msg.pyyaml.org/load](https://msg.pyyaml.org/load). 

The `load()` method is now deprecated and will result in the following error message when used. 

```python
:1: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details
```

The function `yaml.safe_load()` is the recommended alternative to leverage. 


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

***Note: During the lesson, there are instructions to `pip install` different libraries.  If you follow this setup, you will already have the libraries installed, but still run the commands to become familiar with using them***

## DevNet Sandbox
This lesson leverages the [IOS XE on CSR Recommended Code Always On](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology) Sandbox.  This sandbox requires no reservation **or** VPN connection.  

***Note: In the video, a different DevNet Sandbox is used***

In the Python API Examples, the `router` dictionary will use `ios-xe-mgmt.cisco.com` for the address, and different ports than in the video.  The Python example files in the code repository have been updated to use the Always On Sandbox already.


## Download Slides

You can download the slides for this lesson [here](https://developer.cisco.com/fileMedia/download/39d29167-4b3d-3086-b777-3dcfeaeb6a1e). 

> *Suggestion: Right click, "Open in new tab"*