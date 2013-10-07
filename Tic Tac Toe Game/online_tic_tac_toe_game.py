# import the random library for random selection

import random

board = [0,1,2,
         3,4,5,
         6,7,8]

def show():
    print board[0],"|",board[1],"|",board[2]
    print "----------"
    print board[3],"|",board[4],"|",board[5]
    print "----------"
    print board[6],"|",board[7],"|",board[8]

def winCheck(char):
    lines = ["012","345","678","036","147","258","048","642"] # all possible winning combinations
    match = char * 3 # make a winning string to match to
    for line in lines:
        # For each item in the lines list, pull the integer from the index value of that item
        # Obtain that integer from board, then concatenate as a string for match comparison
        check = str(board[int(line[0])]) + str(board[int(line[1])]) + str(board[int(line[2])])
        if check == match:
            return True
            break # Are semicolons really necessary?

# Insert function to make the computer play smarter :-P 

show()

winner = "n" # Created this variable for a condition of running the while loop. 
             # Had issues with computer winning but still asking for selection

while winner == "n":
    selection = raw_input("Pick a spot to play in: ")
    selection = int(selection) # make sure the input is an integer
    
    if board[selection] != "x" and board[selection] != "o": # check the picked spot for signs of usage
        board[selection] = "x" # if it's not used, then use it!
        
        # check for a winner
        if winCheck("x") == True:
            print "You won!"
            winner = "y"
            break;
        
        
        while True:
            random.seed() # obtain a random number yo
            oponent = random.randint(0,8)
            
            if board[oponent] != "o" and board[oponent] != "x": # check the picked spot for signs of usage
                board[oponent] = "o" # if it's not used, then use it!
                
                #check for a winner
                if winCheck("o") == True:
                    print "You let the computer win!"
                    winner = "y"
                    break;
                    
                break;
    
    else:
        print "That spot is taken!" # otherwise, you're wrong!
    
    show()