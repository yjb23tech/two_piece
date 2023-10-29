from Player import Player
from functions import set_player_name, set_player_age, set_player_home_city
from Tile import MapTile, BattleTile
from data_structures import arr_world_map_back_end, arr_world_map_front_end

def play():

    bool_game_is_on = True 

    #Things I need to only happen once
    user_player = Player(set_player_name(), set_player_age(), set_player_home_city())
    print(user_player)

    while ((user_player.bool_game_has_been_won != True) and (bool_game_is_on == True)):

        #The actual game loop which runs indefinitely until one of two conditions are met: the game is one, or the player chooses to quit
        #Back End Render
        for x in range(len(arr_world_map_back_end)):
            for y in range(len(arr_world_map_back_end[x])):
                print(arr_world_map_back_end[x][y])
                print("\n")
    
        #Front End Render
        for x in range(len(arr_world_map_front_end)):
            for y in range(len(arr_world_map_front_end[x])):
                print(arr_world_map_front_end[x][y], end="")
            print("")
        
        arr_world_map_front_end[10][2] = " V "
        arr_world_map_front_end[10][3] = " "

        print(" ")

        for x in range(len(arr_world_map_front_end)):
            for y in range(len(arr_world_map_front_end[x])):
                print(arr_world_map_front_end[x][y], end="")
            print("")
        

        bool_game_is_on = False

play()


