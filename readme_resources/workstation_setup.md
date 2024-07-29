# Developer Workstation and Environment Setup
Before you dive into the individual labs and modules, and their pre-reqs, take time to review this page for: 

* General setup steps
* Assumptions related to software to be installed
* Any suggested configuration details.  

This is not intended to be a comprehensive installation guide for these tools, or general workstation prep, but rather provide guidance and links to resources that are already available on DevNet and other locations.  

In this guide you will find recommendations on tools and applications to use, however there are many ways to accomplish anything in IT.  If you are already familiar with another method, feel free to use that as long as the end result meets the fundamental requirement.  

## Operating System Considerations
The vast majority of the lessons and exercises in the course can be completed from a Windows, Mac, or Linux based workstation.  However there are some cases where an operating system requirement may exist.  In those cases, it will be called out in the prep material for each module and lab.  Some basic notes on operating system choices are provided here.  

### Windows
While Windows has had a reputation of being a difficult platform for network programmability and development options, outside of .NET based development, Microsoft has made great strides to add new features for the general developer using a Windows system recently. With Windows 10, developers can now have a very similar experience as on a Mac or Linux system, with the benefits that Windows offers.  

Features such as the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) that allow a GNU/Linux environment to run natively on Windows, the inclusion of Hyper-V for supporting virtualization of platforms, and solid [Docker for Windows](https://docs.docker.com/docker-for-windows/install/) support make Windows 10 an excellent choice for Network Programmability. However, the installation and management of applications, utilities, and languages on Windows still lack some of the simplicity, or default inclusion, that are available on Mac or Linux options.  

> **Incompatibility Note:** Ansible is a very popular configuration management tool for network programmability, and currently Windows is **not** supported as the control system for Ansible. This means that you will need to leverage an option such as a Linux VM, the Windows Subsystem for Linux, or a Docker container for working with Ansible from a Windows workstation.  

### Mac
OS X and Mac laptops are becoming quite popular with network engineers, and it makes a great platform for network programmability. Because of its Linux roots, many of the same tools, utilities, and software that are popular in Linux development work exactly the same on OS X.  

One aspect of Linux distributions that is not included by default with OS X is an application package manager (ie yum or apt).  There are a few options that have been developed by the OpenSource community that fill this gap.  One very popular and useful one is [Homebrew](http://brew.sh). The use of this tool can make installation and management of development tools very straightforward on a OS X.  You will find references to this tool in this course documentation.  

### Linux
Linux, as well as the specific distributions like Ubuntu, CentOS, Red Hat, etc, are quite popular and powerful as a development environment owing to their popularity for the actual end systems and servers. For example, nearly all network appliances are built on-top of a Linux kernel today.  

## Python

All labs, demonstrations, and examples accompanying the videos in the course should be completed using Python 3.8. Other versions of Python 3 should also work. It is highly recommended to leverage a Python Virtual Environment for completing exercises in this course.

> **Note about Python 2:** Python 2 was [sunset](https://www.python.org/doc/sunset-python-2/) by Python Software Foundation on January 1, 2020. This means that no more updates to Python 2 are being worked on, including security updates. Python 3 is now the recommended version of Python for everyone to use. Most Python developers of software, packages, and scripts have migrated to Python 3 already, however you may find some older scripts and tools that are no longer maintained that only work with Python 2. 
> 
> You may see/hear references to Python 2 within the videos in this course from before January 2020, however all examples scripts and demos available in the GitHub repo to run have been updated to leverage Python 3.

## Setting up your development environment
A great first stop are the [**Learning Labs on Developer Workstation and Environment Setup**](http://developer.cisco.com/learning/modules/dev-setup). The first lab discusses what goes into a dev workstation, and gives some suggested tools. The following labs walk through installing the tools on different platforms.

### What is a Development Environment, and why do you need one?
What exactly goes into a development environment and why? What is the bare minimum you need to get started, and what choices do I need to make related to platforms and operating systems? We'll lay out the details in this quick overview.

[![](https://github.com/CiscoDevNet/netprog_basics/raw/master/readme_resources/dev-env.jpg)](https://developer.cisco.com/learning-labs/setup/#dev-why)

**View the Video:** [Watch a video of the lesson.](https://developer.cisco.com/learning-labs/setup/#dev-why) 

**Take the Lab:** [Complete the Learning Lab on DevNet](https://developer.cisco.com/learning/modules/dev-setup/dev-what/step/1)

### Setting up your Windows workstation as a development environment

So you are a follower of Gates, Balmer, and Nadella, excellent! Let's super charge that Windows workstation with everything you need to be a programability ninja!

[![](https://github.com/CiscoDevNet/netprog_basics/raw/master/readme_resources/dev-env-win.jpg)](https://developer.cisco.com/learning/modules/dev-setup/dev-win/introduction/)

**View the Video:** [Watch a video of the lesson.](https://developer.cisco.com/learning/modules/dev-setup/dev-win/introduction/) 

**Take the Lab:** [Complete the Learning Lab on DevNet](https://developer.cisco.com/learning/modules/dev-setup/dev-win/introduction/)

### Setting up your macOS workstation as a development environment
Are you a fan of black turtle necks and clean design lines? Perfect! Grab your Mac and let's get you ready to put that BSD base to work and slap some stickers all over the shiny case.

[![](https://github.com/CiscoDevNet/netprog_basics/raw/master/readme_resources/dev-env-mac.jpg)](https://developer.cisco.com/learning/modules/dev-setup/dev-mac/introduction/)

**View the Video:** [Watch a video of the lesson.](https://developer.cisco.com/learning-labs/setup/#dev-mac) 

**Take the Lab:** [Complete the Learning Lab on DevNet](https://developer.cisco.com/learning/modules/dev-setup/dev-mac/step/1)

### Setting up your Linux workstation as a development environment
Does Open Source speak to you on a personal level? That's great, grab your penguin and let's dive in and make Linus proud.

[![](https://github.com/CiscoDevNet/netprog_basics/raw/master/readme_resources/dev-env-centos.jpg)](https://developer.cisco.com/learning-labs/setup/#dev-centos)

#### CentOS 
**View the Video:** [Watch a video of the lesson.](https://developer.cisco.com/learning-labs/setup/#dev-centos) 

**Take the Lab:** [Complete the Learning Lab on DevNet](https://developer.cisco.com/learning/modules/dev-setup/dev-centos/step/1)

#### Ubuntu 
**Take the Lab:** [Complete the Learning Lab on DevNet](https://developer.cisco.com/learning/modules/dev-setup/dev-ubuntu/step/1)
