#!/bin/sh

# Population Count for Southern Hemisphere.

~/ghcntool/stationplot.py --offset 0,1,2,3,4,5,6,7,8,9 -d zoncount.dat -s 1 -c ylabel="Station Count" -c ytick=20 -c yscale=1 $(for i in $(seq 0 9); do printf 'zontemzon%02d\n' $i; done)
