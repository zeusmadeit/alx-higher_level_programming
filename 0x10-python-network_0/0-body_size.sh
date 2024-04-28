#!/bin/bash
# send a request to a URL with curl, and display the size of the body response
curl -s "$1" | wc -c