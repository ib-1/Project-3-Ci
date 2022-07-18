from random import randint

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

def grid_size():
    """
    this function ask the user if they want the default grid size or they can choose a custom grid size but the max is 10 or the grid will be too big and minimunm 3 or else it will be too small 
    """
    while True:
        defualt = input("Would you like to play with the defualt grid?(5 rows & 5 columns):(y/n) ").lower()
        if defualt == "n":
            while True:
                # grid_size = int(input("How big would you like your grid?(max 10, min 3): "))
                grid_size = 0
                try:
                    grid_size = int(input("How big would you like your grid?(max 10, min 3): "))
                except ValueError:
                    print("make sure you're putting a number!")
                if grid_size > 10:
                    print("")
                    print("please put a value between 3-10")
                    print("")
                elif grid_size < 3:
                    print("")
                    print("please put a value between 3-10")
                    print("")
                else:
                    return grid_size
                    break
        elif defualt == "y":
            grid_size = 5
            return grid_size
            break
        else:
            print("")
            print("please put a valid input, either 'y' or 'n'")
            print("")

def ship_settings():
    """
    This function asks the user how many ships will be on the map but the max is 8 so there inst too many ships
    """
    while True:
        shipssetting = input("Would you like to play with the default amount of ships?(4 ships)(max 8 ships):(y/n) ").lower()
        if shipssetting == "n":
            while True:
                ships = 0
                try:
                    ships = int(input("How many ships would you like(max 8, min 1): "))
                except ValueError:
                    print("make sure you're putting a number!")
                if ships > 8:
                    print("")
                    print("please enter a value between 1-8")
                    print("")
                elif ships < 1:
                    print("")
                    print("please enter a value between 1-8")
                    print("")
                else:
                    return ships
                    break
        elif shipssetting == "y":
            ships = 4
            return ships
            break
        else:
            print("")
            print("please put a valid input, either 'y' or 'n'")
            print("")
        
    
def create_board(gridsize, ship_count):
    """
    This function will create a board for either the player or the computer and designate the ship spots marked by x
    """
    board = []
    for i in range(0, gridsize):
        board.append(["O"] * gridsize)
    def ship_location(ship_count):
        row = []
        column = []
        coordinates = []
        F = 0
        while F < ship_count:
            x = randint(0, gridsize - 1)
            y = randint(0, gridsize - 1)
            for i in coordinates:
                if i == [x,y]:
                   print("dupe" + str(i) + str([x,y]))  # this will get rid of all duplicate cords so ships do not overlay
                   coordinates.clear()
                   row.clear()
                   column.clear() 
                   F = 0
            coordinates.append([x,y])
            row.append(x)
            column.append(y)
            F += 1
        for i in range(0, ship_count):
            board[row[i]][column[i]] = "x"
    ship_location(ship_count)
    return board

def print_board(board):
    for i in board:
        print(" ".join(i))

def display_game(player_board, display_game, alt_board):
    """
    this function will display the game with the computers board not being visible so the user does not know where the enenmy ship is 
    """
    print("Users board: ")
    print_board(player_board)
    print("")
    print("Computers board: ")
    print_board(alt_board)

def user_guess():
    while True:
        row = input("Row: ")
        column = input("Columm: ")
        


def game():
    """
    will run all main fucntions
    """
    print("Welcome to BATTLESHIP!")
    print("----------------")
    name = player_name()
    gridsize = grid_size()
    ship_count = ship_settings()
    print(name)
    print("Grid Size: " + str(gridsize))
    print("Ships: " + str(ship_count))
    player_board = create_board(gridsize, ship_count) 
    computer_board = create_board(gridsize, ship_count)
    alt_board = create_board(gridsize, 0)
    display_game(player_board, display_game, alt_board)
    
game()

