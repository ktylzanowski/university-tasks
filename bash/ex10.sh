#!/bin/bash

echo "scale=0; (${@// /+}) / $#" | bc
