#!/bin/bash

odwroc_napis() {
  local napis=$1
  local odwrocony=""
  
  for (( i=${#napis}-1; i>=0; i-- )); do
    odwrocony="${odwrocony}${napis:i:1}"
  done
  
  echo "$odwrocony"
}

if [ "$#" -eq 0 ]; then
  echo "Podaj napis do odwrócenia jako argument."
  exit 1
fi

napis_do_odwrocenia=$1

wynik=$(odwroc_napis "$napis_do_odwrocenia")
echo "Odwrocony napis: $wynik"
