#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -so /dev/null -w "You got me!" "http://0.0.0.0:5000/catch_me"
