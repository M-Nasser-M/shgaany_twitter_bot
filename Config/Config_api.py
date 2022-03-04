from . import Config_Vars
import tweepy

auth = tweepy.OAuth1UserHandler(
    Config_Vars.TWITTER_API_KEY, Config_Vars.TWITTER_API_SECRET, Config_Vars.TWITTER_ACCESS_TOKEN,
    Config_Vars.TWITTER_ACCESS_TOKEN_SECRET
)

client = tweepy.Client(
    consumer_key=Config_Vars.TWITTER_API_KEY, consumer_secret=Config_Vars.TWITTER_API_SECRET,
    access_token=Config_Vars.TWITTER_ACCESS_TOKEN, access_token_secret=Config_Vars.TWITTER_ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)
