#!/bin/bash
SLOT=$1
echo -e '\xf0' > /sys/bus/w1/devices/$SLOT/rw && sleep 1.5 && echo -e '\xf0' > /sys/bus/w1/devices/$SLOT/rw 


