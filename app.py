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


@app.route('/insert_review', methods=['POST'])

def insert_review():
    mongo.db.reviews.insert_one(request.form.to_dict())
    return redirect(url_for('home'))


# functionality to display all games

@app.route('/all_games')

def all_games():
    games=mongo.db.games.find()
    return render_template('all_games.html', games=games)


# search function to find games based on user input

@app.route('/find_games', methods=['POST'])

def find_games():
    mongo.db.games.create_index([('game_name', 'text'), ('game_summary', 'text')])
    search=request.form.get('search')
    results=mongo.db.games.find({'$text':{'$search':search }})
    return render_template('search_results.html', results=results)

    
    


# edit_game function, provide users with a possibility to edit information about a specific game

@app.route('/edit_game/<game_id>')

def edit_game(game_id):
    chosen_game=mongo.db.games.find_one({'_id':ObjectId(game_id)})
    return render_template('edit_game.html', game=chosen_game)



@app.route('/update_game/<game_id>', methods=['POST'])

def update_game(game_id):
    game=mongo.db.games
    game.update({'_id':ObjectId(game_id)},
    {
            'game_name':request.form.get('game_name'),
            'image_link':request.form.get('image_link'),
            'purchase_link':request.form.get('purchase_link'),
            'game_summary':request.form.get('game_summary')
            
            })
    return redirect(url_for('game_details'))



    
