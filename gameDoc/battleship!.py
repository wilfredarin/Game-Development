from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(1, len(board)+1)

def random_col(board):
    return randint(1, len(board[0])+1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
#print (ship_col)
name=input("what's your name?:")
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(3):
    print ("Turn",turn+1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print(( "CONGRATULATIONS!!! %s  You sunk my battleship!")%(name))
        break
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1     or guess_col > 5):
         print ("Oops,%s  that's not even in the ocean!!")%(name)
        elif(board[guess_row-1][guess_col-1] == "X"):
            print ("You guessed that one already.")
            print (print_board(board))
        else:
            print (("You missed my battleship!!! %s ")%(name))
            board[guess_row-1][guess_col-1] = "X"
            print (print_board(board))
            if turn==2:
                print (("Game Over %s!!! ")%(name))

    