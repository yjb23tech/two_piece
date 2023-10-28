class MapTile:

    def __init__(self, int_loc_x, int_loc_y, str_tile_name, str_tile_quadrant):

        self.int_loc_x = int_loc_x
        self.int_loc_y = int_loc_y
        self.str_tile_name = str_tile_name
        self.str_tile_quadrant = str_tile_quadrant
    
    def __str__(self):

        raise NotImplementedError("Create a sublass instead!")

class BattleTile(MapTile):

    def __init__(self, int_loc_x, int_loc_y, str_tile_name, str_tile_quadrant, obj_tile_pvp_boss):

        self.obj_tile_pvp_boss = obj_tile_pvp_boss

        super().__init__(int_loc_x, int_loc_y, str_tile_name, str_tile_quadrant)
    
    def __str__(self):

        return (f"Welcome to {self.str_tile_name} Island in the {self.str_tile_quadrant} quadrant of the Map, coordinates [{self.int_loc_x}, {self.int_loc_y}]")


    

    
