#!/bin/bash

sudo docker run -itd --name ${1} --restart=always -p ${2}:80 --shm-size=${3} --security-opt seccomp=unconfined tiryoh/ros2-desktop-vnc:humble 

