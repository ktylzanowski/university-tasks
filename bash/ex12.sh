#!/bin/bash

folder="$1"
uzytkownik=$(whoami)
data=$(date +"%Y%m%d")

mkdir -p ~/backups

find "$folder" -type f -name "*.txt" -exec tar -rvf ~/backups/"$uzytkownik"_backup_data_"$data".tar {} +
