import tweepy
import config


def tweet_img(texts=""):
    client = tweepy.Client(config.bearer_token,config.api_key,config.api_secret,config.access_token,config.access_token_secret)
    auth = tweepy.OAuth1UserHandler(config.api_key,config.api_secret,config.access_token,config.access_token_secret)
    api = tweepy.API(auth)
    media_id = api.media_upload(filename="test.png").media_id_string
    print(media_id)
    client.create_tweet(text=texts,media_ids=[media_id])
    print("DOne")
