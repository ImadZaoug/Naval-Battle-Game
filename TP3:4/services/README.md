# GameService Readme

## Overview

This code defines a `GameService` class that implements various methods for managing a game session. The class incorporates an instance of `GameDao`, an external class responsible for interacting with a database to save and retrieve game objects.

## Methods

### `create_game`

Creates a new game session by instantiating a `Game` object and adding a player to this session using an instance of `Player` and a `Battlefield`.

### `join_game`

Enables a new player to join an existing game session by adding a new `Player` object to that session.

### `add_vessel`

Allows a player to add a vessel to their battlefield. The method first verifies if the player is in the game session and if the vessel is valid before adding it to the player's battlefield.

### `shoot_at`

Allows a player to shoot at an enemy vessel using the specified coordinates. The method first checks if the player is in the game session and if the targeted vessel belongs to another player before proceeding with the shot.

### `get_game_status`

Returns the status of the game session based on the remaining power of each player's vessels. If the calling player's vessel power is zero, the method returns "Lost." Otherwise, it returns "Won" if the other player's vessel power is zero, or "Ongoing" otherwise.

Feel free to explore and utilize these methods for managing and simulating game sessions!
