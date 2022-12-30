CREATE DATABASE tdlog;
USE tdlog;
CREATE TABLE game (
  id INTEGER NOT NULL PRIMARY KEY
);

CREATE TABLE player (
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  game_id INTEGER NOT NULL,
  FOREIGN KEY(game_id) REFERENCES game (id)
);

CREATE TABLE battlefield (
  id INTEGER NOT NULL PRIMARY KEY,
  min_x INTEGER,
  min_y INTEGER,
  min_z INTEGER,
  max_x INTEGER,
  max_y INTEGER,
  max_z INTEGER,
  max_power INTEGER, 
  player_id INTEGER NOT NULL, 
  FOREIGN KEY(player_id) REFERENCES player (id)
);

CREATE TABLE vessel (
  id INTEGER NOT NULL PRIMARY KEY, 
  coord_x INTEGER, 
  coord_y INTEGER, 
  coord_z INTEGER,
  hits_to_be_destroyed INTEGER, 
  type VARCHAR(100),
  battle_field_id INTEGER NOT NULL, 
  FOREIGN KEY(battle_field_id) REFERENCES battlefield (id)
);

CREATE TABLE weapon (
  id INTEGER NOT NULL PRIMARY KEY, 
  ammunitions INTEGER,
  range_ INTEGER,
  type VARCHAR(100),
  vessel_id INTEGER NOT NULL, 
  FOREIGN KEY(vessel_id) REFERENCES vessel (id)
);