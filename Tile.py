class MapTile:

    def __init__(self, str_tile_type, int_loc_x, int_loc_y, str_tile_name, str_tile_quadrant, int_loc_x_tile_quadrant_label_a, int_loc_y_tile_quadrant_label_a):

        self.str_tile_type = str_tile_type

        self.int_loc_x = int_loc_x
        self.int_loc_y = int_loc_y
        self.str_tile_name = str_tile_name
        self.str_tile_quadrant = str_tile_quadrant

        self.int_loc_x_tile_quadrant_label_a = int_loc_x_tile_quadrant_label_a
        self.int_loc_y_tile_quadrant_label_a = int_loc_y_tile_quadrant_label_a


        self.int_loc_x_tile_quadrant_label_b = int_loc_x_tile_quadrant_label_a
        self.int_loc_y_tile_quadrant_label_b = int_loc_y_tile_quadrant_label_a + 1 
    
    def __str__(self):

        raise NotImplementedError("Create a sublass instead!")

class BattleTile(MapTile):

    def __init__(self, str_tile_type, int_loc_x, int_loc_y, str_tile_name, str_tile_quadrant, obj_tile_pvp_boss, int_loc_x_tile_quadrant_label_a, int_loc_y_tile_quadrant_label_a):

        self.obj_tile_pvp_boss = obj_tile_pvp_boss

        super().__init__(str_tile_type, int_loc_x, int_loc_y, str_tile_name, str_tile_quadrant, int_loc_x_tile_quadrant_label_a, int_loc_y_tile_quadrant_label_a)
    
    def __str__(self):

        battle_tile_welcome_msg = (f"\nWelcome to {self.str_tile_name} Island located in the {self.str_tile_quadrant} quadrant of the Map, coordinates [{self.int_loc_x}, {self.int_loc_y}]")
        battle_tile_pvp_boss_msg = (f"Be careful young sailor... the Captain of this island is none other than the infamous {self.obj_tile_pvp_boss.str_name}")

        return (f"{battle_tile_welcome_msg}\n{battle_tile_pvp_boss_msg}")
    
    def pvp_sequence_against_tile_boss(self, user_player):

        tile_boss = self.obj_tile_pvp_boss

        if tile_boss.int_hp <= 0:
            print("NFA")
        else:

            user_player.get_weapon()
            if user_player.obj_weapon_in_hand == None:
                print(f"\nOh no you're unarmed :S Please choose a weapon immediately Captain {user_player.str_name}!")
                user_player.set_weapon()
            
            print("\nLet's fight!\n")
            while tile_boss.int_hp > 0:

                print(f"{user_player.str_name} lands a devastating blow on {tile_boss.str_name}! {tile_boss.str_name} has lost {user_player.obj_weapon_in_hand.int_atk_pwr} health points!")
                tile_boss.int_hp -= user_player.obj_weapon_in_hand.int_atk_pwr 
            
            print(f"\n{tile_boss.str_name} has been defeated!")











    

    
