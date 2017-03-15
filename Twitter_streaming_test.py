import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
import html


#Below values were provided when I registered as a twitter app developer
consumer_key = '1cVcll7mSkot7ZWE7FHOc75Mu'
consumer_secret = '8B1rGgAZPijUxijJVnWEDQ9Gyi8I2oHZOKsKXNpfGPqWLasatz'
access_token = '824048096023748608-KKLyg9MDoq5llxFfOLQhayULvCafvmR'
access_secret = 'QHIGYT1DtiWFKnXkGiZiPr5784Tpe5lqpmpd3uCd8KADz'

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

list=twitter_stream.filter(track=['@realDonaldTrump']) #looks for tweets with
