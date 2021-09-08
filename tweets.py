import tweepy
from tweepy.api import API 

consumer_key = "oltfrgiOaqKhPzmQqiG8TBxRy"
consumer_secret = "7vYq0U2iJzXVdRg1crxfMzJ4EmMMKpoeXFD4s7WgDS61AxC8jJ"
access_token = "3140036587-im1NWcYbWQUGqngDK1V77rY7ipgFjpBFZ80vLSU"
access_token_secret = "2uAUJ8CcMPulAJjz1ZO1H0YpOmc2QQ9kQJJbaGij8uRx8"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)

public_tweets = API.user_timeline()
for tweets in public_tweets:
    print(tweets.text)