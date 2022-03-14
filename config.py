from decouple import config
import tweepy, logging

logging.basicConfig(level=logging.INFO, filename="streamTweets.log")
logger = logging.getLogger()

CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")
ACCESS_TOKEN = config("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = config("ACCESS_TOKEN_SECRET")

def connect_api():
    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY,CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
        logger.info("Tweepy api verified")        
    except:
        logger.warning("Tweepy api couldn't verify")   
    
    return api