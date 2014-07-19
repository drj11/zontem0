#!/usr/bin/env python3

"""
Combine CSV files from Zontem and ccc-gistemp to
make a CSV file that allows both annual series to be plotted.
"""

import csv
import os
import re

HOME = os.path.expanduser("~")

def join(zontem_dir=os.path.join(HOME, "zontem"),
  gistemp_dir=os.path.join(HOME, "ccc-gistemp")):
    import glob

    zontem_csv = sorted(glob.glob(os.path.join(
      zontem_dir, "output", "*ghcnm*.csv")))[-1]
    gistemp_csv = os.path.join(
      gistemp_dir, "result", "landGLB.Ts.ho2.GHCN.CL.PA.csv")

    with open(gistemp_csv) as gistemp_f, open(zontem_csv) as zontem_f:
        gistemp = csv.reader(gistemp_f)
        zontem = csv.reader(zontem_f)
        gistemp_data = [row for row in gistemp if re.match(r'[0-9]{4}', row[0])]
        zontem_data = [row for row in zontem if re.match(r'[0-9]{4}', row[0])]
        gistemp_dict = dict((row[0], row) for row in gistemp_data)
        zontem_dict = dict((row[0], row) for row in zontem_data)

        years = sorted(set(gistemp_dict) & set(zontem_dict))
        # The ZONTEM annual data.
        zontem_annual = [zontem_dict[year][1] for year in years]
        # The GISTEMP annual data.
        gistemp_annual = [gistemp_dict[year][13] for year in years]

        with open("compare_zontem_gistemp.csv", "w") as out:
            csv_out = csv.writer(out)
            csv_out.writerow(["Year", os.path.basename(zontem_csv), os.path.basename(gistemp_csv)])
            for year,zontem_v,gistemp_v in zip(
              years, zontem_annual, gistemp_annual):
                csv_out.writerow([year, zontem_v, gistemp_v])

        with open("compare_zontem_gistemp.dat", "w") as dat:
            for id,values in [('zontem_____', zontem_annual),
              ('ccc-gistemp', gistemp_annual)]:
                for year, value in zip(years, values):
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

join()
