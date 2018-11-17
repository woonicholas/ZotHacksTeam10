import praw

class Reddit:
    def __init__(self):
        self.username = "crsunlimit"
        self.password = "Aa123456"
        self.authenticated = False

    def checkLogin(self, user, pw):
        if user == self.username and pw == self.password:
            self.authenticated = True




