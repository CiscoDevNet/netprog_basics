# Learning Series: Network Programmability Basics
# Module: Programming Fundamentals
# Lesson: REST Part 1
# Author: Hank Preston <hapresto@cisco.com>
#
# curl_examples.sh
# Illustrate the following concepts:
# - REST API Basics
# - Leveraging curl utility

# Example 1: Random Chuck Norris Joke
curl https://api.icndb.com/jokes/random

# Example 2: Nerdy Chuck Norris Joke
curl https://api.icndb.com/jokes/random?limitTo=nerdy

# Example 3: Network Programmability with RESTCONF
curl -vk \
  -u root:cisco123 \
  -H 'accept: application/yang-data+json' \
  https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2
