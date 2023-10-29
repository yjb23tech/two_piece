class Player:

    def __init__(self, str_name, int_age, str_place_of_birth):

        self.str_name = str_name 
        self.int_age = int_age
        self.str_place_of_birth = str_place_of_birth

        self.hp = 100 

        self.bool_game_has_been_won = False 
    
    def __str__(self):

        return (f"\nName: Captain {self.str_name}\nAge: {self.int_age}\nHome City: {self.str_place_of_birth}\n")

