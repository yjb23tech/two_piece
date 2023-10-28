from enemy import Enemy
from Tile import MapTile, BattleTile

arr_world_map_pvp_bosses = [

    [Enemy("Kaido", "Hassaikai"), Enemy("Enel", "Thunder Lance"), Enemy("Red Shanks", "Rapier")], 
    [Enemy("Big Mom", "Long Sword"), Enemy("Dragan", "Mystery"), Enemy("Wapol", "Steel Gauntlets")], 
    [Enemy("Sir Crocodile", "Gaunlet Hook"), Enemy("Hody Jones", "Trident"), Enemy("BlackBeard", "Long Gun")]
]

#Tested; this works very well 
arr_world_map = [

    [BattleTile(0, 0, "Wano", "South Western", arr_world_map_pvp_bosses[0][0]), BattleTile(0, 1, "Skypeia", "Western", arr_world_map_pvp_bosses[0][1]), BattleTile(0, 2, "Elbaf", "North Western", arr_world_map_pvp_bosses[0][2])],
    [BattleTile(1, 0, "Wholecake", "Southern", arr_world_map_pvp_bosses[1][0]), BattleTile(1, 1, "Romance Dawn", "Central", arr_world_map_pvp_bosses[1][1]), BattleTile(1, 2, "Drum", "Northern", arr_world_map_pvp_bosses[1][2])],
    [BattleTile(2, 0, "Alabasta", "Eastern", arr_world_map_pvp_bosses[2][0]), BattleTile(2, 1, "Fishman", "Eastern", arr_world_map_pvp_bosses[2][1]), BattleTile(2, 2, "Hachinosu", "North Eastern", arr_world_map_pvp_bosses[2][2])]
]


#for x in range(len(arr_world_map)):
#for y in range(len(arr_world_map[x])):
#print(arr_world_map[x][y])
#print("\n")

