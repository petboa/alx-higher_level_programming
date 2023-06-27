#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
url="$1"
curl $url -w '%{http_code}' -so /dev/null
