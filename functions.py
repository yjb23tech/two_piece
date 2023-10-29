def set_player_name() -> str:

    chosen_user_name = input("\nWhat is your name Sailor?\n")
    return chosen_user_name
        

def set_player_age() -> int:

    chosen_user_age = None

    while chosen_user_age == None:
        try:
            chosen_user_age = int(input("\nHow old are you Sailor?\n"))
            return chosen_user_age
        except ValueError:
            print("\nYou entered the wrong value; try again Sailor!")
            continue
    
#Might be interesting to combine this with some type of geographical API? Work with CRUD or basic API stuff... 
def set_player_home_city() -> str:

    chosen_user_home_city = input("\nAnd where are you from originally Sailor?\n")
    return chosen_user_home_city

def active_tile_validation(arr_world_map_backend, user_player, chosen_direction_int_loc_x, chosen_direction_int_loc_y):
    
    proposed_int_loc_x = user_player.int_loc_x + chosen_direction_int_loc_x
    proposed_int_loc_y = user_player.int_loc_y + chosen_direction_int_loc_y 

    try:

        if ((proposed_int_loc_x < 0) or (proposed_int_loc_y < 0)):
            raise IndexError
    
        active_tile = arr_world_map_backend[proposed_int_loc_x][proposed_int_loc_y]
        return active_tile
    except IndexError:
        print("\nThose are uncharted waters ye be seeking... tis unsafe to go where no man has gone before...")
        return None

def update_game_settings_battle_pass(proposed_tile, arr_world_map_backend, arr_world_map_front_end, user_player):

    if proposed_tile.str_tile_type == "Battle Tile": 

        print(f"Well done Captain {user_player.str_name}! In lieu of your great win, this quadrant on the map will be updated with the letter V for victory XD\n")
        arr_world_map_front_end[proposed_tile.int_loc_x_tile_quadrant_label_a][proposed_tile.int_loc_y_tile_quadrant_label_a] = " V "
        arr_world_map_front_end[proposed_tile.int_loc_x_tile_quadrant_label_b][proposed_tile.int_loc_y_tile_quadrant_label_b] = " "
        user_player.set_player_current_tile_location(proposed_tile)
    elif proposed_tile.str_tile_type == "Trading Tile":
        user_player.set_player_current_tile_location(proposed_tile)
    else:
        pass

def proposed_tile_game_sequence(proposed_tile, arr_world_map_backend, arr_world_map_front_end, user_player):

    if proposed_tile == None:
        print("Try again Captain; make a better decision\n")
    else:

        print(proposed_tile)

        #Trade
        #Fight
        proposed_tile.pvp_sequence_against_tile_boss(user_player)
        update_game_settings_battle_pass(proposed_tile, arr_world_map_backend, arr_world_map_front_end, user_player)
    


