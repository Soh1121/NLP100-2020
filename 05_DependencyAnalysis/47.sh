#!/bin/bash

cut -f 1 -d $'\t' ./output/47.txt | sort | uniq -c | sort -k 1 -n -r | head -n 10 > ./output/47_sort.txt

cut -f 1 -d $'\t' ./output/47.txt > ./output/47-col1.txt
cut -f 2 -d $'\t' ./output/47.txt > ./output/47-col2.txt
paste ./output/47-col1.txt ./output/47-col2.txt > ./output/47-col1-2.txt
cat ./output/47-col1-2.txt | sort | uniq -c | sort -k 1 -n -r | head -n 10 > ./output/47_pattern.txt
