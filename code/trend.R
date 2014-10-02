#!/usr/bin/env Rscript

# rjson is required

library("rjson")

# Read data, removing -9999 as a missing value.
d <- read.fwf('result/zontem.dat', width=c(11, 4, 4, 5, 3))
global.rows <- (d[,1] == 'zontemglobe')
global.data <- d[global.rows,]
global.data <- global.data[global.data[,4] != -9999,]

# Exract the year and anomly for the whole period...
year <- global.data[,2]
anom <- global.data[,4]

# ... and for the most recent 30 years.
s <- length(year)-29
e <- length(year)
year.30 <- year[s:e]
anom.30 <- anom[s:e]

# Fit linear model to each period.
fit.all <- lm(anom~year)
fit.30 <- lm(anom.30~year.30)

# fit should be a model fit returned by lm
# returns the trend and the error in a list with names
# "trend" and "trend.error". Assumes the relevant coefficient
# is the second coefficient; which it will be if the model is
# of the form p ~ q.
trend_l <- function(fit) {
  coeff <- summary(fit)$coefficients
  list(trend = coeff[2, 1], trend.error = coeff[2, 2])
}

j <- trend_l(fit.30)

out <- file("result/trend.json")
writeLines(toJSON(j), out)
close(out)
