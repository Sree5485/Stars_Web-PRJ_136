from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)

@app.route("/")
def stars():
    return jsonify({
        "stars":data
    })

@app.route("/star")
def planet():
    name=request.args.get("name")
    stardata=next(i for i in data if i["name"]==name)
    return jsonify({
        "stars":stardata
    })
app.run()
