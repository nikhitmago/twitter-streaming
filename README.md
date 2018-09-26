# Twitter Streaming using Reservoir Sampling

Version:

```html
Spark – 2.2.1, Python – 2.7
```

- Implementation of __reservoir sampling__ to track popular twitter tags and calculate some basic statistics like the hottest 5 tags and the average length of the tweet in the list.
- Reservoir has the capacity limit of 100, which can only save 100 tweets. For the first 100 tweets, we save them directly in the list and for the nth twitter, we keep them with a probability of 100/n, else discard it.
- In order to get tweets from Twitter, register [here](https://apps.twitter.com/), by clicking on “Create new app” and then fill the form click on “Create your Twitter app".
- Library dependency: [Tweepy](http://docs.tweepy.org/en/v3.5.0/streaminghowto.html) for Python
- Use the following piece of code to run the file:
```html
bin/spark-submit twitter_streaming.py
```
