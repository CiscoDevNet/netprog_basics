# Learning Series: Network Programmability Basics
# Module: Application Hosting
# Lesson: Package, Deploy and Run Applications in the Network with IOx
# Author: Hank Preston <hapresto@cisco.com>
#
# Dockerfile
# Illustrate the following concepts:
# - Deploy an IOx application using Docker tooling
FROM alpine:3.5
RUN apk add --update \
    python3

# Install Python application requirement
RUN pip3 install bottle

# Application runs on port 8000
EXPOSE 8000

# Add application code to container
COPY main.py /main.py

# Start application 
CMD python3 /main.py
