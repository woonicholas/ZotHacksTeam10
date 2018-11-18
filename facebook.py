#import facebook
import json
import requests

TOKEN="EAAEgO7dp1aoBAN1LfLWZCxZBpS5660XGiTvnVl3P7fvLYt9bJ7BKWPTntBWYZCyi30ZA1axppJOAXKyo7SWCTPSYQyZAC8RoEZCpT2tAAVha7V87V26iED4e1x14Ilf6qSZBT4tfZCBBZA4yAr35J9CG3IBoqK6wMrwBhQ1sdfItnVlrIuQNnJH6BFzm7gx4vB9kXdqpFzwVEa7pytPbrFwWf"
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

return_json = json.dumps(process(get_posts()))
file=open("facebook_data.json", "w")
file.write(return_json)
file.close()
