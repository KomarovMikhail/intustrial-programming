#!/usr/bin/env bash

docker-compose build
docker-compose up -d postgres rabbitmq

sleep 10

docker-compose up consumer
