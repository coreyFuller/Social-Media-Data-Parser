#!/usr/bin/env bash

echo 'starting script....'
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SRC="$(dirname $DIR)"
cd $SRC
for FILE in *py; do python3 $FILE; done
