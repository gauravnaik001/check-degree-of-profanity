# check-degree-of-profanity
Small test code to check degree of profanity in a tweet given a dataset of tweets and list of profanities. 
The code is written in python.

Considered the tweets dataset is an excel file containing only tweets and only in english language.
Considered the set of profanities as a list containing the profanities as words and only in english language.

Here the tweets data and profanities data is read from a csv file and only tweets from english language is considered and loaded into a list.
Before the tweets data is used, it is preprocessed by converting the string into lowercase and then removing special characters and numerical values.
Here the degree of profanity is considered as taking the count of profanities divided by the length of the sentence.
