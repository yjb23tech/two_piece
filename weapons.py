import random

class Weapon:

    def __init__(self, str_weapon_name, str_weapon_title):

        self.str_weapon_name = str_weapon_name
        self.str_weapon_title = str_weapon_title
        self.int_atk_pwr = random.randint(40, 60)
    
    def __str__(self):

        return (f"This is {self.str_weapon_title}; it is a {self.str_weapon_name} and has an attack power of {self.int_atk_pwr}")
    

class DoubleAxe(Weapon):

    def str_victory_msg(self):

        return (f"All must kneel at the feet of {self.str_weapon_title}, destroyer of men")

class BroadSword(Weapon):

    def str_victory_msg(self):

        return (f"Those who seek to rise against me shall be felled by the almighty {self.str_weapon_title}")

class LongGun(Weapon):

    def str_victory_msg(self):

        return (f"There isn't a target I can't hit with my trusty {self.str_weapon_title}")

