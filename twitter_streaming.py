import tweepy
from random import randint
from pyspark import SparkContext
import numpy as np

sc = SparkContext(appName="Twitter Streaming")
sc.setLogLevel("ERROR")

consumerKey = "2oHgib9Hn208bNVsGz2giwPgb"
consumerSecret = "Cbw0I5e4W7DGnDzRjYVLTDzgBYVyZDsaD3AwheRhv2Nj6cXVo4"
accessKey = "1018299854030700544-8kIpWCGgPgTqhFGhdKWzh9fMQudddc"
accessSecret = "QnX9QydNKCaA2hL8iUDtif0vFWqAGx2qQtCNnIdMJjOru"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

count = -1
tweets = []

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global count
        global tweets
        count += 1
        if count > 99:
            index = randint(0,count)
            if index < len(tweets):
                hot = {}
                tweetLen = []
                tweets[index] = status
                for tweet in tweets:
                    tweetLen.append(len(tweet.text))
                    hashtags = tweet.entities.get('hashtags')
                    if len(hashtags) != 0:
                        for hashtag in hashtags:
                            if hashtag['text'] not in hot:
                                hot[hashtag['text']] = 1
                            else:
                                hot[hashtag['text']] += 1
                
                print("\nThe number of twitter from beginning: {}".format(count+1))
                print("Top 5 hot hashtags:")
                hotHashTags = sorted(hot.items(), key = lambda x: x[1], reverse = True)[:5]
                for hashtag in hotHashTags:
                    print('{}:{}'.format(hashtag[0].encode('utf-8'), str(hashtag[1])))
                print("The average length of the twitter is: {}\n".format(np.mean(tweetLen)))
        else:
            tweets.append(status)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['#'])