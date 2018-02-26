#!/usr/bin/env bash

docker build -t task1_check ./check
docker run -i --network=task1_default task1_check
