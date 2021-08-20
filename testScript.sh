#!/bin/bash
x=0
while [ $x -le 25 ]
  do python3 test.py $1 $x
  printf "\n\n"
  x=$(( $x + 1 ))
done