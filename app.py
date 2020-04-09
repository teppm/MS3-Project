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


@app.route('/')


# returns game from games list to be displayed in home page card 
@app.route('/home')

def home():
   return render_template('home.html', games=mongo.db.games.find())

# game details function displays all details about selected game 

@app.route('/game_details, <game_id>')

def game_details(game_id):
  games=mongo.db.games
  chosen_game=mongo.db.games.find_one({'_id':ObjectId(game_id)})
  return render_template('game_details.html', game=chosen_game)
