#Create for first tweet here
#load rtweet
if (!"rtweet" %in% installed.packages()) {install.packages("rtweet")}

library(rtweet)

#twitter setup
appname <- ""
#Consumer Key (API Key)
key <- "" 
#Consumer Secret (API Secret)
secret <- ""

twitter_token <- create_token(app=appname, consumer_key=key, consumer_secret=secret)

#save twitter token
home_directory <- path.expand("~/")
file_name <- file.path(home_directory, "twitter_token.rds")
saveRDS(twitter_token, file = file_name)
cat(paste0("TWITTER_PAT=", file_name), file = file.path(home_directory, ".Renviron"), append=TRUE)


library(dplyr)
library(tidytext)
library(stringr)


tweets <- search_tweets(q="current weather in Karlsruhe", n=100, lang="en", include_rts=FALSE)
tweet_current <- tweets$text[1]
temp<-"°C"
humd<-"%"

loc_temp<-str_locate(tweet_current,temp) 
loc_hum<-str_locate(tweet_current,humd)
 
#need to find more valid readings
temprature_drybulb <- str_sub(tweet_current, start=(loc_temp[1]-3),end=(loc_temp[2]-2))
#need to find more valid readings
humidity_relative <- str_sub(tweet_current, start=(loc_hum[1]-3),end=(loc_hum[2]-1))

#clean results by removing all but numerals and set proper data type
regexp <- "[[:digit:]]+"
humidity_relative <- as.numeric(str_extract(humidity_relative, regexp))
temprature_drybulb <- as.numeric(str_extract(temprature_drybulb, regexp))

#calculate heat index from http://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
#HI <- 2.04901523*temprature_drybulb + 10.14333127*humidity_relative - (.22475541*temprature_drybulb*humidity_relative) - (.00683783*temprature_drybulb*temprature_drybulb) - (.05481717*humidity_relative*humidity_relative) + (.00122874*temprature_drybulb*temprature_drybulb*humidity_relative) + (.00085282*temprature_drybulb*humidity_relative*humidity_relative) - (.00000199*temprature_drybulb*temprature_drybulb*humidity_relative*humidity_relative)-42.379 

#Rothfusz regression and adjustments necessary in specific conditions
HI <- .5*(temprature_drybulb + 61 + ((temprature_drybulb - 68)*1.2) + (humidity_relative * 0.094))

result <- mean(HI + temprature_drybulb)

ifelse (result < 80, current_condition <- "Safe",
	ifelse(80 > result | result <= 90, current_condition <- "Yellow",
	ifelse(90 > result | result <= 103, current_condition <- "L_Orange",
	ifelse(103 > result | result <= 124, current_condition <- "D_Orange",current_condition <- "Red"
))))

#random relevant facts Safe

s1 <- "#OSHA will tell you that sweating does not work as well on humid days as it does on dry days. It is this muggy feeling. #Karlsruhe"
s2 <- "When the weather is dry, please drink more water. Sweat evaporates more quickly than in #highhumidity. #Karlsruhe"

S = list(s1, s2)

#random facts when high humidity
h1 <- "You might be feeling hotter now. Humidity will do that."

ifelse (current_condition == "Safe", status <- as.character(sample(S[])),"error")

#post momentary tweet guidance
post_tweet(status=status[1])

