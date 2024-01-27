#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Podaj podsłowo jako argument."
  exit 1
fi

podslowo=$1

liczba_plikow=$(find / -maxdepth 1 -type f -name "*$podslowo*" | wc -l)
liczba_katalogow=$(find / -maxdepth 1 -type d -name "*$podslowo*" | wc -l)

echo "Liczba plików z podsłowem '$podslowo': $liczba_plikow"
echo "Liczba katalogów z podsłowem '$podslowo': $liczba_katalogow"
