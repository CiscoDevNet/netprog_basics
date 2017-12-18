# REST APIs Part 1: HTTP is for more than Web Browsing

## "Gitting" the Code
All of the code and examples for this lesson is located in the `netprog_basics/programming_fundamentals/rest_part_1 ` directory.  Clone and access it with the following commands:

```bash
git clone https://github.com/CiscoDevNet/netprog_basics
cd netprog_basics/programming_fundamentals/rest_part_1
```

## Local Workstation Setup
Be sure to complete the [General Workstation Setup](https://github.com/CiscoDevNet/netprog_basics/blob/master/readme_resources/workstation_setup.md) instructions before beginning this lesson.  

### curl on Windows
In this lesson the Linux utility `curl` is used to send basic REST API requests.  On Linux and OS X, `curl` is available and installed by default.  

Windows does **not** come with `curl` by default, but today there are several options for running Linux utilities like `curl` on Windows with ease.  Here are two options to use.  

1. `git bash`: When you install git for Windows, it includes `git bash` which is a bash shell  option for Windows that includes common Linux tools such as `curl`.  Just start `git bash` and work as if you are within bash on Linux.  
2. `Ubuntu Bash`: If you are on Windows 10 you can install Ubuntu Bash using the Linux Subsystem for Windows.  Once installed you can run the Ubuntu Bash Shell and work within Linux from Windows.  

## DevNet Sandbox
This lesson leverages the [Always On: NETCONF/YANG & RESTCONF on IOS XE](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology) Sandbox.  This sandbox requires no reservation **or** VPN connection.  

***Note: In the video, a different DevNet Sandbox is used***

When running the `curl` for the RESTCONF example, leverage `https://ios-xe-mgmt.cisco.com:9443` as the URL instead of `https://10.10.20.21`.    
