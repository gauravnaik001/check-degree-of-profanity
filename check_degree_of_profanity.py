# Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. 
# Write a program that can indicate the degree of profanity for each sentence in the file. 
# Write in any programming language (preferably in Python)-make any assumptions, but remember to state them. 
# Please place the code in GitHub with proper documentation and share.

# Considered the tweets dataset is an excel file containing only tweets and only in english language.
# Considered the set of profanities as a list containing the profanities as words and only in english language.

# Here the tweets data and profanities data is read from a csv file and only tweets from english language is considered and loaded into a list.
# Before the tweets data is used, it is preprocessed by converting the string into lowercase and then removing special characters and numerical values.
# Here the degree of profanity is considered as taking the count of profanities divided by the length of the sentence.
 
# libraries to import
import re
import csv

# Read the tweets data from the csv file
# Here the tweets data is present in a csv file, the tweets considered are only in the english language
tweets_list = []
with open('Tweets dataset.csv', newline='') as file:
    for row in csv.reader(file,delimiter='\n'):
        tweets_list.append(row[0])  # the data is taken from the csv file and converted into a list
print(tweets_list)

# Read the profanities data from the csv file
# Here the tweets data is present in a csv file, the tweets considered are only in the english language
profanities_list = []
with open('Profanities dataset.csv', newline='') as file:
    for row in csv.reader(file):
        profanities_list.append(row[0])  # the data is taken from the csv file and converted into a list
print(profanities_list)

# Preprocess the data

# Convert into lowercase
def convert_lowercase(sentence):
    filtered_sentence = sentence.lower()  # converts the inputted string into lowercase
    return filtered_sentence

# Remove special characters
def remove_specialchar(sentence):
    pattern = r'[?|$|&|*|%|@|(|)|~|!|_|-]' 
    filtered_sentence = re.sub(pattern, r'', sentence)  # removes special characters from the inputted string
    pattern = r'[0-9]' 
    filtered_sentence = re.sub(pattern,r'',sentence)  # removes numerical value from the inputted string
    return filtered_sentence

# Tokenize the sentence
def tokenize(text): 
    return re.findall(r'\w+', text) # breaks down the string into words and returns the value as a list

# Calculate degree of profanity 
# Here the degree of profanity is considered as number of occurrences divided by total number
def calculate_profanity(sentence):
    degree_of_profanity = sum(1 for t in sentence if t in profanities_list) / len(sentence) 
    return degree_of_profanity

# Calculate the degree of profanity for each tweet
for sentence in tweets_list :
    sentence = str(sentence)
    lower_sentence = convert_lowercase(sentence)     
    removedchar_sentence = remove_specialchar(lower_sentence)    
    tokenized_sentence = tokenize(removedchar_sentence)    
    degree_of_profanity = calculate_profanity(tokenized_sentence)
    print("Degree of profanity - {:.2f}".format(degree_of_profanity))




