#load rtweet
if (!"rtweet" %in% installed.packages()) {install.packages("rtweet")}

library(rtweet)


#twitter setup
appname <- "KarlsruheLocalData"
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