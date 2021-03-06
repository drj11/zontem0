#!/bin/sh

# Temperature Anomalies for all zones.

offset=$(seq 0 19 | paste -s -d, -)
zones=$(printf 'zontemzon%02d\n' $(seq 0 19))

~/ghcntool/stationplot.py -o result/figure-zones.svg --title "Zonal Temperature Anomalies" -d result/zontem.dat -y --offset "$offset" -c legend=none -c yscale=20 -c ytick=2 $zones
