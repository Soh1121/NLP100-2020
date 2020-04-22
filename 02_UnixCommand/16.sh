#!/bin/bash

SH="sh_"
PY="py_"
HEAD="split_file_"

if [ $# -ne 1 ]; then
  echo "指定された引数は$#個です。" 1>&2
  echo "実行するには数字を1個引数に指定してください。" 1>&2
  exit 1
fi

split -l $1 popular-names.txt ./output/16/$SH$HEAD

for i in a b c d e f g h i j k l m n o p q r s t u v w x y z
do
  for j in a b c d e f g h i j k l m n o p q r s t u v w x y z
  do
    ADDRESS="./output/16/"
    SHFILE=$ADDRESS$SH$HEAD$i$j
    PYFILE=$ADDRESS$PY$HEAD$i$j
    if [ -e $SHFILE -a -e $PYFILE ]; then
      diff $SHFILE $PYFILE
    fi
  done
done
