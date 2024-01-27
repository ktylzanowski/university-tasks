#!/bin/bash

BUFFER_CAPACITY=3
FIRST_PLACE="first_place"
SECOND_PLACE="second_place"
BUFFER="buffer"

simulate_crane1() {
    count=0
    for file in "$FIRST_PLACE"/*; do
        if [ "$count" -lt "$BUFFER_CAPACITY" ]; then
            mv "$file" "$BUFFER/"
            echo "Crane 1 moved $file to buffer."
            ((count++))
        else
            echo "Buffer is full. Crane 1 waiting."
            sleep 1
        fi
    done
    echo "Crane 1 finished. Moved $count files to buffer."
    exit $count
}

simulate_crane2() {
    count=0
    while [ "$(ls -A $BUFFER)" ]; do
        file=$(ls "$BUFFER" | head -n 1)
        mv "$BUFFER/$file" "$SECOND_PLACE/"
        echo "Crane 2 moved $file to second place."
        ((count++))
    done
    echo "Crane 2 finished. Moved $count files to second place."
    exit $count
}


supervisor() {
    echo "Supervisor started."

    trap "start_cranes" USR1

    trap "stop_cranes" SIGINT

    while true; do
        sleep 1
    done
}


start_cranes() {
    echo "Cranes started."

    simulate_crane1 &

    simulate_crane2 &

    wait

    echo "Cranes finished."
    exit
}

stop_cranes() {
    echo "Received SIGINT. Stopping cranes."
    pkill -P $$  # Zabij procesy potomne
    exit
}

mkdir -p "$FIRST_PLACE" "$SECOND_PLACE" "$BUFFER"

touch "$FIRST_PLACE"/file{1..10}

supervisor
