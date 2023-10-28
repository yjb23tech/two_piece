import random

class Enemy:

    def __init__(self, str_name, str_weapon_name):

        self.str_name = str_name
        self.str_weapon_name = str_weapon_name
        self.int_gold_value = random.randint(30, 50)
    
    def __str__(self):

        return (f"My name is Captain {self.str_name} ya sea faring bastard! If ye can beat me I'll give ya all me gold - {self.int_gold_value} coins to be exact!")


