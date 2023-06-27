#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
url="$1"
curl -so /dev/null $url -w "%{size_of_body}\n"
