#!/bin/bash
#  Docker healthcheck.  Ensures our server is working.
#  https://docs.docker.com/compose/compose-file/#healthcheck
curl -f http://0.0.0.0 || exit 1
