from weapons import DoubleAxe, BroadSword, LongGun

class Player:

    def __init__(self, str_name, int_age, str_place_of_birth):

        self.str_name = str_name 
        self.int_age = int_age
        self.str_place_of_birth = str_place_of_birth

        self.int_loc_x = 1
        self.int_loc_y = 1

        self.hp = 100 

        self.obj_weapon_in_hand = None
        self.arr_objs_weapons_inventory = [DoubleAxe("Double Axe", "Mjolnir"), BroadSword("Broad Sword", "Requiem"), LongGun("Long Gun", "Flying Death")]

        self.arr_islands_conquered = []

        self.bool_game_has_been_won = False 
    
    def __str__(self):

        return (f"\nName: Captain {self.str_name}\nAge: {self.int_age}\nHome City: {self.str_place_of_birth}\n")
    
    def get_player_current_tile_location(self, arr_world_map_back_end):
        
        player_current_tile_location = arr_world_map_back_end[self.int_loc_x][self.int_loc_y]
        print(f"\nYou're currently on {player_current_tile_location.str_tile_name} Island in the {player_current_tile_location.str_tile_quadrant} quadrant of the map")
        print(f"Your current coordinate location is [{self.int_loc_x}, {self.int_loc_y}]\n")
        return player_current_tile_location
    
    def set_player_current_tile_location(self, active_tile):

        self.int_loc_x = active_tile.int_loc_x
        self.int_loc_y = active_tile.int_loc_y 
    
    def get_weapon(self):
        return self.obj_weapon_in_hand

    def set_weapon(self):

        print(f"\nYou have the following weapons available to you Captain:\n")

        current_weapons_inventory = self.arr_objs_weapons_inventory

        for x, weapon in enumerate(current_weapons_inventory, 1):
            print(f"{x}. {weapon}")

        valid_weapon_selection = False
        
        while valid_weapon_selection == False:
            try:
                chosen_weapon = int(input("\nUsing the number pad, enter the number corresponding to your weapon of choice:\n"))
                self.obj_weapon_in_hand = current_weapons_inventory[chosen_weapon - 1]
                print(f"You have chosen to wield the {self.obj_weapon_in_hand.str_weapon_name}; happy hunting Sailor!")
                valid_weapon_selection = True
            except ValueError:
                print(f"\nInvalid weapon selection; try again")
            except IndexError:
                print(f"\nInvalid weapon selection; try again")



    


