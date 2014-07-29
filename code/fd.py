#!/usr/bin/env python3

"""
A first difference (ASCII) chart.

Show for each year, when a zone was warmer (+) or colder (-)
than the previous year. The margin figures give the number of
zones in each hemisphere that match the majority sign.
"""

import csv
import glob
import os
import sys

def fd(inp):
    rows = csv.reader(inp)
    next(rows)
    all_columns = list(zip(*rows))
    all_series = all_columns[2:]
    all_years = all_columns[0]
    all_fd = [first_difference_one(series) for series in all_series]
    all_simple = [simplify(series) for series in all_fd]
    for year,data in zip(all_years[1:], zip(*all_simple)):
        margin = []
        for hemi in (data[:10],data[10:]):
            count = None
            plusses = hemi.count('+')
            minusses = hemi.count('-')
            if plusses == minusses:
                match = '  '
            else:
                match = "{:2d}".format(max(plusses, minusses))
            margin.append(match)
        print(year, margin[0] + ' ' + "".join(data) + ' ' + margin[1])

def first_difference_one(series):
    series = list(series)
    for a, b in zip(series, series[1:]):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            yield None
        else:
            yield b-a

def simplify(series):
    for v in series:
        if v is None:
            yield ' '
        elif v > 0:
            yield '+'
        elif v == 0:
            yield '0'
        else:
            yield '-'

def main(argv=None):
    if argv is None:
        argv = sys.argv

    pattern = os.path.expanduser("~/zontem/output/Zontem-ghcnm*.csv")
    filename = sorted(glob.glob(pattern))[-1]
    fd(open(filename))

if __name__ == '__main__':
    main()
