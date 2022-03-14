import tweepy, logging, time
from config import *
from trendTopics import trending_topics


# custom stream listener
class StreamListener(tweepy.Stream):
    def on_status(self, status):
        time.sleep(2)
        print(f"[Tweet]{status.text}")
        print(f"[Screen name] {status.user.screen_name}")
        return status

# main function
def main(trends):
    stream = StreamListener(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream.filter(track=trends, languages=['en'])

main(trending_topics())