import random
# You may create additional functions here:
board_size = 0
number_of_bombs = 0
bomb_locations = []
hidden_board = []
shown_board = []
list_with_first_column = []
holes_dug = 0
empty_locations = []

def play():
    
    gameSetUp()
    populateBombsList()
    populateBoardWithBombs()
    populateCellsNextToBombs()
    playGame()
    


#End of initial user input
######################################
def gameSetUp():
    global board_size 
    board_size = 0
    global number_of_bombs
    number_of_bombs = 0
    global hidden_board
    hidden_board.clear()
    global bomb_locations
    bomb_locations.clear()
    global list_with_first_column
    list_with_first_column.clear()
    global empty_locations
    empty_locations.clear()
    global shown_board
    shown_board.clear()

    print ("How big would you like the sides of the board to be?")

    board_size = int(input())

    if (board_size < 5 or board_size > 20):
        while (board_size < 5 or board_size > 20):
            if board_size < 5:
                print ("That size is too small.\nChoose a size bigger than 4.")
            else:
                print ("That size is too big.\nChoose a size smaller than 21.")
            board_size = int(input())


    for i in range (board_size):
        hidden_board.append(["0"] * board_size)
        shown_board.append([""] * board_size)
    # https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array

    print ("How many bombs should be present?")
    number_of_bombs = int(input())

    if (number_of_bombs >= board_size or number_of_bombs < 1):
        while (number_of_bombs >= (board_size * board_size) or number_of_bombs < 1):
            print (f"That is an invalid number of bombs.\nThe number should be bigger than 0 and less than the size of the board ({board_size} * {board_size} = " + str(board_size * board_size) + ")")
            number_of_bombs = int(input())
    

def populateBombsList():
    while len(bomb_locations) < number_of_bombs:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)
        if not bomb_locations.__contains__([x,y]):
            bomb_locations.append([x,y])

def populateBoardWithBombs():
    for i in range (number_of_bombs):
        hidden_board[bomb_locations[i][0]][bomb_locations[i][1]] = "*"


def drawBoard (board_used):
    if len(list_with_first_column) < board_size + 1:
        list_with_first_column.clear()
        list_with_first_column.append("y,x")
        for i in range (board_size):
            list_with_first_column.append(str(i))
    
    # https://stackabuse.com/padding-strings-in-python/
    # https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/#:~:text=The%20new%20line%20character%20in%20Python%20is%20%5Cn%20.,used%20to%20separate%20the%20lines.
    for i in  list_with_first_column:
        if i == "y,x":
            print(i.center(5, " "), end = "||")
        else:
            print(i.center(5, " "), end = "|")

    print("")
    print ("-".center(7,"-") * board_size)
    
    for i in range (len(board_used)):
        print(str(i).center(5, " ") , end ="||")
        for j in range (len(board_used)):
            print (board_used[i][j].center(5, " "), end = "|")
        print("")    
    print ("\n")

def populateCellsNextToBombs():
    for i in range(board_size):
        for j in range(board_size):
            if not hidden_board[i][j] == "*":

                counter = 0
                
                if i - 1 >= 0 and j - 1 >= 0:
                    if hidden_board[i - 1][j - 1] == "*":
                        counter += 1
                
                if j - 1 >= 0:
                    if hidden_board[i][j - 1] == "*":
                        counter += 1

                if i + 1 < board_size and j - 1 >= 0:
                    if hidden_board[i + 1][j - 1] == "*":
                        counter += 1

                if i - 1 >= 0:
                    if hidden_board[i - 1][j] == "*":
                        counter += 1

                if i + 1 < board_size:
                    if hidden_board[i + 1][j] == "*":
                        counter += 1

                if i - 1 >= 0 and j + 1 < board_size:
                    if hidden_board[i - 1][j + 1] == "*":
                        counter += 1

                if j + 1 < board_size:
                    if hidden_board[i][j + 1] == "*":
                        counter += 1

                if i + 1 < board_size and j + 1 < board_size:
                    if hidden_board[i + 1][j + 1] == "*":
                        counter += 1

                hidden_board[i][j] = str(counter)

def scores(Version):
    openFile = open("Minesweeper Scores.txt", "r")
    editableFile = openFile.readlines()
    openFile.close()
    fullScores = []
    
    for line in editableFile:
        tempScore = line.replace("\n", "").split(",")
        fullScores.append([tempScore[0],tempScore[1]])
    
    fullScores = sorted(fullScores, key = lambda x: x[1])
    # https://www.kite.com/python/answers/how-to-sort-a-multidimensional-list-by-column-in-python
    # https://datatofish.com/sort-list-python/

    if str(Version).isnumeric():
        if int(Version) > int(fullScores[0][1]):
            editableFile.pop(0)
            print ("Well done! You got a high score!\nPlease enter your name")
            name = input()
            editableFile.append(name + ","  + str(Version) + "\n")

            openFile = open("Minesweeper Scores.txt", "w")
            for line in editableFile:
                if not line.__contains__("\n"):
                    openFile.writelines(str(line) + "\n")
                else:
                    openFile.writelines(str(line))
            openFile.close()

    fullScores.clear()
    for line in editableFile:
        tempScore = line.replace("\n", "").split(",")
        fullScores.append([tempScore[0],tempScore[1]])
    fullScores = sorted(fullScores, key = lambda x: x[1])

    print("\n")
    print ("Player".ljust(20, " "), end = " ")
    print ("Score")
    print("_" * 30)
    for playerScore in fullScores:
        print (playerScore[0].ljust(20, " "), end = " ")
        print (playerScore[1])

    print ("\n\n")
    playAgain(Version)


