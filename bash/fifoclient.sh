#!/bin/bash

fifo_path="myfifo_client"
mkfifo "$fifo_path"

echo "Podaj słowo:"
read -r word

echo "$fifo_path" > myfifo
echo "$word" > "$fifo_path"

response=$(cat "$fifo_path")
echo "Klient: $response"

rm "$fifo_path"
