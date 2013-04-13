#!/bin/bash
SLOT=$1
echo -ne '\x55' > /sys/bus/w1/devices/$SLOT/rw && sleep 2 && echo -ne '\xf0' > /sys/bus/w1/devices/$SLOT/rw 

