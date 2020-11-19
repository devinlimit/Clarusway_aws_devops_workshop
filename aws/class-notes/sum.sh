#!/bin/bash

for i in {1..100}
do
	echo "$i+=$i"

done
let "sum=i/100"
echo "$sum"
