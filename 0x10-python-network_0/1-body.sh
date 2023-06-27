#!/bin/bash
#script that takes in a URL, sends a GET request to the URL, and displays the body of the response
url="$1"
curl -sL $url
