import praw
import secrets
import string
from flask import Flask, render_template
import requests

class Reddit:
    def __init__(self):
        app = Flask(__name__)
        @app.route(/)

        client_id = "25EcHoX8LS14rg"
        random_string = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        url = "https://www.reddit.com/api/v1/authorize?client_id=" + client_id + \
              "&response_type=\"code\"&state=\"" + random_string + \
              "\"&redirect_uri=\"localhost:8080\"&duration=\"temporary\"&scope=[]"

        subscribedList = []

    def getSubscribedList(self):

