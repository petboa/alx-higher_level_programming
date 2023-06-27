#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
url="$1"
file="$2"
curl $url -sX POST -H "Content-Type: application/json" -d @$file
