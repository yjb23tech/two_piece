from Player import Player
from data_structures import dict_action_horiz_vector_options, dict_action_vertical_vector_options, arr_world_map_back_end

test_player = Player("Yuri Orlov", "29", "Odessa")

arr_available_action_directions = []
arr_unavailable_action_directions = []

print(" ")
for k in dict_action_horiz_vector_options:
    for v in dict_action_horiz_vector_options[k]:
        #print(f"[{k},{v}]")
        #print(dict_action_horiz_vector_options[k][v])

        potential_int_loc_x = test_player.int_loc_x + k
        potential_int_loc_y = test_player.int_loc_y + v

        #print(f"Possibilities: [{potential_int_loc_x}, {potential_int_loc_y}]\n")

        try:
            if potential_int_loc_x < 0:
                raise IndexError
            potential_tile = arr_world_map_back_end[potential_int_loc_x][potential_int_loc_y]

            arr_available_action_directions.append(dict_action_horiz_vector_options[k][v])
        except IndexError:
            arr_unavailable_action_directions.append(dict_action_horiz_vector_options[k][v])
        



print(" ")
for k in dict_action_vertical_vector_options:
    for v in dict_action_vertical_vector_options[k]:
        #print(f"[{k}, {v}]")
        #print(dict_action_vertical_vector_options[k][v])

        potential_int_loc_x = test_player.int_loc_x + k 
        potential_int_loc_y = test_player.int_loc_y + v
        
        #print(f"Possibilities: [{potential_int_loc_x}, {potential_int_loc_y}]")

        try:
            if potential_int_loc_y < 0:
                raise IndexError
            potential_tile = arr_world_map_back_end[potential_int_loc_x][potential_int_loc_y]

            arr_available_action_directions.append(dict_action_vertical_vector_options[k][v])
        except IndexError:
            arr_unavailable_action_directions.append(dict_action_vertical_vector_options[k][v])


print("You can travel:")
for available_action in arr_available_action_directions:
    if available_action in ['No Movement', 'Stationary']:
        pass
    else:
        print(available_action)
        
print("\nYou cannot travel:")
for unavailable_action in arr_unavailable_action_directions:
    print(unavailable_action)













