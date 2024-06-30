
import pandas as pd
# 1683 Invalid Tweets
data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets.content.str.len() > 15][['tweet_id']]

