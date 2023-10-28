from Player import Player
from functions import set_player_name, set_player_age, set_player_home_city
from Tile import MapTile, BattleTile

def play():

    #Things I need to only happen once
    user_player = Player(set_player_name(), set_player_age(), set_player_home_city())
    print(user_player)

    test_battle_tile = BattleTile(1, 1, "Dressrosa", "South East", "PlaceHolder")
    print(test_battle_tile)


play()


