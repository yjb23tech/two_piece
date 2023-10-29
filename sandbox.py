from Player import Player
from functions import set_player_name, set_player_age, set_player_home_city
from Tile import MapTile, BattleTile
from data_structures import arr_world_map_back_end, arr_world_map_front_end
from data_structures import action_options_travel_north, action_options_travel_east, action_options_travel_south, action_options_travel_west, action_options_game_quit

def play():

    bool_game_is_on = True 

    #Things I need to only happen once
    user_player = Player(set_player_name(), set_player_age(), set_player_home_city())
    print(user_player)

    while ((user_player.bool_game_has_been_won != True) and (bool_game_is_on == True)):

        #Front End Render
        for x in range(len(arr_world_map_front_end)):
            for y in range(len(arr_world_map_front_end[x])):
                print(arr_world_map_front_end[x][y], end="")
            print("")
        
        user_player_current_tile_location = user_player.get_player_current_tile_location(arr_world_map_back_end)
        
        user_player_action = input(f"What would you like to do Captain {user_player.str_name}?\n")

        if user_player_action in action_options_travel_north:
            print("You're travelling North")
        elif user_player_action in action_options_travel_east:
            print("You're travelling East")
        elif user_player_action in action_options_travel_south:
            print("You're travelling South")
        elif user_player_action in action_options_travel_west:
            print("You're travelling West")
        elif user_player_action in action_options_game_quit:
            user_player_action_quit_confirmation = input("Are you sure you'd like to (Q)uit? Please confirm once more by typing in the word 'QUIT'\n")
            if user_player_action_quit_confirmation in action_options_game_quit:
                print("See you soon Captain")
                bool_game_is_on = False
            else:
                print("The marathon continues")
        else:
            print("Invalid option: try again Captain!")
    

play()


