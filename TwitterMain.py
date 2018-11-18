import twitter
from twitter import api
import json
import twitterToFacebookTimes


api = twitter.Api(consumer_key="egUwwqWDe0X3e0fkrt2U1Tj7t",
                  consumer_secret="w1PhwWwAasL8YHJRCOFQsF38v94IAxpjIMxG6blfVsvTHVEKJ6",
                  access_token_key="1740311539-Qa6RPuWhKpz8IygUNqgt1FzzMsFuZHZUf7VlVry",
                  access_token_secret="8k6eoE9ulHCowBddoVtv7hDUyjAlHOdaJrVFkyobuXKHO")

def process():
  processed = []
  toProcess = api.GetUserTimeline()
  for post in toProcess:
      processed_post = {"time": post.created_at, "content": post.text, "platform": "Twitter"}
      processed.append(processed_post)
  return processed

def changeTimes(data):
  for d in data:
    d["time"] = twitterToFacebookTimes.makeFacebookTime(d["time"])

def get_processed_data():
  return json.dumps(process())



