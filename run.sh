#!/bin/sh
export VIKINGHOME=$HOME/code/vikinghome
cd ${VIKINGHOME}/
if [ -f env/bin/activate ]; then
  source env/bin/activate
fi
exec python src/main.py 2>&1 >${VIKINGHOME}/vikinghome.log
