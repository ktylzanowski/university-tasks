#!/bin/bash

trap 'echo "Jestem nieśmiertelny."' SIGINT

handle_sighup() {
  trap '' SIGINT
  echo "Przestałem reagować na SIGINT."
}

trap 'handle_sighup' SIGHUP

while true; do
  sleep 1
done
