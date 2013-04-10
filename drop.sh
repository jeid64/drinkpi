#!/bin/bash
SLOT=$1
echo -e '\x55' > /sys/bus/w1/devices/$SLOT/rw && sleep 1 && echo -e '\x55' > /sys/bus/w1/devices/$SLOT/rw 
