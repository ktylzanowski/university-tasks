#!/bin/bash

if [ "$#" -eq 0 ]; then
  echo "Podaj login osoby, której ścieżkę do pliku terminala chcesz sprawdzić."
  exit 1
fi

login=$1

sciezka_terminala=$(getent passwd "$login" | cut -d: -f7)

if [ -z "$sciezka_terminala" ]; then
  echo "Użytkownik o loginie $login nie istnieje."
  exit 1
fi

echo "Ścieżka do pliku terminala użytkownika $login: $sciezka_terminala"
