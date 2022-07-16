def player_name():
    """
    runs a while loop to get a valid string of data from the user
    """
    while True:
        name = input("What is your name?: ")
        checkstr1 = name.isalpha()
        if checkstr1 == True:
            break
        else:
            print("please enter a correct name")
    return name

def settings_check():
    """
    This function asks the user if they want to play on default settings and if they do not want to they can change how many rows and columns they want (max 10)
    """
    while True:
        defualt = input("Would you like to play on defualt settings?(5 rows & 5 columns):(y/n) ")
        if defualt == "n":
            while True:
                rows = int(input("How many rows?(max 10): "))
                columns = int(input("How many columns?(max 10): "))
                if rows > 10 or columns > 10:
                    print("")
                    print("please put values lower then 10")
                    print("")
                else:
                    return rows, columns
                    break
        elif defualt == "y":
            rows = 5
            columns = 5
            return rows, columns
            break
        else:
            print("please put a valid input, either 'y' or 'n'")
        
    
def game():
    """
    will run all main fucntions
    """
    print("Welcome to BATTLESHIP!")
    print("----------------")
    name = player_name()
    gamesettings = settings_check()
    rows = gamesettings[0]
    columns = gamesettings[1]
    print(name)
    print("rows: " + str(rows))
    print("columns: " + str(columns))
    
game()