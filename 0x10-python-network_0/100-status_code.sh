#!/usr/bin/bash
# get code url
curl -s -o /dev/null -w "%{http_code}" "$1"
