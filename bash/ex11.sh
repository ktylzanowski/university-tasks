#!/bin/bash

find "$1" -type f -exec du -b {} + | awk '{total += $1} END {print total}'
