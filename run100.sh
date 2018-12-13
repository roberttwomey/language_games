#!/bin/bash
for ((i=0; i<100;i+=1)); do
	python mutate.py $1
done
