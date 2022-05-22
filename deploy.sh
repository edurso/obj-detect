#!/bin/sh
# Usage: ./deploy.sh [remote username] [remote ip]

if [ -z "$1" ] || [ -z "$2" ] ; then
    echo "No command line arguments given"
    echo "Defaulting connection to lightning@10.8.62.3"
    rsync -zravP ./vision/ lightning@10.8.62.3:/home/lightning/vision/
    rsync -zravP ./vision/ lightning@10.8.62.3:/home/lightning/bin/
	ssh lightning@10.8.62.3 "sudo bash -s" < ./scripts/build.sh
else
    echo "Connecting to $1 at $2"
    rsync -zravP ./vision/ ${1}@${2}:/home/lightning/vision/
    rsync -zravP ./vision/ ${1}@${2}:/home/lightning/bin/
	ssh ${1}@${2} "sudo bash -s" < ./scripts/build.sh
fi
