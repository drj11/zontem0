## Why GISTEMP?

Of the commonly available instrumental estimates of temperature change,
the GISTEMP meteorological station analysis is the most appropriate for
comparison for several reasons: no ocean data, zonal scheme, reference
station method. Ocean data improves coverage, but comes with
data homogenisation issues of their own [HANSENETAL1996].
For simplicity's sake ZONTEM uses only
metereological station data; a comparison with a dataset that
combines metereological station data with ocean data wouldn't be
a meaningful comparison in this context.

The zonal scheme used by GISTEMP [HANSENETAL2006] is similar to
the zonal scheme used by ZONTEM. In GISTEMP hemispheric and
global averages are computed from zonal averages weighted by the
area of the zone, which avoids giving too much weight to zones
that are well-endowed with stations. Mitchell, 1963, discusses a
similar approach, but other analyses of global temperature
change do not generally incorporate this zonal idea. I encourage
the curious to produce their own comparisons of ZONTEM and other
analyses of global temperature change.

ZONTEM uses the Reference Station
Method [HANSENLEBEDEFF1987] to combine data from several
metereological stations. I expect the method used to combine stations
to only make a small difference to global trends [VOSEETAL2005],
and again I encourage the curious to modify ZONTEM to use a
different method of combining stations.

## Station Density

[figure-popcount-s] shows, separately for each of the 10 zones in
the Southern hemisphere, the number of stations contributing to each
month. The gross features of this station-count graph are discussed in
[LAWRIMOREETAL2011]. Compared to the Northern hemisphere, the Southern
hemisphere has far fewer stations, and those stations are generally
established later. Data is particularly sparse in the Southernmost
zones. Zone 1 (53°S to 64°S) has no stations until the first decade of
the 1900s when Base Orcadas, WMO 88968, was established and Grytviken,
WMO 88903, was settled.  Zone 0 (64°S to 90°S) has no stations until
the 1940s when Faraday, now Vernadsky, WMO 89063, was settled and a
station identified as WMO 89062 and named Rothera starts reporting.
The station record for WMO 89062 in GHCN-M deserves further attention as
Rothera Research Station was not established until 1975.

The reliance on a very small number of stations for certain
regions and decadal periods is unfortunate, but indicates the
importance of careful reconstruction and correction for even
individual stations, such as that undertaken by Bromwich et al
for Byrd station [BROMWICHETAL2013]. Bromwich's Byrd record has not
been used in ZONTEM because for simplicity only a single source,
GHCN-M, is used. I encourage the curious to perform their own
experiment, changing ZONTEM to incorporate the record into the
analysis.

## Data Utilisation

The Reference Station Method has advantages over the Climate
Anomaly Method in being able to make use of meteorological station
data when the station has no data in a particular reference period
[HANSENLEBEDEFF1987]. ZONTEM, because it combines all stations in a
zone, is able to make use of a large fraction of the data available
in GHCN-M. ZONTEM makes uses of all meteorological stations that
have at least 20 years of data (since 1880).

ZONTEM is simplified by only having to deal with one record for
each station. GHCN-M v2 published several, possibly overlapping
and different, records for station, called *duplicates*. In
GHCN-M v3, duplicates are combined so that only one record is
published for each station [LAWRIMOREETAL2011]. Other workers,
using GHCN-M v2 or more diverse data sources, have had to
develop their own procedures for handling duplicates
[HANSENETAL1999] [ROHDEETAL2013] [JONESETAL2010]. I agree with
Lawrimore's concluding remarks: "The removal of
station duplicates has greatly simplified the use of the data
set by removing a feature that created confusion and kept
some users from gaining full use of the data set." [LAWRIMOREETAL2011]
