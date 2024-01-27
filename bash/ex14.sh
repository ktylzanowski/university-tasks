#!/bin/bash

if [ "$1" -gt 0 ] && [ "$2" -gt 0 ] && [ "$3" -gt 0 ]; then
	exit 1
else
	exit 0
fi
