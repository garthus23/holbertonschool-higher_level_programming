#!/bin/bash
# curl catch me
curl -s 0.0.0.0:5000/catch_me | head -n 1 | sed -e 's/.*/You got me!/'
