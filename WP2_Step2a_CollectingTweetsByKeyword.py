# WP2 Social Media Use Case, Step 2a
# If you need more information:
# Contact: j.maslankowski@stat.gov.pl

import tweepy 
import csv

# !!! put your keys in single quota in the four lines below
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# !!! REPLACE pl WITH YOUR COUNTRY CODE
language='pl'

# !!! REPLACE THE keywords IF YOU WANT TO COLLECT INFORMATION SPECIFIC TO THE KEYWORD
keywords=["commercial","marketing"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# you can use geo location if you need by, e.g., 
# api=tweepy.API(auth, geocode="51.776667, 19.454722, 300km")
api = tweepy.API(auth)

# the name of the output file is keyword_ .csv, where space is replaced with the keyword, e.g., WP2_keyword_commercial.csv
for keyword in keywords:
# the software will collect 5000 current tweets in selected language
    hashTweet = tweepy.Cursor(api.search, q=keyword, count=5000, lang=language).items(5000)
    with open('WP2_keyword_%s.csv' % keyword, 'w', encoding="utf-8", errors="ignore") as f:
        for tweet in hashTweet:
            outtweets=str(tweet.text)
            if "RT " not in outtweets:
                f.write(outtweets+"\n")




