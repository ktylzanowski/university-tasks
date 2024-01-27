#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Podaj dokładnie jedną ścieżkę do pliku lub katalogu jako argument."
  exit 1
fi

sciezka=$1

if [ ! -e "$sciezka" ]; then
  echo "Podana ścieżka nie istnieje."
  exit 1
fi

echo "Informacje o ścieżce: $sciezka"
echo "Typ: $(file -b "$sciezka")"

echo "Prawa dostępu użytkownika do $sciezka:"
if [ -r "$sciezka" ]; then
  echo "Odczyt: Tak"
else
  echo "Odczyt: Nie"
fi

if [ -w "$sciezka" ]; then
  echo "Zapis: Tak"
else
  echo "Zapis: Nie"
fi

if [ -x "$sciezka" ]; then
  echo "Wykonanie: Tak"
else
  echo "Wykonanie: Nie"
fi
