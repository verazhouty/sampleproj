% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/countdate.R
\name{enddate}
\alias{enddate}
\title{The end date of your OPT, and the date to apply for extension, if applicable}
\usage{
enddate(date, days = 0)
}
\arguments{
\item{date}{format:YYYY-MM-DD}

\item{days}{format:number}
}
\value{
the estimated end date of your OPT, and the date you shall apply for STEM extension
}
\description{
The end date of your OPT, and the date to apply for extension, if applicable
}
\examples{
enddate("2022-06-01",60) # your OPT start date is 2022-06-01, and you had used 60 days of your OPT.
}
