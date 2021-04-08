#!/bin/bash
# count bytes of webpage
curl -s "$1" | wc -c
