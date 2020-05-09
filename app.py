import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
from flask_paginate import Pagination, get_page_parameter
if path.exists("env.py"):
  import env 

app=Flask(__name__)


app.config['MONGO_DBNAME'] = 'game_review'
app.config['MONGO_URI'] = os.environ['MONGO_URI']

mongo = PyMongo(app)


@app.route('/')




@app.route('/home')
def home():
    #function def home() renders home.html and finds latest addition to games database
    return render_template('home.html', games=mongo.db.games.find().limit(1).sort([('_id', -1)])) 





@app.route('/game_details/<game_id>')
def game_details(game_id):
    '''
    find a specific game based on ObjectID from games collection
    assign variable game name of the game from chosen_game variable 
    match game name from games collection to game_name from reviews collection
    '''
    chosen_game=mongo.db.games.find_one({'_id':ObjectId(game_id)})    
    game_name=chosen_game['game_name'] 
    reviews=mongo.db.reviews.find({'game_name': game_name}) 
    '''
    return all reviews for specific game name and use for loop to return the sum of all 
    ratings for a that game
    '''
    rating_amount=mongo.db.reviews.find({'game_name': game_name})
    totalRating=0
    for review in rating_amount:        
        totalRating += int(review['rating'])        
        print(totalRating)
    '''
    return all reviews for specific and len(list) to get total amount of reviews
    that have been submitted for a game
    '''
    reviews_amount=mongo.db.reviews.find({'game_name': game_name})
    numberOfReviews= len(list(reviews_amount))
    print(numberOfReviews)    
    '''
    if elif else function to check if there any reviews submitted, if not to print(0)
    if reviews have been submitted calculates and returns average score from ratings
    '''
    if numberOfReviews == 0:
        averageRating=print(0)
    elif numberOfReviews == None:
        averageRating=print(0)
    else:
        averageRating=totalRating/numberOfReviews
        print(averageRating)

    #render game_details with chose game for details and reviews for that game + average function
    return render_template('game_details.html', game=chosen_game, reviews=reviews, average=averageRating)





@app.route('/add_game')

def add_game():
    #render add_game.html page to access form where new games can be added to games collection
    return render_template('add_game.html')





@app.route('/insert_game', methods=['POST'])

def insert_game():
    '''
    gets values from add_game.html form and insert to games collection in mongo db
    after value has been inserted returns to home page where latest addition to database is displayed
    '''
    mongo.db.games.create_index([('game_name', 1)], unique=True) #unique index to minimize possibility that duplicates are added into games DB
    try:
      mongo.db.games.insert_one(request.form.to_dict())
      return redirect(url_for('home'))
    except pymongo.errors.DuplicateKeyError:
      return redirect(url_for('add_game'))
     
      

 


@app.route('/add_review/<game_id>')

def add_review(game_id):
    '''
    objectId from game_details page and render add_review.html where users can use form
    to leave reviews for that specific game
    '''
    games=mongo.db.games.find_one({'_id':ObjectId(game_id)})  
    return render_template('add_review.html', games=games)





@app.route('/insert_review/<game_id>', methods=['POST'])

def insert_review(game_id):
    '''
    inserts review to reviews collection and redirects back to game_details page where users 
    can see the review they have just left
    '''
    games=mongo.db.games.find_one({'_id':ObjectId(game_id)}) 
    mongo.db.reviews.insert_one(request.form.to_dict())
    return redirect(url_for('game_details', game_id=game_id))





@app.route('/all_games')

def all_games():
    '''
    provide users access to see all games that have been added in the games collection
    to make the page more usable when more and more games are being added, pagination used to limit
    amount of games that are displayed to 5 per page
    '''
    search=False
    args=request.args.get('args')
    if args:
        search=True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page=5
    offset =((page -1) * per_page)
    games=mongo.db.games.find()
    games_to_render=games.limit(per_page).skip(offset)
    pagination= Pagination(page=page, total=games.count(), search=search, record_name='games',  per_page=5)
    return render_template('all_games.html', games=games_to_render, pagination=pagination)




@app.route('/find_games', methods=['POST'])

def find_games():
    '''
    mongodb full text search functionality to allow users to search from database 
    and display results that are a match
    '''
    mongo.db.games.create_index([('game_name', 'text'), ('game_summary', 'text')])
    search=request.form.get('search')
    results=mongo.db.games.find({'$text':{'$search':search }})
    return render_template('search_results.html', results=results)

    
    


@app.route('/edit_game/<game_id>')

def edit_game(game_id):
    '''
    allow user to edit game details if they find a mistake, can be accessed by user from game_details page 
    returns all details based on ObjectId and renders edit_game.html where prefilled form can be used 
    to update 
    '''
    chosen_game=mongo.db.games.find_one({'_id':ObjectId(game_id)})
    return render_template('edit_game.html', game=chosen_game)





@app.route('/update_game/<game_id>', methods=['POST'])

def update_game(game_id):
    '''
    returns values from form on edit_game.html page where user has been able to update game details
    '''
    game=mongo.db.games
    game.update({'_id':ObjectId(game_id)},
    {
            'game_name':request.form.get('game_name'),
            'image_link':request.form.get('image_link'),
            'purchase_link':request.form.get('purchase_link'),
            'game_summary':request.form.get('game_summary')
            
            })
    return redirect(url_for('game_details', game_id=game_id))





'''
return IP and PORT to be able to deploy site on heroku
'''
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)