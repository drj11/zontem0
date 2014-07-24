#!/bin/sh

# Population Count for Southern Hemisphere.

~/ghcntool/stationplot.py -o figure-popcount-s.svg --title "Station Contribution Southern Hemisphere" -d zoncount.dat -s 1 -c ylabel="Station Count" -c ytick=25 -c yscale=1 $(for i in $(seq 0 9); do printf 'zontemzon%02d\n' $i; done)
