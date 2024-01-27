#!/bin/bash

trap 'echo "Jestes niesmiertelny"' INT

while true; do
	sleep 1
done

trap '' HUP
