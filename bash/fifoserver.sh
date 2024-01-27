#!/bin/bash

fifo_path="myfifo"
mkfifo "$fifo_path"

while true; do
  read -r word < "$fifo_path"
  vowels_count=$(echo "$word" | tr -cdaeiouAEIOU | wc -c)
  echo "Serwer: Słowo '$word' zawiera $vowels_count samogłosek." > "$fifo_path"
done
