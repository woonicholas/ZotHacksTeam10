from flask import Flask, render_template, jsonify, request
import facebook
import TwitterMain
import all
app = Flask(__name__)

@app.route("/main/process", methods=["GET"])
def sendData():
    request.POST(all.process())

@app.route("/facebook/process", methods=["GET"])
def sendData():
    request.POST(facebook.get_processed_data())

@app.route("/twitter/process", methods=["GET"])
def sendData():
    request.POST(TwitterMain.process())

@app.route("/main/", methods=["GET"])

@app.route("/main/", methods=["GET"])

@app.route("/main/", methods=["GET"])

@app.route("/main/", methods=["GET"])




if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment