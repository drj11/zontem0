#!/usr/bin/env python3

"""
Convert CSV file from Zontem to .dat format.
"""

import csv
import os
import re

HOME = os.path.expanduser("~")

def to_dat(zontem_f, out):
    zontem = csv.reader(zontem_f)
    zontem_data = [row for row in zontem if re.match(r'[0-9]{4}', row[0])]

    columns = list(zip(*zontem_data))
    years = columns[0]
    for i, series in enumerate(columns[1:]):
        if i == 0:
            id = "zontemglobe"
        else:
            id = "zontemzon{:02d}".format(i-1)
        for year, value in zip(years, series):
            months = "{}  f".format(convert1(value)) * 12
            out.write("{}{}TAVG{}\n".format(id, year, months))

def convert1(v):
    """
    Convert decimal string to 5 character GHCN-M value.
    """

    try:
        x = float(v)
    except ValueError:
        return "-9999"
    return "{:5.0f}".format(x*100)

def main(argv=None):
    import getopt
    import glob
    import sys

    if argv is None:
        argv = sys.argv

    opt, arg = getopt.getopt(argv[1:], '', ['zontem='])
    assert not arg
    zontem_csv = None
    for o, v in opt:
        if o == '--zontem':
            zontem_csv = v

    if zontem_csv is None:
        zontem_dir = os.path.join(HOME, "zontem")
        zontem_csv = sorted(glob.glob(os.path.join(
          zontem_dir, "output", "*ghcnm*.csv")))[-1]

    with open(zontem_csv) as f:
        with open(os.path.join("result", "zontem.dat"), "w") as dat:
            to_dat(f, dat)

if __name__ == '__main__':
    main()
