#!/bin/bash

for F in `ls ../ | sort -n`; do
  if [ "$F" != "gpi" ]; then
    echo `cat ../$F`
  fi
done > scaling.dat

gnuplot scaling.gpi
gnuplot scaling_no_init.gpi
