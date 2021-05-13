from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask("my-app")

#connecting with database
client = MongoClient("mongodb://127.0.0.1:27017")

#getting the table (collection)
#format is client.<data-base-name>.<collection-name>
collection=client.userdb.u_collection

get_data = lambda x : request.args.get(x)
  
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

@app.route("/fetchdata")
def fetch_data():
  #this method is used to fetch data
  return render_template("fetch.html")

@app.route("/addop" , methods = ["GET"])
def add_to_db():
  #this function adds the data to database

  doc={ 
        "_id": get_data("id"),
        "name": get_data("na"),
        "age": int(get_data("ag")),
        "region": get_data("reg"),
        "weight": get_data("we")
  }

  collection.insert_one(doc)
  return "Data Added!"

@app.route("/updateop" , methods = ["GET"])
def update_data():
  #this function updates record already present

  collection.update_one(
             {"_id":get_data("idd")},
             {"$set":{get_data("sel"):get_data("nv")}}
  )

  return "Updated!"

@app.route("/delop" , methods = ["GET"])
def delete_data():
  #this function deletes the document

  collection.delete_one({ "_id":get_data("id1") })
  return "Deleted!"

@app.route("/fad")
def get_all_data():
  #this prints the whole table
  
  out = ''
  for record in collection.find():
    out += str(record) + "</br>"

  return out

@app.route("/fsd" , methods = ["GET"])
def get_doc():
  #this will print a document data based on ID
   
  query =  { "_id" : get_data("sd") }
  doc = str(collection.find_one(query))
  return doc

app.run(host = "0.0.0.0", port = 3882)
