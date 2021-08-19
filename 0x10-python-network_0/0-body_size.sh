#!/bin/bash
# display the size of the body from the response of the request url 
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
