import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app=Flask(__name__)

app.config['MONGO_DBNAME'] = 'game_review'
app.config['MONGO_URI'] = os.environ['MONGO_URI']

mongo = PyMongo(app)


@app.route("/")

def home():

   return 'did i get this to work properly'