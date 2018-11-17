from flask import Flask, render_template, jsonify
import secrets
import string
app = Flask(__name__)

client_id = "25EcHoX8LS14rg"
random_string = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
url = "https://www.reddit.com/api/v1/authorize?client_id=" + client_id + \
              "&response_type=\"code\"&state=\"" + random_string + \
              "\"&redirect_uri=\"localhost:8080\"&duration=\"temporary\"&scope=[]"

@app.route("/api/getRedditLogin")
def getLogin():
    return jsonify({"url": url})

@app.route("/api/getPosts")
def getPosts():


if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment