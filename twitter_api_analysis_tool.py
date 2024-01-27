import tweepy
from textblob import TextBlob

# Set up your Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def analyze_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    # Classify the polarity of the tweet
    return 'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'

def twitter_analysis(hashtag, num_tweets=10):
    try:
        # Fetch tweets with the given hashtag
        tweets = tweepy.Cursor(api.search, q=f'#{hashtag}', lang='en').items(num_tweets)

        print(f"Analyzing tweets with #{hashtag}...\n")

        for tweet in tweets:
            print(f"Tweet: {tweet.text}")
            print(f"Sentiment: {analyze_tweet_sentiment(tweet.text)}\n")

    except tweepy.TweepError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example: Analyze tweets with the hashtag #Python
    twitter_analysis('Python', num_tweets=5)
