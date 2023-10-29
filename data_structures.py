from enemy import Enemy
from Tile import MapTile, BattleTile

arr_world_map_pvp_bosses = [

    [Enemy("Kaido", "Hassaikai"), Enemy("Enel", "Thunder Lance"), Enemy("Red Shanks", "Rapier")], 
    [Enemy("Big Mom", "Long Sword"), Enemy("Dragan", "Mystery"), Enemy("Wapol", "Steel Gauntlets")], 
    [Enemy("Sir Crocodile", "Gaunlet Hook"), Enemy("Hody Jones", "Trident"), Enemy("BlackBeard", "Long Gun")]
]

#Tested; this works very well 
arr_world_map_back_end = [

    [BattleTile(0, 0, "Wano", "South Western", arr_world_map_pvp_bosses[0][0], 10, 2), BattleTile(0, 1, "Skypeia", "Western", arr_world_map_pvp_bosses[0][1], 6, 2), BattleTile(0, 2, "Elbaf", "North Western", arr_world_map_pvp_bosses[0][2], 2, 2)],
    [BattleTile(1, 0, "Wholecake", "Southern", arr_world_map_pvp_bosses[1][0], 10, 6), BattleTile(1, 1, "Romance Dawn", "Central", arr_world_map_pvp_bosses[1][1], 6, 6), BattleTile(1, 2, "Drum", "Northern", arr_world_map_pvp_bosses[1][2], 2, 6)],
    [BattleTile(2, 0, "Alabasta", "South Eastern", arr_world_map_pvp_bosses[2][0], 10, 10), BattleTile(2, 1, "Fishman", "Eastern", arr_world_map_pvp_bosses[2][1], 6, 10), BattleTile(2, 2, "Hachinosu", "North Eastern", arr_world_map_pvp_bosses[2][2], 2, 10)]
]

#Tested; this works very well 
arr_world_map_front_end = [

    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *"], 
    ["*", "  ", " NW", " ", " *", "  ", " N ", " ", " *", "  ", " NE", " ", " *"], 
    ["*", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *"], 
    ["*", "  ", " W ", " ", " *", "  ", " C ", " ", " *", "  ", " E ", " ", " *"], 
    ["*", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *"], 
    ["*", "  ", " SW", " ", " *", "  ", " S ", " ", " *", "  ", " SE", " ", " *"], 
    ["*", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *", "  ", "  ", "  ", " *"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"]
]

action_options_travel_north = ['North', 'NORTH', 'north', 'N', 'n', '^']
action_options_travel_east = ['East', 'EAST', 'east', 'E', 'e', '>']
action_options_travel_south = ['South', 'SOUTH', 'south', 'S', 's', 'v']
action_options_travel_west = ['West', 'WEST', 'west', 'W', 'w', '<']
action_options_game_quit = ['Quit', 'QUIT', 'quit', 'Q', 'q']