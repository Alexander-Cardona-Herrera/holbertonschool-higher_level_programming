#!/bin/bash
# send a request and displays only the status
curl -o -I -L -s -w "%{http_code}" "$1"
