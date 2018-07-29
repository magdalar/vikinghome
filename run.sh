#!/bin/sh
export VIKINGHOME=$HOME/code/vikinghome
cd ${VIKINGHOME}/src/
if [ -f env/bin/activate ]; then
  source env/bin/activate
fi
exec python main.py &>${VIKINGHOME}/vikinghome.log
