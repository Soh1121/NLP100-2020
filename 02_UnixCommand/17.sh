#!/bin/bash

diff <(cut -f 1 -d $'\t' popular-names.txt | sort | uniq) <(python 17.py)
