from flask import Flask, render_template, jsonify, request
import facebook
app = Flask(__name__)

@app.route("/main/", methods=["GET"])

@app.route("/facebook/process", methods=["GET"])
def sendData():
    request.POST(facebook.process(facebook.get_posts()))

@app.route("/main/", methods=["GET"])

@app.route("/main/", methods=["GET"])

@app.route("/main/", methods=["GET"])

@app.route("/main/", methods=["GET"])

@app.route("/main/", methods=["GET"])




if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment