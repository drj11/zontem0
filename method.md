# Method

I have participated in ccc-gistemp, a project to create a clearer
reconstruction of GISTEMP [BARNESJONES2011]. ZONTEM is similar
in spirit, but without the constraint of exactly matching
GISTEMP's algorithm. The aim of ZONTEM is to be as simple as
possible while giving a reasonable result.

Input data is taken from the Global Historical Climate Network--Monthly
version 3 [LAWRIMOREETAL2011] (GHCN-M v3 hereafter). The traditional
analysis is of adjusted monthly mean temperature, but it is also
possible to use unadjusted data, and also to analyse minimum or
maximum temperatures.

The input is a number of records, each record being a
time series of monthly (air) temperature averages from a single
station. In the usual analysis, only data since 1880 are used
(and stations that do not have data since 1880 are not used).

The input records are distributed into N (=20 by default) zones
according to the latitude of the station (stations in GHCN-M
v3 are provided with basic metadata that includes latitude and
longitude). Each zone represents the surface of the globe between
two circles of latitude; each zone covers an equal area. [figure-map]
shows the 20 zones on a map of Earth.

All the station records in a zone are combined into one record using
Hansen's Reference Station Method [HANSEN1987], giving each
station an equal weighting. Records are combined by starting
with the longest record and attempting to combine the other
records in order of decreasing length (and where records are of
equal length, in the order that they appear in the input). In
order to be combined, a station needs 20 valid data for any
particular calendar month. Each of the 12 calendar months are
processed separately at this stage.

All the zone records are combined into a single global record using the
same method. Each zone is weighted equally; since all the zones
have equal area, this is equivalent to weighting each zone by
its area.

The global record, which is a monthly series at this stage, is
converted to annual anomalies in a simple 2 step process: it is first
converted to monthly anomalies by subtracting from each datum
the series average value for that calendar month; yearly
anomalies are formed by averaging the 12 monthly anomalies for
each year (only years with 12 valid monthly anomalies form an average
yearly anomaly, but with the usual input all years except the current
have 12 valid monthly anomalies).

The result is a global annual anomaly series. It is output as a
CSV [SHAFRANOVICH2005] file, and is hence importable into many
software packages such as R, Python, OpenOffice, and so on. As a
convenience the annual series for each zone is also output.
These zonal series are not meant to be representative of the zones for
which they are computed, the monthly series are merely used as an
intermediate step in calculating the global series, and the
annual series are a useful diagnostic. I urge caution when using
the zonal series directly.
