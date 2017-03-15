#Original Code by Marco Bonanzini
#Modified by Bassam Salim
# collects tweets with a given key word and saves them in JSON format
import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
import html


#Below values were provided when I registered as a twitter app developer
consumer_key = 'Get your own twitter key'
consumer_secret = 'Get your own twitter key'
access_token = 'Get your own twitter key'
access_secret = 'Get your own twitter key'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data",str(e))
            return True

        def on_error(self, status):
            print(status)
            return True

twitter_stream = Stream(auth, MyListener())

list=twitter_stream.filter(track=['@realDonaldTrump']) # look for tweets with given tag.can be any search term 
