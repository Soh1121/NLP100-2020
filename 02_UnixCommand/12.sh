#!/bin/bash

diff output/col1.txt <(cut -f 1 -d $'\t' popular-names.txt)
diff output/col2.txt <(cut -f 2 -d $'\t' popular-names.txt)
