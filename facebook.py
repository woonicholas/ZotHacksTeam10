#import facebook
import json
import requests

TOKEN="EAAEgO7dp1aoBAGOgPHMgTx01q44AiKfjudvQuoy0fzBhZAk9DPgZCtrhUMrYJIZBDPZCaL6jTP045tkyizJ9NZAXeDZClXEq2ubDOhBZCUBc1w0UwB6GuN1YVUCmqw6LsQZA43x5dtPWAZAohpaMimcoFDr6dviQUfhaVZBJbtcrMF1xy5dqAUhA0WZBZAHzCJYBGiCs9MzqFojdGyA0eI6MuW15"
#graph=facebook.GraphAPI(access_token=TOKEN, version="2.12")

def get_posts():
    """Returns list of posts on my timeline"""

    parameters = {'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/me/feed', params=parameters)
    result = json.loads(r.text)
    return result['data']

def process(data):
    processed=[]
    for post in data:
        processed_post={"time":post["created_time"],"content": "","platform":"Facebook"}
        if "message" in post.keys():
            processed_post["content"]+=" "+post["message"]
        if "story" in post.keys():
            processed_post["content"]+=" "+post["story"]
        processed.append(processed_post)
    return processed

def get_processed_data():
    return json.dumps(process(get_posts()))

get_posts()