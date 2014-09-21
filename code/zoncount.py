#!/usr/bin/env python3

import os
import sys

from collections import defaultdict

def stations_used(inp):
    used = defaultdict(lambda: (None,[]))
    zone = -1
    for line in inp:
        action, id, combined = line.split()
        if action == "LONGEST":
            zone += 1
            if zone >= 20:
                break
        months_used = [i for i,c in enumerate(combined) if c == "1"]
        used[id] = (zone, months_used)

    return used

def count_ghcn(dat, used):
    """
    Returns a count structure which is a list of dicts, one for
    each zone. The dict maps from year (a string) to a
    12-element array of counts for each month.
    """
    count = [defaultdict(lambda:[0]*12) for i in range(20)]
    for row in dat:
        id = row[:11]
        year = row[11:15]
        zone, months = used[id]
        for m in months:
            v = row[19+8*m:24+8*m]
            if v != '-9999':
                count[zone][year][m] += 1
    return count

def count_to_v3(count, out):
    """
    `count` is as returned from `count_ghcn()`.  They are output
    as a file in GHCN-M v3 format.
    """

    for z,d in enumerate(count):
        id = "zontemzon{:02d}".format(z)
        for year,months in sorted(d.items()):
            MONTHS_FORMAT = "{:5d}   " * 12
            formatted_counts = MONTHS_FORMAT.format(*months)
            out.write("{}{}STAT{}\n".format(id, year, formatted_counts))
               

def main(argv=None):
    if argv is None:
        argv = sys.argv

    used = stations_used(
      open(os.path.expanduser("~/zontem/log/zontem.log")))
    count = count_ghcn(open("/home/drj/zontem/input/ghcnm.v3.2.2.20140611/ghcnm.tavg.v3.2.2.20140611.qca.dat"),
      used)
    with open(os.path.join("result", "zoncount.dat"), 'w') as out:
        count_to_v3(count, out)

if __name__ == '__main__':
    main()

