# Twitter Streaming using Reservoir Sampling

- Implementation of __reservoir sampling__ to track popular twitter tags and calculate some basic statistics like the hottest 5 tags and the average length of the tweet in the list.
- In order to get tweets from Twitter, register [here](https://apps.twitter.com/), by clicking on “Create new app” and then fill the form click on “Create your Twitter app".
- Library dependency: [Tweepy](http://docs.tweepy.org/en/v3.5.0/streaming how to.html) for Python
- Use the following piece of code to run the file:
```
bin/spark-submit twitter_streaming.py
```
