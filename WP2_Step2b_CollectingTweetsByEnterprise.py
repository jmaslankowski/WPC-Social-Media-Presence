# WP2 Social Media Use Case, Step 2b
# If you need more information:
# Contact: j.maslankowski@stat.gov.pl

import tweepy 
import csv

# !!! put your keys in single quota in the four lines below
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# !!! replace ACCOUNT name of the enterprise to collect information from
account_names=['jmaslankowski','GUS_stat']

def get_all_tweets(screen_name):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        alltweets = []
        new_tweets = api.user_timeline(screen_name = screen_name,count=200)
        alltweets.extend(new_tweets)
    except:
        print("Cannot authenticate with Twitter credentials. Check consumer keys.")
    else:
        oldest = alltweets[-1].id - 1
        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
            print ("%s tweets downloaded and still downloading..." % len(alltweets))
        # the output file is WP2_enterprise_... .csv where ... is the account name
        with open('WP2_enterprise_%s.csv' % screen_name, 'w') as f:
            for tweet in alltweets:
                outtweets = str(tweet.text)+"\n"
                f.write(outtweets)
        pass
if __name__ == '__main__':
    for account in account_names:
        get_all_tweets(account)
