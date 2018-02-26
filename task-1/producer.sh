#!/usr/bin/env bash

docker build -t task-1-producer ./producer
docker run -i --network=task1_default task-1-producer
