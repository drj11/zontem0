#!/bin/sh

set -e

reticule_path=$(printf '<path d="M 0 %d h 720" />\\\n' $(seq 0 18 360))

zone_text=$(
  for i in $(seq 0 19)
  do
      printf '<text alignment-baseline="middle" font-size="12.0" x="300" y="'$(expr 351 - $i \* 18)'">Zone '"$i"'</text>\\\n' "$i"
  done
)

~/shptosvg/code/tosvg.py --transform=eqarea ~/.local/share/data/ne_110m_land/*.shp |
  sed '$i\
<g class="reticule">\
'"$reticule_path"'
</g>\
<g class="zone-label">\
'"$zone_text"'
</g>
/^ *<style/a\
g.reticule { stroke: white; stroke-width: 1.4; }
' > figure-map.svg
