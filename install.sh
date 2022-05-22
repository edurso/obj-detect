#!/bin/sh
# Usage: ./deploy.sh [remote username] [remote ip]

if [ -z "$1" ] || [ -z "$2" ] ; then
    echo "No command line arguments given"
    echo "Defaulting connection to lightning@10.8.62.3"
	ssh lightning@10.8.62.3 "sudo bash -s" < ./scripts/setup.sh
else
    echo "Connecting to $1@$2"
	ssh ${1}@${2} "sudo bash -s" < ./scripts/setup.sh
fi
