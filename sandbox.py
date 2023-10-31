from Player import Player
from functions import set_player_name, set_player_age, set_player_home_city
from functions import active_tile_validation, proposed_tile_game_sequence, islands_conquered_checklist, available_action_direction_options
from Tile import MapTile, BattleTile
from data_structures import arr_world_map_back_end, arr_world_map_front_end, arr_world_map_islands_collection
from data_structures import action_options_travel_north, action_options_travel_east, action_options_travel_south, action_options_travel_west, action_options_game_quit
from data_structures import dict_action_horiz_vector_options, dict_action_vertical_vector_options

def play():

    bool_game_is_on = True 

    user_player = Player(set_player_name(), set_player_age(), set_player_home_city())
    print(user_player)

    while ((user_player.bool_game_has_been_won != True) and (bool_game_is_on == True)):

        print("\n===========================================================================================================================================\n")

        #Front End Render; solely concerned with visualisation - changes on the backend which manipulate the front end will be made further down in the code 
        for x in range(len(arr_world_map_front_end)):
            for y in range(len(arr_world_map_front_end[x])):
                print(arr_world_map_front_end[x][y], end="")
            print("")
        
        #Establish the Player's current location within the map before any decicions can be made to update their being within the game 
        user_player_current_tile_location = user_player.get_player_current_tile_location(arr_world_map_back_end)

        #Based on the Player's current location, dynamically present a series of viable options available to the Player
        #Based on the Player's current location, dynamically present a series of unviable options available to the Player
        available_action_direction_options(user_player, arr_world_map_back_end, dict_action_horiz_vector_options, dict_action_vertical_vector_options)

        
        #Prompt the Player to make a decision which has the ability to interact with the game based on the options above
        user_player_action = input(f"\nWhat would you like to do Captain {user_player.str_name}?\n")

        if user_player_action in action_options_travel_north:

            #Validation Series: a decision to travel North is equivalent to the following vector [0, 1]; Does this decision to travel North lead to an error? This must be established 
            proposed_tile = active_tile_validation(arr_world_map_back_end, user_player, 0, 1)
            proposed_tile_game_sequence(proposed_tile, arr_world_map_back_end, arr_world_map_front_end, user_player)
            islands_conquered_checklist(user_player, arr_world_map_islands_collection)
        
        elif user_player_action in action_options_travel_east:

            proposed_tile = active_tile_validation(arr_world_map_back_end, user_player, 1, 0)
            proposed_tile_game_sequence(proposed_tile, arr_world_map_back_end, arr_world_map_front_end, user_player)
            islands_conquered_checklist(user_player, arr_world_map_islands_collection)

        elif user_player_action in action_options_travel_south:

            proposed_tile = active_tile_validation(arr_world_map_back_end, user_player, 0, -1)
            proposed_tile_game_sequence(proposed_tile, arr_world_map_back_end, arr_world_map_front_end, user_player)
            islands_conquered_checklist(user_player, arr_world_map_islands_collection)

        elif user_player_action in action_options_travel_west:

            proposed_tile = active_tile_validation(arr_world_map_back_end, user_player, -1, 0)
            proposed_tile_game_sequence(proposed_tile, arr_world_map_back_end, arr_world_map_front_end, user_player)
            islands_conquered_checklist(user_player, arr_world_map_islands_collection)

        elif user_player_action in action_options_game_quit:
            user_player_action_quit_confirmation = input("Are you sure you'd like to (Q)uit? Please confirm once more by typing in the word 'QUIT'\n")
            if user_player_action_quit_confirmation in action_options_game_quit:
                print("See you soon Captain")
                bool_game_is_on = False
            else:
                print("The marathon continues")
        else:
            print("\nInvalid option: try again Captain!\n")
    

play()


