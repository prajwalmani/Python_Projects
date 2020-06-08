import tweepy
import hidden
keys=[]
keys=hidden.oauth()
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)
name=input("Enter the account name ")
user_tweets=api.user_timeline(id=name,count=5)
for tweet in user_tweets:
    print(tweet.text)
