#!/bin/bash
docker rm -f feedback
docker build -t feedback .
docker run --name=feedback --rm -p5000:5000 -it feedback
