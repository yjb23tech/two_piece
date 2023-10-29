class Player:

    def __init__(self, str_name, int_age, str_place_of_birth):

        self.str_name = str_name 
        self.int_age = int_age
        self.str_place_of_birth = str_place_of_birth

        self.int_loc_x = 1 
        self.int_loc_y = 1 

        self.hp = 100 

        self.bool_game_has_been_won = False 
    
    def __str__(self):

        return (f"\nName: Captain {self.str_name}\nAge: {self.int_age}\nHome City: {self.str_place_of_birth}\n")
    
    def get_player_current_tile_location(self, arr_world_map_back_end):
        
        player_current_tile_location = arr_world_map_back_end[self.int_loc_x][self.int_loc_y]
        print(f"\nYou're currently on {player_current_tile_location.str_tile_name} Island in the {player_current_tile_location.str_tile_quadrant} quadrant of the map")
        print(f"Your current coordinate location is [{self.int_loc_x}, {self.int_loc_y}]\n")
        return player_current_tile_location


    


