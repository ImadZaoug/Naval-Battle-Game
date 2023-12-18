# FastAPI Game Server

This script defines a FastAPI web server that exposes several HTTP endpoints for creating, joining, and interacting with games.

## Dependencies
At the beginning of the script, various libraries are imported, including uvicorn, FastAPI, and BaseModel from pydantic. uvicorn is a high-performance web server for running asyncio-based web applications, and FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python data types. BaseModel is a pydantic class that can be used to define input and output models for an API endpoint.

## Initialization
The script creates an instance of FastAPI called `app` and an instance of `GameService` called `game_service`. It also defines several classes representing input models for different API endpoints (CreateGameData, JoinGameData, AddVesselData, and ShootAtData). These classes use the BaseModel class and specify a number of fields with different data types (e.g., `player_name` is a string, `game_id` is an integer, etc.).

## API Endpoints
After defining these classes, the script defines multiple API endpoints using the `@app.post` and `@app.get` decorators. These endpoints allow clients to create games, join games, add vessels to games, shoot at vessels in games, and retrieve the state of a game. Each endpoint is associated with a specific input model (e.g., `create_game` is associated with `CreateGameData`) and a specific return type (e.g., `get_game` returns a `Game` object).

## Exception Handling
The script also defines an exception handler (`exception_handler`) that will be called in case of an exception during request processing. This handler returns a JSON response with a status code of 500 (Internal Server Error) and a message containing the occurred exception.

## Server Start
At the end of the script, the `uvicorn.run` function is called to start the web server, listening on host `0.0.0.0` and port `5000`. This allows clients to access the API by sending HTTP requests to the specified host and port.
