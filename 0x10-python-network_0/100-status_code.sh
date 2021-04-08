#!/usr/bin/bash
# get code url
curl -sI "$1" | head -n 1 | cut -d ' ' -f 2
