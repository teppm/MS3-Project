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
   return render_template('home.html', games=mongo.db.games.find().limit(1))



# game details function displays all details about selected game 
@app.route('/game_details/<game_id>')

def game_details(game_id):
    chosen_game=mongo.db.games.find_one({'_id':ObjectId(game_id)})
    return render_template('game_details.html', game=chosen_game, reviews=mongo.db.reviews.find())



# add games functionality to add new games to collection

@app.route('/add_game')

def add_game():
      return render_template('add_game.html', games=mongo.db.games.find())


@app.route('/insert_game', methods=['POST'])

def insert_game():
    mongo.db.games.insert_one(request.form.to_dict())
    return redirect(url_for('game_details'))


# add a review to game functionality 

@app.route('/add_review')

def add_review():
    games=mongo.db.games.find()    
    return render_template('add_review.html', games=games)