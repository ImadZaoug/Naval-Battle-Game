# Views

This folder contains HTML files that serve as the user interface for the naval battle game. Below is a brief overview of each HTML file:

## create_game.html

This page allows users to create a new game. It includes a form to enter a player's name and set the dimensions of the game space. Users can then submit the form to create a new game session.

## home.html

The home page welcomes users to the naval battle game. It provides information about the game, stating that two players are required to start. Users can navigate to other pages from the home page.

## join_game.html

This page enables users to join an existing game by entering their player name and the game ID. Once the form is submitted, the player is added to the specified game session.

## manage_fleet.html

On this page, users can manage their fleet by entering their player name, game ID, and choosing the type of vessel to add. The form allows players to select the type of vessel, set coordinates, and validate their choices.

## play_game.html

This page is the main playing area for the naval battle game. Currently, it is empty and may require further development to display game elements and interactions.

## scripts/create-game.js

This JavaScript file contains functions related to creating a game. It communicates with the server API to handle the creation of new game sessions. The script includes functions to submit the create-game form, process the API response, and display appropriate messages to the user.

Feel free to explore these HTML files and the associated JavaScript code to understand and modify the user interface of the naval battle game.
