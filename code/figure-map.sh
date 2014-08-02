#!/bin/sh

set -e

reticule_path=$(printf '<path d="M 0 %d h 720" />\\\n' $(seq 18 18 359))

zone_text=$(
  # Find the number of stations used in each Zone...
  grep -v 000000000000 ~/zontem/log/zontem.log |
    grep -n LONGEST |
    awk -F: 'l{print $1-l};{l=$1}' |
  # And pipe it into this loop that prints Zone labels.
  for i in $(seq 0 19)
  do
      y=$(expr 351 - $i \* 18)
      read n_stations
      z=$(printf 'Zone %2d' "$i")
      n=$(printf '%4d stations' "$n_stations")
      printf '<text alignment-baseline="middle" font-size="12.0" x="292" y="'$y'">%s</text><text text-anchor="end" alignment-baseline="middle" font-size="12.0" x="550" y="'$y'">%s</text>\\\n' "$z" "$n"
  done
)

~/shptosvg/code/tosvg.py --transform=eqarea ~/.local/share/data/ne_110m_land/*.shp |
  sed 's/olive/#aaa/
$i\
<g class="reticule">\
'"$reticule_path"'
</g>\
<g class="zone-label">\
'"$zone_text"'
</g>
/^ *<style/a\
g.reticule { stroke: white; stroke-width: 1.4; }
' > figure-map.svg
