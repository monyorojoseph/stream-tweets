from config import connect_api

KENYA_WOEID = 23424863

api = connect_api()


# get woeid
def get_woeid():
    try:
        woeid = 1
        for place  in api.available_trends():
            if place['name'] == "Kenya":
                woeid = int(place['woeid'])
                break
        return woeid
    except:
        print("Can't get WOEID")


# get trending tweets
def trending_topics():
    try:
        trend = api.get_place_trends(get_woeid())
        lst = [tr['name'] for tr in trend[0]['trends']]
        return lst
    except:
        print("Can't get trending topics")