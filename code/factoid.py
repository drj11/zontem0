#!/usr/bin/env python3

import json
import os
import re
import sys

n_stations = 0
n_fractions = 0

for line in open(os.path.expanduser("~/zontem/log/zontem.log")):
    record = line.split()
    if re.match(r'\d{11}', record[1]):
        fractions = record[2].count("1")
        n_fractions += fractions
        if fractions > 0:
            n_stations += 1

json.dump(dict(n_stations=n_stations, n_fractions=n_fractions),
  sys.stdout, indent=0)
