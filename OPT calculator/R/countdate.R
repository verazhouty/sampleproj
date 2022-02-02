#' Returns the current day and date
#'
#' @return character string with day and date
#' @export
#'
#' @examples
#' today()
today <- function() {
  paste0("Today is ",format(Sys.Date(), "%A, %B %d, %Y"))
}
#' Calculate days left to a certain date from today
#'
#' @param date format:YYYY-MM-DD
#'
#' @return Difference of days between today and the date you've entered
#'
#' @examples
#' daysto("2040-01-01")
daysto<-function(date){
  paste0("There are ", as.Date(date)-Sys.Date(), " days until ", date)
}

#' The earliest and latest you shall apply for your initial OPT
#'
#' @param date format:YYYY-MM-DD
#'
#' @return The day range for OPT application, based on your graduation date
#'
#' @examples
#' whentoapply("2022-05-01") #Please refer to your own program for the graduation/completion date
whentoapply<-function(date){
  paste0("You can apply between ", as.Date(date)-90, " and ", as.Date(date) + 60)
}

#' The earliest and latest starting date for your OPT
#'
#' @param date format:YYYY-MM-DD
#'
#' @return The earliest and latest starting date possible, based on your graduation date
#'
#' @examples
#' startdate("2022-05-01") #Please refer to your own program for the graduation/completion date

startdate<-function(date){
  paste0("Your OPT shall start between ", as.Date(date)+1, " and ", as.Date(date) + 60)
}
#' How many days you have used in your current academic level of OPT
#'
#' @param begin format:YYYY-MM-DD
#' @param end format:YYYY-MM-DD
#'
#' @return Total amount of days that were used
#'
#' @examples
#' useddays("2021-05-01","2021-08-01") #If you had used OPT at your current academic level of OPT previously

useddays<-function(begin,end){
  paste0("You had previously used ",difftime(as.Date(end),as.Date(begin))+1," days of your OPT." )
}

#' The end date of your OPT, and the date to apply for extension, if applicable
#'
#' @param date format:YYYY-MM-DD
#' @param days format:number
#'
#' @return the estimated end date of your OPT, and the date you shall apply for STEM extension
#'
#' @examples
#' enddate("2022-06-01",60) # your OPT start date is 2022-06-01, and you had used 60 days of your OPT.
enddate<-function(date,days=0){
  if (days==0){
    paste0("If you've never used OPT at your current academic level, your initial OPT end date is ", as.Date(date)+365,
           ", one year after your selected OPT start date, ", date,
           " .If you are eligible for the STEM OPT extension, you shall apply the extension between " , as.Date(date)+305,
           " and ", as.Date(date)+365, "." )
  }
  else{
    paste0("You had previously used ", days," days of your OPT. Your OPT end date is ", as.Date(date)+ 365-days,
           " .If you are eligible for the STEM OPT extension, you shall apply the extension between " , as.Date(date)+305-days,
           " and ", as.Date(date)+365-days, ".")
  }

}

#' Some links that may be helpful
#'
#' @return links
#'
#' @examples
#' usefullinks()
usefullinks<-function(){
  cat("Applying for OPT is stressful, and you are not in it alone. The following links hopefully will help you out along the process:",
      "USCIS official site: https://www.uscis.gov/working-in-the-united-states/students-and-exchange-visitors/optional-practical-training-opt-for-f-1-students",
      "OPT application tutorial by UC Berkely International office: https://internationaloffice.berkeley.edu/sites/default/files/opt-tutorial.pdf",
      "OPT timeline tracker: https://opttimeline.com/IOE",
      "Please look for the most relevant information from the international student service at your University.",
      "Please do not hesitate to reach out to mental health resource if you find yourself needing extra support."
      , sep = '\n')
}
