# SQLAlchemy Data Models

This script utilizes the SQLAlchemy library to define data models using object-oriented programming (OOP) principles. Each model is defined as a class inheriting from `Base`, which is a base class provided by SQLAlchemy for creating data models.

The various classes defined in this script represent tables in a database and define the columns of each table as well as the relationships between these tables. For instance, the `GameEntity` class defines a `game` table with an `id` column and a relationship with the `player` table through the `players` column. The `PlayerEntity` class defines a `player` table with an `id` column and a relationship with the `game` table through the `game_id` column.

The script also creates an instance of `engine` using `create_engine` from SQLAlchemy, which is used to connect to a database. Finally, the script creates an instance of `Session`, which is used to interact with the database and save and retrieve objects from these data models.
