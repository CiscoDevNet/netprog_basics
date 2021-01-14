#! /bin/bash

echo "Step 2: Killing VPN Connection to Pod"
OCPID=$(cat openconnect_pid.txt)
kill ${OCPID}
rm openconnect_pid.txt
