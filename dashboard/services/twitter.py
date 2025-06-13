import tweepy

def get_twitter_client(token):
    return tweepy.Client(bearer_token=token)

def post_tweet_api(token, message):
    client = get_twitter_client(token)
    try:
        client.create_tweet(text=message)
    except Exception as e:
        print("Failed to post tweet:", e)
