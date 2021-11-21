#!/bin/bash

NAME="tfod-api"
FILEPATH="/tensorflow/workspace"
JETSON_IMAGE="edurs0/tfod-wkspc:latest-jetson"

sudo docker run \
    -it \
    --rm \
    --runtime nvidia \
    --network host \
    --name $NAME \
    -p 8888:8888 \
    -p 6006:6006 \
    -v $FILEPATH:/tensorflow/workspace \
    $JETSON_IMAGE
