import tweepy
import pandas as pd
from datetime import datetime
import s3fs


bearer_token = "AAAAAAAAAAAAAAAAAAAAAA4b0wEAAAAAUf0LkbBYUXMQ2iNT8yidX5fyXtU%3DY0xIYbT7MHvgLJMtZY8t0imTMz58OmAvXJnmUIO83nOg5FlOIq"

client = tweepy.Client(bearer_token=bearer_token)

# Get tweets from a user by username (user ID is needed)
user = client.get_user(username='elonmusk')
user_id = user.data.id

# Fetch tweets from the user timeline (max 100 per call)
tweets = client.get_users_tweets(id=user_id, max_results=100, tweet_fields=["created_at","public_metrics","text"])

# Parse tweets
data = []
for tweet in tweets.data:
    data.append({
        'user': 'elonmusk',
        'text': tweet.text,
        'favorite_count': tweet.public_metrics['like_count'],
        'retweet_count': tweet.public_metrics['retweet_count'],
        'created_at': tweet.created_at
    })

df = pd.DataFrame(data)
df.to_csv("musk_x.csv")
