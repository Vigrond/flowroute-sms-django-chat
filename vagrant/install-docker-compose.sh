#!/bin/bash
#  Copyright (c) 2018 Art & Logic, Inc. All Rights Reserved.
#  Script to install docker-compose
#  Automatically called by Vagrant


sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

docker-compose --version
