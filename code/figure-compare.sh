#!/bin/sh
~/ghcntool/stationplot.py -o result/figure-compare.svg --title "Global Temperature Change" -c ytick=0.2 -c yscale=200 -y -d result/crutem4.dat CRUTEM4GLOB -d result/ccc-gistemp.dat ccc-gistemp -d result/zontem.dat zontemglobe
