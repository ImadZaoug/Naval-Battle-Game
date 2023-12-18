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
    # Récupération de l'objet de jeu correspondant à l'identifiant donné
        game = self.game_dao.find_game(game_id)
    # Création d'un objet joueur avec le nom donné
        player = Player(name=player_name)
    # Enregistrement du joueur en base de données
        player_entitiy = map_to_player_entity(player)
        self.game_dao.db_session.add(player_entitiy)
    # Ajout du joueur au jeu et retour du résultat de l'opération
        return game.add_player(player)

    def get_game(self, game_id: int) -> Game:
    # Récupération de l'objet de jeu correspondant à l'identifiant donné
        return self.game_dao.find_game(game_id)
        
    def add_vessel(self, game_id: int, player_name: str, vessel_type: str, x: int, y: int, z: int) -> bool:
    # Liste des types de navire disponibles
        L=[Aircraft,Cruiser,Destroyer,Frigate,Submarine]
    # Liste des noms de types de navire en minuscule
        l=["aircraft","cruiser","destroyer","frigate","submarine"]
    # Récupération de l'objet de jeu correspondant à l'identifiant donné
        game = self.get_game(game_id)
    # Pour chaque type de navire disponible,
        for i in range(len(l)):
        # Si le type de navire donné correspond au type de navire disponible,
            if vessel_type.lower() == l[i]:
            # On récupère l'objet navire correspondant
                vessel=L[i]
    # Pour chaque joueur du jeu,
        for k in range(len(game.players)):
        # Si le nom du joueur correspond au nom donné,
            if game.players[k].name == player_name:
            # On enregistre le navire en base de données et on l'ajoute au champ de bataille du joueur
                vessel_entity = map_to_vessel_entity(game.players[k].battlefield.id,vessel(x,y,z))
                self.game_dao.db_session.add(vessel_entity)
                game.players[k].battle_field.add_vessel(vessel_type(x,y,z))
            # On retourne vrai pour indiquer que l'ajout du navire a réussi
                return True
    # Si aucun joueur ne correspond au nom donné, on retourne faux
        return False

    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int, y: int, z: int) -> bool:
    # Récupération de l'objet de jeu correspondant à l'identifiant donné
        game = self.get_game(game_id)
    # Récupération de l'objet navire correspondant à l'identifiant donné
        vessel = self.game_dao.find_vessel(vessel_id)
    # Récupération de la liste des objets joueur du jeu
        players = game.get_players()
    # Création d'une liste de noms de joueurs dans le jeu
        players_in_the_game=[]
        for i in range(len(players)):
            players_in_the_game.append(players[i].name)
    # Itération sur chaque joueur
        for k in range(len(players)):
        # Si le nom du joueur actuel correspond au nom du tireur,
        # la boucle interne itère sur chaque navire du joueur et vérifie si l'identifiant du navire correspond à celui spécifié
            if players[k].name == shooter_name:
                for vessel in players[k].battle_field.vessels :
                    if vessel.id == vessel_id:
                    # Le navire tire à l'emplacement cible et les informations du navire sont mises à jour en base de données
                        vessel.fire_at(x,y,z)
                        vessel_entity = map_to_vessel_entity(game.players[k].battlefield.id,vessel)
                        self.game_dao.db_session.add(vessel_entity)
        # Si le nom du joueur actuel n'est pas celui du tireur, mais que le tireur est dans la liste des joueurs du jeu,
        # la boucle interne itère sur chaque navire du joueur et vérifie si les coordonnées du navire correspondent à celles spécifiées
            elif players[k].name != shooter_name and shooter_name in players_in_the_game:
                for vessel in players[k].battle_field.vessels :
                    if vessel.get_coordinates()==(x,y,z):
                        # Les informations du navire sont mises à jour en base de données
                        vessel_entity = map_to_vessel_entity(game.players[k].battlefield.id,vessel(x,y,z))
                        self.game_dao.db_session.add(vessel_entity)
                        # Retourne vrai pour indiquer que le navire a été touché
                        return True
    # Si aucun navire n'a été touché, retourne faux
        return  False
                        

    def get_game_status(self, game_id: int, shooter_name: str) -> str:
    # Récupération de l'objet de jeu correspondant à l'identifiant donné
        game = self.get_game(game_id)
    # Création d'un objet joueur à partir du nom donné
        player = Player(name=shooter_name)
    # Récupération de la liste des objets joueur du jeu
        players = game.get_players
    # Si l'objet joueur créé se trouve dans la liste des joueurs du jeu,
        if player in players :
        # il est retiré de la liste
            players.remove(player)
        # Le seul joueur restant est récupéré
            player_2 = players[0]
        # Si la puissance du navire du joueur créé est nulle, le statut de la partie est "Perdu"
            if player.battle_field.get_power() ==0:
                return "Perdu"
        # Si la puissance du navire du joueur restant est nulle, le statut de la partie est "Gagne"
            elif player_2.battle_field.get_power()==0:
                return "Gagne"
        # Sinon, le statut de la partie est "En cours"
            else :
                return "Encours"