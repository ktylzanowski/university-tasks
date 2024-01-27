#!/bin/bash

./script3.sh $1 $2 $3 &
pid=$!

wait $pid
result=$?

if [ $result -eq 1 ]; then
	echo "true"
else
	echo "false"
fi

exit 1
