#The actual game loop which runs indefinitely until one of two conditions are met: the game is one, or the player chooses to quit
        #Back End Render
        for x in range(len(arr_world_map_back_end)):
            for y in range(len(arr_world_map_back_end[x])):
                print(arr_world_map_back_end[x][y])
                print("\n")


arr_world_map_front_end[10][2] = " V "
        arr_world_map_front_end[10][3] = " "

        print(" ")

        for x in range(len(arr_world_map_front_end)):
            for y in range(len(arr_world_map_front_end[x])):
                print(arr_world_map_front_end[x][y], end="")
            print("")


if active_tile == None:
                print("Try again Captain; make another decision")
            else:
                print(active_tile)
                #Battle Sequence
                #Victory Sequence [update the map, update the player's current location, check to see what islands the player has conquered, what islands are left]
                user_player.set_player_current_tile_location(active_tile)

                #At the end of each sequence...
                #Player location must be updated
                #FrontEnd must be updated to show that the Island has been conquered 

if active_tile == None:
                print("Try again Captain; make another decision")
            else:
                print(active_tile)
                user_player.set_player_current_tile_location(active_tile)

#Player should have the option to choose from a collection of weapons
                #Player should also be able to pick their strongest weapon 
                user_player.get_weapon()

                if user_player.obj_weapon_in_hand == None:
                    print(f"Unarmed; please choose a weapon Captain {user_player.str_name} ")
                    user_player.set_weapon()
                else: