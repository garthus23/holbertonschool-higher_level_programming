#!/bin/bash
# Header var post
curl -s -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" -X POST "$1"
