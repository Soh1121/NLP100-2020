#!/bin/sh

cat  ./popular-names.txt | sed -e s/$'\t'/' '/g

echo "---"

cat ./popular-names.txt | tr '\t' ' '

echo "---"

expand -t 1 popular-names.txt
