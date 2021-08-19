#!/bin/bash
# send a POST request and displays the body of the content
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
