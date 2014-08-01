#!/usr/bin/env python3

import os
import urllib.request

URL = "http://www.metoffice.gov.uk/hadobs/crutem4/data/diagnostics/global/nh+sh/CRUTEM.4.2.0.0.global_n+s"

DATA_DIR = os.path.expanduser("~/.local/share/data/crutem4")

def fetch(url):
    response = urllib.request.urlopen(url)
    if response.getcode() != 200:
        raise Exception("status = {}".format(response.getcode()))
    try:
        dir = DATA_DIR
        os.makedirs(dir)
    except OSError:
        # Assume that the "error" is that the directories already exist.
        pass
    with open(os.path.join(dir, os.path.basename(url)), 'wb') as out:
        while True:
            s = response.read(9999)
            if not s:
                break
            out.write(s)

def dat(out):
    data_filename = os.path.join(DATA_DIR, os.path.basename(URL))
    id = "CRUTEM4GLOB"
    with open(data_filename) as inp:
        for row in inp:
            year, anomaly = row.split()[:2]
            anomaly = float(anomaly)
            months = "{:5.0f}  f".format(anomaly * 100) * 12
            out.write("{}{}TAVG{}\n".format(id, year, months))

def main():
    fetch(URL)
    with open("crutem4.dat", 'w') as out:
        dat(out)

if __name__ == '__main__':
    main()
