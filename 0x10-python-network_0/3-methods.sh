#!/bin/bash
# get allowed methods
curl -sI "$1" | grep Allow | sed s/"Allow: "//
