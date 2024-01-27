#!/bin/bash

if [ "$#" -eq 0 ]; then
  echo "Podaj co najmniej jeden argument."
  exit 1
fi

args=("$@")

echo "Argumenty w odwrotnej kolejności:"
for (( i=${#args[@]}-1; i>=0; i-- )); do
  echo "${args[i]}"
done
