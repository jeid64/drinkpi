#!/bin/bash
echo -e '\x55' > /sys/bus/w1/devices/$1/rw
