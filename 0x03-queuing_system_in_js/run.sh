#!/usr/bin/bash

curl localhost:1245/reserve_seat ; echo ""
curl localhost:1245/available_seats ; echo "" 
curl localhost:1245/process ; echo ""
curl localhost:1245/available_seats ; echo "" 
