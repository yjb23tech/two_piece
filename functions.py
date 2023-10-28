def set_player_name() -> str:

    chosen_user_name = input("\nWhat is your name Sailor?\n")
    return chosen_user_name
        

def set_player_age() -> int:

    chosen_user_age = None

    while chosen_user_age == None:
        try:
            chosen_user_age = int(input("\nHow old are you Sailor?\n"))
            return chosen_user_age
        except ValueError:
            print("\nYou entered the wrong value; try again Sailor!")
            continue
    
#Might be interesting to combine this with some type of geographical API? Work with CRUD or basic API stuff... 
def set_player_home_city() -> str:

    chosen_user_home_city = input("\nAnd where are you from originally Sailor?\n")
    return chosen_user_home_city

