# By Gamers 4 Gamers

As a fan of gaming i decided to great a review site for video games, where users can review and leave rating to games, update content by other users if they find mistakes, add new games when there are some that are missing. The idea is that games are very expensive now a days and any honest feedback is useful before making a purchase decision. Personal goal for the project was, in addition to provide an honest gamer to gamer platform,  to develop my skills in Python programming and working with Mongo database.



## Project Goal

* Create a site for anyone who loves gaming and is looking for something to play but wants to make sure to make the best decision where to spend their money
* Have a place where gamers could leave honest reviews to other users, provide links where the game could be purchased 
* Provide a possibility to rate games and then make the average rating available to gamers.
* Provide an easy to use experience


## User Stories for the site

* As a gamer, i want to get honest information about games that is not purchased by the developers so that i can buy only the best games.
* As a gamer, i want to be able to leave reviews for other people so that they can get an overall understanding of the games strengths/weaknesses
* As a gamer, i want to leave a rating for a game so that other people can understand if the game is good or not.
* As a gamer, i want to see ratings from other users so that i can understand what people generally think of a game.
* As a gamer, i want to read reviews from other users so that i can understand what people generally think of a game.
* As a gamer, i want to be able to add games if there is something i feel should be reviewed but i cannot find it in the library.
* As a gamer, i want to be able to search for games so that i could easily find what i am interested in, or i could add a game if i cannot find it by searching.
* As a site owner i want to provide gamers with a site that provides honest information about games, which is not determined by how much anyone invests in the site
* As a site user i want to provide users with a simple to use site to add games and reviews.
* As a site owner i want to provide a free of charge page for users that they can trust as the content is added by the users themselves


## Design 

The design and choice of colors for the site was determined by ease of use. Goal was to provide easy to read, and easy to use site that works well across platforms and is simple and clean in design. 

Color design aims to provide a strong contrast between the navbar and footer and the background color while keeping an smooth design that is easy on the eye. Content background color is a stronger color to highligh the card with content.

Navbar and Footer colors: 

        background: rgb(196, 196, 198);
        background: linear-gradient(31deg, rgba(196, 196, 198, 1) 1%, rgba(39, 39, 40, 1) 27%, rgba(229, 231, 232, 1) 71%, rgba(84, 84, 84, 1) 91%);


Body background:

        background-color: #E8E5C5;


Content background, provides background color for all game content:

        background-color: #E8E5C5;



Font - across the project same font type has been used for consistency across pages:

        font-family: 'Roboto', sans-serif;


### Wireframes 

I used Balsamiq to create the wireframes, some changes were made to the original wireframes in the process of building the project to provide a cleaner and simpler user experienct. For example page for All Games was changed to display games one on top of the other instead of using the original plan of using a grid to have the games 2 X 2 on top of each other.

![Image](Assets/Wireframes/MS3.png)




## Database 

For this project MONGO Database has been used to store information about games and reviews from users. Two separate databases have been created for games and reviews to be able to scale up in the future and to try to keep the project as efficient as possible.

### Reviews Collection

Reviews collection stores the reviews, ratings and username from the user who left the review, it is a simple collection that will be extended as the project developes in the future.

Key | Type 
------------ | -------------
game_name   | String
user_name   | String
review_name   | String
rating   | String


### Games Collection

Game collection stores the games and details about games, for ease of use to add new data the collection has been kept simple but will grow in complexity as the project developes.

Key | Type 
------------ | -------------
game_name   | String
image_link   | String
purchase_link   | String
game_summary   | String


## Features

### Base.html 

Base.html which provides the base for all pages to build upon has the following features implemented:

Navbar:

* Home that redirects to homepage
* All Games redirects to page where all games can be viewed
* Add a New Game redirects users to a form wher new games can be added
* search functionality that allows users to search games from the library


### Homepage 

Homepage card displayes the latest addition to games library, users who add a new game are redirected to homepage where they can see the game they added and from the go and leave a review.

#### Future features for homepage

In the future a plan to add average score to homepage and create a card functionality that displays 5 top rated games.


### All Games page 

All Games page retrieves all games from collection and displayes them 5 at a time on a page, pagination has been used to limit games to 5 per page as that makes the information easier to consume.

#### Future features for All Games page

In the future plan to sort the games based on alphabetical order instead of the current ordering which displayes oldest additions first.

### Add a new game page 

Provides a form where users can add new games that they cannot find from the existing library of games. It is a simple to use form that inserts data to mongodb.

#### Future features for Add new Game page

This page will develop in line with new functionalities and data needed to implement new functionalities. Some of the features could be to drag-drop image instead of providing a link, add reviews at the same time as new games are added etc. 

### Game details (read and leave reviews)

This page provides all the details about a game that have been stored in reviews and games database. For example in this page you can read all the reviews, see the ratings and also see an average rating for the game. Also you can buy this game via a link provided by users and edit information if there is wrong info/details about the game.

#### Future Features for game details 

Would be to include a video/trailer for the game, more details about when the game has been released, who has made it etc. Also to provide a link to purchase game where site owner could get a percentage of sales to make the site sustainable without advertisement.


### Add Reviews

Users can leave reviews and ratings about a game, the game name is prefilled as the user can access this page only via game details page. The form is simple to use and inserts the data into mongodb reviews collection.

#### Future features for Add reviews

This page will develop in line with new functionalities and data needed to implement new functionalities. In the future user could create a user profile for the site and then if logged in username would be prefilled etc. 


### Search results page

Displayes all games that fit the search criteria.


## Technologies used

* HTML
* CSS 
* JQuery
* Python 
* Materialize
* Jinja 
* Flask 
* Pymongo
* Google fonts



