#!/bin/bash

if [ $# -ne 1 ]; then
  echo "指定された引数は$#個です。" 1>&2
  echo "実行するには数字を1個引数に指定してください。" 1>&2
  exit 1
fi

diff <(head -n $1 popular-names.txt) <(python 14.py)
