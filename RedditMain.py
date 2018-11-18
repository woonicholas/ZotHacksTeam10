import praw
import json

class Reddit:
    def __init__(self):
        self.username = "crsunlimit"
        self.password = "Aa123456"
        self.authenticated = False

    def checkLogin(self, user, pw):
        if user == self.username and pw == self.password:
            self.authenticated = True
            return "Authenticated"

    def create_reddit_instance(self):
        if self.authenticated:
            with open("credentialsReddit.json", "r") as creds:
                credentials = json.load(creds)
            instance = praw.Reddit(client_id=credentials['client_id'],
                                   client_secret=credentials['client_secret'],
                                   username=self.username,
                                   password=self.password,
                                   user_agent=credentials['user_agent'])
            stuff = instance.subreddit('all').new()
            for thing in stuff:


        else:
            return "Error: Not Authenticated"


x = Reddit()
x.checkLogin("crsunlimit", "Aa123456")
x.create_reddit_instance()
