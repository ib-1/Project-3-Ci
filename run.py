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
                if i == [x,y]: # clears any dupe ships and runs the code again
                   coordinates.clear()
                   row.clear()
                   column.clear() 
                   F = 0
            coordinates.append([x,y])
            row.append(x)
            column.append(y)
            F += 1
        for i in range(0, ship_count):
            board[row[i]][column[i]] = "*"
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

def user_guess(gridsize):
    """
    this function will ask the user for thier guess of row and column
    """
    max = gridsize - 1
    print("Top left corner is row: 0, col: 0")
    while True:
        try:
            row = int(input("Row: "))
            if row > max:
                print("please put a value lower or equal to " + str(max))
            elif row < 0:
                print("please put a number higher then 0")
            else:
                break
        except ValueError:
                print("make sure you're putting a number!")
    while True:
        try:
            column = int(input("Column: "))
            if column > max:
                print("please put a value lower or equal to " + str(max))
            elif column < 0:
                print("please put a number higher then 0")
            else:
                break
        except ValueError:
                print("make sure you're putting a number!")
    return row, column
        

def computer_guess(gridsize):
    """
    this function will calculate the computers guess
    """
    max = gridsize - 1
    row = randint(0, max)
    column = randint(0, max)
    return row, column

def update_game(player_board, userguess, computer_board, computerguess, user_score, computer_score, alt_board):
    """
    this function will take all the information we have gathered and update the output of the game
    """
    user_mark = player_board[computerguess[0]][computerguess[1]]
    print(user_mark)
    player_board[computerguess[0]][computerguess[1]] = "x"
    computer_mark = computer_board[userguess[0]][userguess[1]]
    print(computer_mark)
    alt_board[userguess[0]][userguess[1]] = "x"
    if user_mark == "*":
        print("The computer hit one of your ships!")
        return 0, 1
    if computer_mark == "*":
        print("you hit a computers ship!" )
        return 1, 0
    else:
        return 0, 0
    



def game_over():
    print("-------------------")
    print("Thank you for playing my game - ib")
    print("-------------------")



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
    user_score = 0
    computer_score = 0
    while True:
        userguess = user_guess(gridsize)
        computerguess = computer_guess(gridsize)
        score = update_game(player_board, userguess, computer_board, computerguess, user_score, computer_score, alt_board) 
        if score[0] == 1:
            user_score += 1
        elif score[1] == 1:
            computer_score += 1
        else:
            print("no hits")
        display_game(player_board, display_game, alt_board)
        print("-------------------")
        print(name + "'s score: " + str(user_score))
        print("computers score: " + str(computer_score))
        print("-------------------")
        if user_score == ship_count:
            print("YOU WIN!!!!")
            break
        elif computer_score == ship_count:
            print("uh oh, you lose... computer wins!")
            break
    game_over()
    
game()

