#!/bin/bash
# curl catch me
curl -s https://en.wikipedia.org/wiki/You_Got_Me! | head | grep title | sed 's/<title>//' | sed 's/\ -.*//' | sed 's/G/g/' | sed 's/M/m/'
