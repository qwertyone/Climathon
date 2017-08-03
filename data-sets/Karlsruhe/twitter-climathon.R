library(rtweet)
library(ggplot2)
library(dplyr)
library(tidytext)
library(igraph)
library(ggraph)

tweets <- search_tweets(q="#salt", n=10000, lang="en", include_rts=FALSE)

#eliminate irrelevant http elements
tweets$stripped_text <- gsub("http.*","",  tweets$text)
tweets$stripped_text <- gsub("https.*","", tweets$stripped_text)

# remove punctuation, convert to lowercase, add id for each tweet!
tweets_clean <- tweets %>%
  dplyr::select(stripped_text) %>%
  unnest_tokens(word, stripped_text)

# remove punctuation, convert to lowercase, add id for each tweet!
tweets_clean <- tweets %>%
  dplyr::select(stripped_text) %>%
  unnest_tokens(word, stripped_text)

# load list of stop words - from the tidytext package
data("stop_words")

# remove stop words from our list of words
cleaned_tweet_words <- tweets_clean %>%
  anti_join(stop_words)

#install_github("dgrtwo/widyr")
#library(widyr)

# remove punctuation, convert to lowercase, add id for each tweet!
tweets_paired_words <- tweets %>%
  dplyr::select(stripped_text) %>%
  unnest_tokens(paired_words, stripped_text, token = "ngrams", n=2)

tweets_paired_words %>%
  count(paired_words, sort = TRUE)


library(tidyr)
tweets_separated_words <- tweets_paired_words %>%
  separate(paired_words, c("word1", "word2"), sep = " ")

tweets_filtered <- tweets_separated_words %>%
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word)

# new bigram counts:
words_counts <- tweets_filtered %>%
  count(word1, word2, sort = TRUE)

library(igraph)
library(ggraph)

# plot word network
words_counts %>%
        filter(n >= 10)%>%
        graph_from_data_frame() %>%
        ggraph(layout = "fr") +
        geom_edge_link(aes(edge_alpha = n, edge_width = n)) +
        geom_node_point(color = "darkslategray4", size = 3) +
        geom_node_text(aes(label = name), vjust = 1.8, size=3) +
        labs(title= "Word Network: Tweets using the hashtag - #...",
             subtitle="Text mining twitter data ",
             x="", y="")

