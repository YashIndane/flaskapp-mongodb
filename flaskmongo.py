from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask("my-app")

@app.route("/home")
def welcome():
  #this is the homepage
  return render_template("home.html")

@app.route("/add")
def add_record():
  #this is page where user adds records
  return render_template("add.html")

@app.route("/update")
def update_record():
  #this is page for updating existing record
  return render_template("update.html")

@app.route("/delete")
def delete():
  #this is for deleting stuff
  return render_template("delete.html")
  

app.run(host = "0.0.0.0", port = 3882)
