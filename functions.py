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

def available_action_options(user_player, arr_world_map_backend, dict_horiz_actions, dict_vert_actions):

    arr_available_action_options = []
    arr_unavailable_action_options = []

    for x in dict_horiz_actions:
        for y in dict_horiz_actions[x]:

            potential_int_loc_x = user_player.int_loc_x + x
            potential_int_loc_y = user_player.int_loc_y + y 

            try:
                if potential_int_loc_x < 0:
                    raise IndexError
                potential_tile = arr_world_map_backend[potential_int_loc_x][potential_int_loc_y]
                arr_available_action_options.append(dict_horiz_actions[x][y])

            except IndexError:
                arr_unavailable_action_options.append(dict_horiz_actions[x][y])
    
    for x in dict_vert_actions:
        for y in dict_vert_actions[x]:

            potential_int_loc_x = user_player.int_loc_x + x 
            potential_int_loc_y = user_player.int_loc_y + y 

            try:
                if potential_int_loc_y < 0:
                    raise IndexError
                potential_tile = arr_world_map_backend[potential_int_loc_x][potential_int_loc_y]
                arr_available_action_options.append(dict_vert_actions[x][y])
            except IndexError:
                arr_unavailable_action_options.append(dict_vert_actions[x][y])
    

    a = 1
    print(f"You can travel in the following directions:\n")
    for available_action in arr_available_action_options:
        if available_action in ['No Movement', 'Stationary']:
            pass
        else:
            print(f"{a}. {available_action}")
            a += 1
    
    if ((len(arr_unavailable_action_options)) == 0):
        pass
    else:
        b = 1
        print(f"You cannot travel in the following directions:\n")
        for unavailable_action in arr_unavailable_action_options:
            print(f"{b}. {unavailable_action}")
            b += 1 
    

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
        user_player.arr_islands_conquered.append(proposed_tile.str_tile_name)
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
    

def islands_conquered_checklist(user_player, arr_world_map_islands_collection):

    arr_conquered_islands = []
    arr_unconquered_islands = []

    if (len(user_player.arr_islands_conquered) == 0):
        pass
    else:

        for island in arr_world_map_islands_collection:

            if island in user_player.arr_islands_conquered:
                arr_conquered_islands.append(island)

            else:
                arr_unconquered_islands.append(island)
        
        print(f"YeeHaw! Captain {user_player.str_name}! You have conquered the following islands:\n")
        x = 1
        for island in arr_conquered_islands:
            print(f"{x}. {island} Island")
            x += 1
        
        if len(arr_unconquered_islands) != 0:
            print(f"\nYou still have the following islands to conquer:\n")
            y = 1
            for island in arr_unconquered_islands:
                print(f"{y}. {island} Island")
                y += 1 
            
            user_player.bool_game_has_been_won = False
        else:

            print(f"Congrulations {user_player.str_name} you have conquered all of the islands - the game is complete XD")
            user_player.bool_game_has_been_won = True


        

            


