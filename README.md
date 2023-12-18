# Naval Battle Game

This repository comprises a naval battle game implemented with distinct folders for better organization and separation of concerns. Each folder encapsulates specific functionalities and components. Below is an overview of the primary folders within the repository:

## 1. Controller

The `Controller` folder contains the FastAPI Game Server, which defines a FastAPI web server exposing HTTP endpoints for creating, joining, and interacting with games. The script utilizes dependencies such as uvicorn, FastAPI, and pydantic. It initializes the FastAPI app, GameService, and various input/output models for API endpoints. API endpoints include creating/joining games, adding vessels, shooting at vessels, and retrieving game states. Exception handling and server start configurations are also included.

## 2. Dao

The `Dao` (Data Access Object) folder encompasses SQLAlchemy Data Models. This script utilizes SQLAlchemy to define data models using object-oriented programming principles. Each class represents a table in a database with defined columns and relationships. It establishes an engine to connect to the database and a Session to interact with and manage objects in the database.

## 3. Model

The `Model` folder contains Python scripts representing fundamental classes and data structures used in the game. These include classes for weapons, vessels, and various launchers. These classes define the behavior and characteristics of the game entities.

## 4. Services

The `Services` folder includes a `GameService` README, providing an overview of the code that defines a `GameService` class. The class implements methods for managing a game session and utilizes an instance of `GameDao` for database interaction. Methods include creating/joining games, adding vessels, shooting at vessels, and retrieving game status.

## 5. Views

The `Views` folder holds HTML files representing different pages of the game's user interface. Each HTML file corresponds to a specific game-related action, such as creating a game, joining a game, managing the fleet, and playing the game. Additionally, there are associated JavaScript scripts for handling frontend functionality.

Feel free to explore each folder for detailed information on their contents and functionalities. Modify and enhance the code to customize the naval battle game according to your preferences. Refer to individual README files within each folder for more specific details.
