from flask import Flask, render_template, jsonify, request
import secrets
import string
from RedditMain import Reddit

app = Flask(__name__)

client_id = "25EcHoX8LS14rg"
#random_string = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
#url = "https://www.reddit.com/api/v1/authorize?client_id=" + client_id + \
#              "&response_type=\"code\"&state=\"" + random_string + \
#              "\"&redirect_uri=\"localhost:8080\"&duration=\"temporary\"&scope=[]"

@app.route("/api/redditLogin", methods=["GET", "POST"])
def getLogin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]




@app.route("/api/getPosts")
def getPosts():


if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment