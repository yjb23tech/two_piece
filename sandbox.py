from Player import Player
from functions import set_player_name, set_player_age, set_player_home_city
from Tile import MapTile, BattleTile
from data_structures import arr_world_map_back_end

def play():

    #Things I need to only happen once
    user_player = Player(set_player_name(), set_player_age(), set_player_home_city())
    print(user_player)

    #The actual game loop which runs indefinitely until one of two conditions are met: the game is one, or the player chooses to quit
    for x in range(len(arr_world_map_back_end)):
        for y in range(len(arr_world_map_back_end[x])):
            print(arr_world_map_back_end[x][y])
            print("\n")

play()


