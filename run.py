def player_name():
    """
    runs a while loop to get a valid string of data from the user
    """
    while True:
        name = input("What is your name?: ")
        checkstr1 = name.isalpha()
        if checkstr1 == True:
            break
    return name
    

def game():
    """
    will run all main fucntions
    """
    player_name()
    
game()