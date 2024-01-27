#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Podaj dokładnie dwa napisy jako argumenty."
  exit 1
fi

napis1=$1
napis2=$2

echo "Długość napisu '$napis1': ${#napis1} znaków"
echo "Długość napisu '$napis2': ${#napis2} znaków"

if [ "$napis1" \> "$napis2" ]; then
  echo "Napis '$napis1' jest dłuższy od napisu '$napis2'."
elif [ "$napis1" \< "$napis2" ]; then
  echo "Napis '$napis1' jest krótszy od napisu '$napis2'."
else
  echo "Napisy '$napis1' i '$napis2' mają taką samą długość."
fi
