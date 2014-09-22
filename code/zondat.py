#!/usr/bin/env python3

"""
Convert CSV file from Zontem to .dat format.
"""

import csv
import os
import re

HOME = os.path.expanduser("~")

def to_dat(zontem_dir=os.path.join(HOME, "zontem")):
    import glob

    zontem_csv = sorted(glob.glob(os.path.join(
      zontem_dir, "output", "*ghcnm*.csv")))[-1]

    with open(zontem_csv) as zontem_f:
        zontem = csv.reader(zontem_f)
        zontem_data = [row for row in zontem if re.match(r'[0-9]{4}', row[0])]
        zontem_dict = dict((row[0], row) for row in zontem_data)

        with open(os.path.join("result", "zontem.dat"), "w") as dat:
            columns = list(zip(*zontem_data))
            years = columns[0]
            for i, series in enumerate(columns[1:]):
                if i == 0:
                    id = "zontemglobe"
                else:
                    id = "zontemzon{:02d}".format(i-1)
                for year, value in zip(years, series):
                    months = "{}  f".format(convert1(value)) * 12
                    dat.write("{}{}TAVG{}\n".format(id, year, months))

def convert1(v):
    """
    Convert decimal string to 5 character GHCN-M value.
    """

    try:
        x = float(v)
    except ValueError:
        return "-9999"
    return "{:5.0f}".format(x*100)

to_dat()
