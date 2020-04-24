#!/bin/bash

cut -f 1 -d $'\t' popular-names.txt | sort | uniq -c | sort -k 1 -n -r
