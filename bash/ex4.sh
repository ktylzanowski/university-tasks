#!/bin/bash

katalog_domowy=~

dzis=$(date +"%Y-%m-%d")

nowy_katalog="$katalog_domowy/$dzis"
mkdir -p "$nowy_katalog"

find "$katalog_domowy" -maxdepth 1 -type f -newermt "$dzis" -exec cp {} "$nowy_katalog" \;

echo "Utworzono katalog $nowy_katalog i skopiowano pliki utworzone dzisiaj do tego katalogu."
