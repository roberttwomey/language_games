#!/bin/bash
for ((i=0; i<10;i+=1)); do
	python mutate.py $1
done
