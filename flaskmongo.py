from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask("my-app")

#connecting with database
client = MongoClient("mongodb://127.0.0.1:27017")
collection=client.userdb.u_collection

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

@app.route("/addop" , methods=["GET"])
def add_to_db():
  #this function adds the data to database

  doc={ 
        "_id": request.args.get("id"),
        "name": request.args.get("na"),
        "age": int(request.args.get("ag")),
        "region": request.args.get("reg"),
        "weight": request.args.get("we")
  }

  collection.insert_one(doc)
  return "Data Added!"

@app.route("/updateop" , methods=["GET"])
def update_data():
  #this function updates record already present

  collection.update_one(
             {"_id":request.args.get("idd")},
             {"$set":{request.args.get("sel"):request.args.get("nv")}}
  )

  return "Updated!"

@app.route("/delop" , methods=["GET"])
def delete_data():
  #this function deletes the document

  collection.delete_one({ "_id":request.args.get("id1") })
  return "Deleted!"

  
app.run(host = "0.0.0.0", port = 3882)
