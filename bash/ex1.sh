#!/bin/bash

if [ "$#" -ne 3 ]; then
  echo "Podaj dokładnie trzy liczby jako argumenty."
  exit 1
fi

liczba1=$1
liczba2=$2
liczba3=$3

suma=$((liczba1 + liczba2 + liczba3))

echo "Suma liczb $liczba1, $liczba2 i $liczba3 wynosi: $suma"
