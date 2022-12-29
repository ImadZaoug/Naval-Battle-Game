from dao.game_dao import * 
from model.game import Game
from model.player import Player
from model.battlefield import Battlefield
from sqlalchemy import *
from sqlalchemy.orm import *
from email.mime import base
from sqlalchemy.ext.declarative import declarative_base

class GameService:
    def __init__(self):
        self.game_dao = GameDao()

    def create_game(self, player_name: str, min_x: int, max_x: int, min_y: int, max_y: int, min_z: int, max_z: int) -> int:
        game = Game()
        battle_field = Battlefield(min_x, max_x, min_y, max_y, min_z, max_z)
        game.add_player(Player(player_name, battle_field))
        return self.game_dao.create_game(game)

    def join_game(self, game_id: int, player_name: str) -> bool:
        game = self.game_dao.find_game(game_id)
        player = Player(name=player_name)
        return game.add_player(player)

    def get_game(self, game_id: int) -> Game:
        return self.game_dao.find_game(game_id)
        
    def add_vessel(self, game_id: int, player_name: str, vessel_type: str, x: int, y: int, z: int) -> bool:
        l=["Aircraft","Cruiser","Destroyer","Frigate","Submarine"]
        game = self.get_game(game_id)
        player = Player(player_name)
        if player in game.players:
            if vessel_type in l :
                player.battle_field.add_vessel(vessel_type(x,y,z))
            return True
        else:
            return False

    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int, y: int, z: int) -> bool:
        game = self.get_game(game_id)
        player = Player(name=shooter_name)
        vessel = self.game_dao.find_vessel(vessel_id)
        players = game.get_players
        if player in players :
            if vessel in player.battle_field.vessels :
                vessel.fire_at(x,y,z)
                return True
        else :
            return  False

    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        game = self.get_game(game_id)
        player = Player(name=shooter_name)
        players = game.get_players
        if player in players :
            players.remove(player)
            player_2 = players[0]
            if player.battle_field.get_power() ==0:
                return "Perdu"
            elif player_2.battle_field.get_power()==0:
                return "Gagne"
            else :
                return "Encours"