def playAgain(Version):
    
    if Version == "Replay":
        print ("Would you like to (P)lay again, go back to the (M)ain Menu, view the (S)coreboard, or (Q)uit game")
    else:
        print ("Hello and Welcome to Minesweeper")
        print ("Choose an option:\n\n(P)lay Game\nView the (S)coreboard\n(Q)uit game")
    playAgainQuestion = input()
    playAgainQuestion = playAgainQuestion.lower()

    if playAgainQuestion == "p":
        play()
    
    elif playAgainQuestion == "m":
        playAgain("NewGame")

    elif playAgainQuestion == "s":
        scores(Version)
    
    elif playAgainQuestion == "q":
        exit()

    else:
        print ("\n\nThat is not valid option. Try again.")
        playAgain(Version)

def checkSurroundingEmptySquares():
    orignal_length = len(empty_locations)

    for location in empty_locations:
        # location = location.split(",")
        dig_location_y = location[0]
        dig_location_x = location[1]

        if (hidden_board[dig_location_y][dig_location_x] == "0"):
            if dig_location_y > 0:
                if hidden_board[dig_location_y - 1][dig_location_x] == "0":
                    if not empty_locations.__contains__([dig_location_y - 1, dig_location_x]):
                        empty_locations.append([dig_location_y - 1, dig_location_x])

            if dig_location_y + 1 < board_size:
                if hidden_board[dig_location_y + 1][dig_location_x] == "0":
                    if not empty_locations.__contains__([dig_location_y + 1, dig_location_x]):
                        empty_locations.append([dig_location_y + 1, dig_location_x])

            if dig_location_x > 0:
                if hidden_board[dig_location_y][dig_location_x - 1] == "0":
                    if not empty_locations.__contains__([dig_location_y, dig_location_x - 1]):
                        empty_locations.append([dig_location_y, dig_location_x - 1])

            if dig_location_x + 1 < board_size:
                if hidden_board[dig_location_y][dig_location_x + 1] == "0":
                    if not empty_locations.__contains__([dig_location_y, dig_location_x + 1]):
                        empty_locations.append([dig_location_y, dig_location_x + 1])

    if not orignal_length == len(empty_locations):
        checkSurroundingEmptySquares()

    else:
        for location in empty_locations:
            # location = location.split(",")
            dig_location_y = location[0]
            dig_location_x = location[1]
            shown_board[dig_location_y][dig_location_x] = hidden_board[dig_location_y][dig_location_x]
            
# shown_board[dig_location_y][dig_location_x] = hidden_board[dig_location_y][dig_location_x]



def playGame():
    global holes_dug
    holes_dug = 0
    print ("This is the empty board.")

    while True:
        print ("Where would you like to dig?\nGive your answer in the format \"y,x\"\n(Down, then across)")        

        drawBoard(hidden_board)
        drawBoard(shown_board)
        dig_location_y = ""
        dig_location_x = ""
        gameOver = False
        

        dig_location = input()

        while  (dig_location_x == "" or dig_location_y == ""):            
            if dig_location.__contains__(","):
                dig_location = dig_location.split(",")

                if dig_location[0].isnumeric and not dig_location[0] == "":
                    dig_location_y = int(dig_location[0])
                else: dig_location_y = ""
                if dig_location[1].isnumeric and not dig_location[1] == "":
                    dig_location_x = int(dig_location[1])
                else: dig_location_x = ""
            else:
                dig_location_y = ""
                dig_location_x = ""

            if dig_location_x == "" or dig_location_y == "":
                print ("That input is not valid\nGive your answer in the format \"y,x\"\n(Down, then across)")
                dig_location = input()
        

        if dig_location_x >= 0 and dig_location_x < board_size and dig_location_y >= 0 and dig_location_y < board_size:
            if shown_board[dig_location_y][dig_location_x] == "":
                holes_dug += 1
                if hidden_board[dig_location_y][dig_location_x] == "0":
                    empty_locations.append([dig_location_y, dig_location_x])
                    checkSurroundingEmptySquares()
            else:
                print ("That location has already been dug up. Try again on a different spot.")

            shown_board[dig_location_y][dig_location_x] = hidden_board[dig_location_y][dig_location_x]

            if hidden_board[dig_location_y][dig_location_x] == "*":
                print(f"\nYOU LOSE.\nYou managed to avoid the bombs {holes_dug} time(s).\n")
                gameOver = True

        else:
            print ("That is an invalid location. Try again.")

        if (holes_dug ==board_size * board_size - number_of_bombs):
            print(f"\nWINNER!.\nYou managed to all the bombs!.\nGood job!")
            gameOver = True
        
        if gameOver:
            drawBoard(shown_board)
            scores(holes_dug)
            playAgain("Replay")





    

# Additional Functions above this comment

# Implement your Minesweeper Solution Below:

# def play(dim_size, num_bombs):
    #Edit the code Below Here



    # pass
    #Edit the code Above Here
#play Function Ends Here


if __name__=='__main__':
    playAgain("NewGame")
    # scores(50)
    
    
