#!/usr/bin/env bash

i=0
while [ "$i" -lt 1000 ]
do
    echo "$RANDOM" >> file1.txt
    i=$((i+1))
done
