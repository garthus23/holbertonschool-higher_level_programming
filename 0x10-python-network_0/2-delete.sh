#!/bin/bash
# del request curl
curl "$1" --data "selection=filename&action=delete"
