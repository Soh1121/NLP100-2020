#!/bin/bash

cat ./output/45.txt | sort | uniq -c | sort -k 1 -n -r | head -n 10 > ./output/45_sort.txt
cat ./output/45.txt | sort | uniq -c | sort -k 1 -n -r | grep -e " 見る\t" -e " する\t" -e " 与える\t" > ./output/45_limit.txt
