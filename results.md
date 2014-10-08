# RESULTS

## Global Temperature Anomaly

Below references to the results of ZONTEM refer to the output of the
software package described in this report. References to the
results of GISTEMP refer to the output of the software package
ccc-gistemp [BARNESJONES2011]; this is not the software that
GISS use to produce their GISTEMP series, but the method and
results are identical.

[figure-compare] shows the annually resolved temperature change
computed by ZONTEM, and, for comparison, the GISTEMP series using
only meteorological stations [HANSENLEBEDEFF1987].

[table-compare] shows the trend obtained by fitting a linear
model to the most recent 30 years. The GISTEMP and ZONTEM
series have the same trend (differences in trends are far smaller
than differences explained by noise).
The errors in estimating the trend are more likely than
not smaller for GISTEMP than for ZONTEM. This is to be expected
from its more sophisticated treatment of what is essentially
the same input data. In estimating errors, I have not
accounted for autocorrelation even though an estimate of the
autocorrelation structure of the residuals from the fit marginally
suggests that an AR(1) model might be appropriate. The effect of this
would be to reduce the degrees of freedom, and hence increase the
estimated errors in trend.  Since ZONTEM is no more than a sketch,
I have chosen the simpler model, but with the caveat that the errors
are more likely than not underestimated. I encourage curious modellers
to torture the data with increasingly elaborate models.

At the time of preparing this report, ZONTEM has 1998 as the
warmest year (highest anomaly). Record years are not particular
stable features of annually resolved analyses of global
temperature change. Minor changes to methods, the receipt of
delayed data for a meteorological station, or improved metadata,
are among the kinds of changes that can shift a particular
year's anomaly value by a few hundredths of a Kelvin which could
be enough to move it up or down the ranking.
For example, CRUTEM3 [BROHANETAL2006] also has 1998 as the
warmest year, but CRUTEM4 [JONESETAL2010] does not.

## Code Size

[table-code] shows the code size (source lines of code) for the
implementations of ZONTEM, ccc-gistemp, and GISS GISTEMP.
Comparisons of code size are complicated by a number of factors:
What code should be included (for example, code that generates plots
should probably not be included)? What lines should be included
(comments, blank lines)? Are some lines worth more than others?
Those issues aside, it is clear that the code for ZONTEM is far smaller
than either ccc-gistemp or GISS GISTEMP.

The implementation of ZONTEM is simpler than ccc-gistemp and GISS
GISTEMP and this is reflected in its smaller code size. The
implementation is simpler because the method is simpler (and
partly because ZONTEM is a "clean room" implementation, produced
by a single worker in a relatively short span of time,
unconstrained by history).
