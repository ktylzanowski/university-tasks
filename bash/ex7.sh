#!/bin/bash

if [ "$#" -eq 0 ]; then
  echo "Brakuje argumentu. Podaj ścieżkę do pliku."
  exit 1
fi

sciezka_do_pliku=$1

rozszerzenie="${sciezka_do_pliku##*.}"

case "$rozszerzenie" in
  "txt")
    echo "Otwieranie pliku $sciezka_do_pliku w edytorze tekstu..."
    xdg-open "$sciezka_do_pliku" || open "$sciezka_do_pliku"
    ;;
  "sh")
    echo "Uruchamianie skryptu $sciezka_do_pliku..."
    bash "$sciezka_do_pliku"
    ;;
  *)
    echo "Plik $sciezka_do_pliku jest nieznany."
    ;;
esac
