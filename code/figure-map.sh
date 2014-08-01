#!/bin/sh

set -e
reticule_path=$(printf '<path d="M 0 %d h 720" />\\\n' $(seq 0 18 360))

~/shptosvg/code/tosvg.py --transform=eqarea ~/.local/share/data/ne_110m_land/*.shp |
  sed '$i\
<g class="reticule">\
'"$reticule_path"'
</g>
/^ *<style/a\
g.reticule { stroke: white; stroke-width: 1.4; }
' > figure-map.svg
