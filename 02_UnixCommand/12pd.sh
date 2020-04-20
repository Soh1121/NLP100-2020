#!/bin/bash

diff output/col1pd.txt <(cut -f 1 -d $'\t' popular-names.txt)
diff output/col2pd.txt <(cut -f 2 -d $'\t' popular-names.txt)
