# General Workstation Setup
Before you dive into the individual labs and modules, and their pre-reqs, take time to review this page for general setups steps and assumptions related to software to be installed, and any suggested configuration details.  This is not intended to be a comprehensive installation guide for these tools, or general workstation prep, but rather provide guidance and links to resources that are already available on DevNet and other locations.  

In this guide you will find recommendations on tools and applications to use, however there are many ways to accomplish anything in IT.  If you are already familiar with another method, feel free to use that as long as the end result meets the fundamental requirement.  

## Operating System Considerations
The vast majority of the lessons and exercises in the course can be completed from a Windows, Mac, or Linux based workstation.  However there are some cases where an operating system requirement may exist.  In those cases, it will be called out in the prep material for each module and lab.  Some basic notes on operating system choices are provided here.  

### Windows
While Windows has had a reputation of being a difficult platform for network programmability and development options, outside of .NET based development, Microsoft has made great strides to add new features for the general developer using a Windows system recently.  With Windows 10, developers can now have a very similar experience as on a Mac or Linux system, with the benefits that Windows offers.  

Features such as the Linux Subsystem that allow Ubuntu Bash to run natively on Windows, the inclusion of Hyper-V for supporting virtualization of platforms, and solid Docker for Windows support make Windows 10 an excellent choice for Network Programmability.  However, the installation and management of applications, utilities, and languages on Windows still lack some of the simplicity, or default inclusion, that are available on Mac or Linux options.  

**Incompatibility Note:** Ansible is a very popular configuration management tool for network programmability, and currently Windows is **not** supported as the control system for Ansible.  This means that you will need to leverage an option such as a Linux VM or the Ubuntu Bash with Linux Subsystem for working with Ansible from a Windows workstation.  

### Mac
OS X and Mac laptops are becoming quite popular with network engineers, and it makes a great platform for network programmability.  Because of it's Linux roots, many of the same tools, utilities, and software that are popular in Linux development work exactly the same on OS X.  

One aspect of Linux distriubtions that is not included by default with OS X is an application package manager (ie yum or apt).  There are a few options that have been developed by the OpenSource community that fill this gap.  One very popular and useful one is [Homebrew](http://brew.sh).  The use of this tool can make installation and management of development tools very straightforward on a OS X.  You will find references to this tool in this course documentation.  

### Linux
Linux, as well as the specific distributions like Ubuntu, CentOS, Red Hat, etc, are quite popular and powerful as a development environment owing to their popularity for the actual end systems and servers.  For example, nearly all network appliances are built on-top of a Linux kernel today.  

## Setting up git

Managing code repositories and source control is not a core topic of this course, however a basic working knowledge of how to clone code from a source, and the utilities to do the cloning are needed to obtain and keep updated the source code and examples for the exercises.  

You can download and find installation instructions for the latest version of git on the download site: [https://git-scm.com/downloads](https://git-scm.com/downloads).  

### Mac OS X Note
In addition to downloading from the site above, OS X also includes the command line utilities for git within the X-Code tools included in the operating system.  Simply executing `git` from the terminal on a Mac will prompt you to accept a license and then complete the setup.  

## Setting Up Python
Many of the exercises in the course will leverage Python so it is critical to setup and install it properly.  In addition, it is recommended to install the latest versions of both Python 2.7 and Python 3 as some of the tools and technologies discussed are version dependent.  

The main source of download information on Python is at [https://www.python.org/downloads/](https://www.python.org/downloads/).  

In addition, here are some notes and suggestions for Python installation on each of the main platforms.  

### Windows
Download the installers for both Python 2.7 and 3.x from the above site and install them on your workstation with the following suggestions.  

* Install Python 2.7 and then Python 3
* During the installation of both, be sure review the settings and select the option to add Python to your path
  * By default the installer does **not** do this, which means you would need to explicitly provide the full path to `python.exe` whenever running commands.  

### Mac OS X
OS X includes Python natively, however it is **not** the latest version.  Though the included version may work for most exercises, there are many bugs and fixes in later versions that you will want to have to use.  Though you can download installers from python.org at the link above, you can also leverage Homebrew to install and maintain Python.  The following commands will install the latest versions of Python 2.7 and Python3.  

```bash
brew install python2
brew install python3
```

This will alias the command `python2` to the latest version of Python 2.7.  Likewise, `python3` will be the latest version of Python 3.  

You can upgrade your installed versions of Python with

```bash
brew upgrade python2
brew upgrade python3
```

### Linux
Though all Linux distro's provide an application package manager, they often lack the latest versions of Python in the supported repos.  There are alternative repositories you can install and use, however it is often easier and better to download and install from source.  The following example shows how to download and install both Python 2.7.14 and Python 3.6.2 from source.  

*May require sudo*

```bash
# Python 2
cd ~
wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz
tar xzf Python-2.7.14.tgz
cd Python-2.7.14
./configure
make altinstall

# Python 3
cd ~
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
tar xzf Python-3.6.3.tgz
cd Python-3.6.3
./configure
make altinstall
```

### Standard Python Utilities
With Python installed, you'll also want to make sure two Python utilities are installed and working.  

#### pip
`pip` allows developers to install libraries and modules with Python for added capablities, such as making NETCONF requests with ncclient.  If you installed the latest versions of Python as suggested, you should have pip installed already.  Test with `pip --version`.  

If it is not installed, you can do so by downloading [`get-pip.py`](https://bootstrap.pypa.io/get-pip.py) and then running the file with Python.  

```bash
# OS X or Linux
python2 get-pip.py
python3 get-pip.py
```

Windows installers will have installed pip by default.  

#### virtualenv
A Virtual Environment is an isolated Python instance (directory structure) that can be created with a specific version of Python and an independent set of libraries installed and available.  This allows developers to have different Virtual Environments for different projects or applications, where they could have conflicting settings.  `virtualenv` is the Python utility for creating virtual environments, and it is installed with `pip`

```bash
pip install virtualenv
```

On Mac or Linux it may require `sudo`

```bash
sudo pip install virtualenv
```

## Postman
Working with REST APIs is an important skill for any developer today, including network programmability focused engineers.  Postman is an excellent tool for exploring, testing and working with REST APIs.  Download and install it from [https://www.getpostman.com](https://www.getpostman.com).  

***Note:*** Postman was originally deployed as a Google Chrome Application, but is now available as a standalone application.  As Chrome apps are being phased out by Google, it is recommended to use the standalone application.  

## DevNet Sandbox VPN Access
Many of the lessons leverage a Reserved [DevNet Sandbox](http://developer.cisco.com/sandbox) as the target infrastructure.  To connect to your sandbox, you'll need to VPN in.  

The most common VPN Client to use is Cisco AnyConnect which is available to [download from Cisco](https://software.cisco.com/download/release.html?mdfid=286281283&softwareid=282364313&release=4.5.02036&relind=AVAILABLE&rellifecycle=&reltype=latest).  

You can also leverage the OpenSource Client [OpenConnect](http://www.infradead.org/openconnect/index.html).
