##tic tac toe program

import random

import copy

import time

def blank_board(): 
    blankboard=[]

    for y in range(3):
        innerlist=[]
        for x in range(3):
            innerlist.append(None)

        blankboard.append(innerlist)

    return blankboard

def render(board):


    print('   0  1  2')

    print(' +'+'-'*9+'+')

    for y in range(3):
        print(y,end='')
        print('|', end='')
        for x in range(3): 
            
            ##FORMATTING PRINT
            if board[y][x] == None:
                print('   ',end='')

            ##PLAYER 1 PRINT
            if board[y][x] == 0:
                print(' X ',end='')
            
            ##PLAYER 2 PRINT 
            if board[y][x] == 1:
                print(' O ',end='')
            
        print('|')

    print(' +'+'-'*9+'+')
        
    return(board)



def make_move(board,coordinates,player):

    ## this doesnt work. you will show each move that a player has inputted, but you will wipe
    ## the memory of what has occured each time a player gives a move
    ## instead, you need to copy the contents of the existing board into a new variable
    ## a new variable that makes no reference to board, so that we dont create
    ## an extra pointer to board. we can do this by reading off the contents
    ##and writing them using a for loop of some sort 
    #new_board=blank_board() this is WRONG
    #new_board=board this is WRONG, creates an extra pointer to board and all updates to        
    ## new_board will also update board, creating a mutable reference point
    ## we want the initial board to be immutable, mutating the NEW copy instead
    ## OVERALL: READ from the feed in, CHANGE on the copy 
    ## in this scenario we need to REMEMBER the last board everytime, so DONT overwrite a blank in this

    #create an empty list
    new_board=[]

    #goes through each row in board
    for row in board:
        #copies all the contents of that row
        new_row=row[:]
        #appends them into the new board
        new_board.append(new_row)

    x,y=coordinates

    ##player 1 prints 'X'  (according to render module)

    if player==0:
        new_board[y][x]=0

    ##player 2 prints 'O"  (acording to render module)
    if player==1:
        new_board[y][x]=1

    return new_board


def is_valid_move(board, coordinates):

    
    ## checks if they are within the 0/2 constriction of our board
    if not coordinates:
        return False
    
    ## grabs x,y coords that got fed in

    x,y=coordinates

    if x<0 or x>2 or y<0 or y>2:
        return False

    ##checks if there is nothing there- if both conditiosn met, return a true 
    ##fixed from == None, its just a logical statement, more exact.
    if board[y][x] is None:
        return True
    
    #if board [y][x]!=None:
    else:
        return False
    
def human_player(board,player):

    
    try:
        x_move=int(input('What column do you choose (0-2):' ))
        y_move=int(input('What row do you chose (0-2):' ))

        move_tuple=(x_move,y_move)

        return move_tuple
    
    except ValueError:
        print('')
        

def random_ai(board, player): 

    ## to randomly select something we should import the random library for help
    ## we can scan the board at each iteration and import the address of each None into a new list
    ## then we can use the random.choice() function from random library
    ## this will choose a random tuple that we stored in that list we stored in

    emptylist=[]


    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                emptylist.append((column,row))

    if len(emptylist)>0:
        ai_tuple=random.choice(emptylist)
        return ai_tuple
    
    else:
        
        return False
    
def finds_winning_moves_ai(board, player):

    emptylist=[]

    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                emptylist.append((column,row))

    
    ##go througgh all the possible moves
    ##simulate a move, and check if it fulfills a win condition
    ## if the win condition returns as true, return the coordinates
    ##if it didnt, try again, keep trying until nothing else,
    ## at which point, make a random move
    for coordinate in emptylist:
        x,y=coordinate
        simulatedboard=copy.deepcopy(board)
        simulatedboard[y][x]=player 

        ## checks if they return true, if so, execute
        if O_checks(simulatedboard) or X_checks(simulatedboard): 
            return coordinate 
        
    
    ##if we have no winning moves just make a random choice 

    if len(emptylist)>0:
        ai_tuple=random.choice(emptylist)
        return ai_tuple
            
    else:
        
        return False
    

def finds_winning_and_losing_moves(board, player):

    emptylist=[]

    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                emptylist.append((column,row))

    
    ##go througgh all the possible moves
    ##simulate a move, and check if it fulfills a win condition
    ## if the win condition returns as true, return the coordinates
    ##if it didnt, try again, keep trying until nothing else,
    ## at which point, make a random move
    for coordinate in emptylist:
        x,y=coordinate
        simulatedboard=copy.deepcopy(board)
        simulatedboard[y][x]=player 

        ## checks if they return true, if so, execute
        if O_checks(simulatedboard) or X_checks(simulatedboard): 
            return coordinate 
        
    for coordinate in emptylist: 
        x,y=coordinate 
        simulatedboard=copy.deepcopy(board)
        simulatedboard[y][x]= not player 

        if O_checks(simulatedboard) or X_checks(simulatedboard):
            return coordinate 

        
    
    ##if we have no winning moves just make a random choice 

    if len(emptylist)>0:
        ai_tuple=random.choice(emptylist)
        return ai_tuple
            
    else:
        
        return False

def minimax_ai(board,player):
    best_move=None
    best_score=None

    emptylist=[]

    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                emptylist.append((column,row))


    ## iterate thru moves, calculating scores for them
    ##add it to scores array
 
    for move in emptylist:

        sim_min_max_board2=copy.deepcopy(board)

        sim_minmax_movement2=make_move(sim_min_max_board2,move,player)

        opponent_of_player_moving=not player

        score=minimax_score(sim_minmax_movement2,opponent_of_player_moving,player)

        if best_score is None or score > best_score:
            best_move = move
            best_score = score
    
    return best_move
       

def minimax_score(board, player_moving,player_to_optimize):

    if X_checks(board):
        return +10

    elif O_checks(board):
        return -10

    elif tie_checks(board):
        return 0
    

    ## get all moves that can be played
    emptylist=[]

    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                emptylist.append((column,row))


    ## iterate thru moves, calculating scores for them
    ##add it to scores array

    scores=[]
    
    for move in emptylist:

        ##make a deep copy to simulate moves on
        simulated_minmax_board=copy.deepcopy(board)

        ##simulate the opponents
        simulated_minmax_movement=make_move(simulated_minmax_board,move,player_moving)

        ##this is where we go down the rabbit hole, and exit it
        ## we create this huge spiral of this function over and over, all unique instances 
        #until we hit the bottom
        ##and return a value, then we start to unravel through it in a process
        ##which i describe below 

        opponent_of_player_moving=not player_moving

        value=minimax_score(simulated_minmax_movement,opponent_of_player_moving,player_to_optimize)
       
        scores.append(value)

    ##this goes back up to the function call attached to value in the for loop
    ##this will return the value of a complete board with a condition of victory/tie
    ##attached that we defined at the top of the loop
    ##since this will go back into the second to the last "instance" of the function call,
    ##or rather, a list of 2 elements that go into 2 possibilities
    ## it will resume at the [first,next] FIRST element that we came from
    ## and return max_score will assign the score of the outcome to element it corresponds to
    ## in this instance, FIRST will = VALUE of the LAST POSSIBLE BOARD.
    ## then, will realize where it paused is done- and it will go append that value, and 
    ## go to the NEXT element, and go down to the single element, say [G]  that corresponds
    ## with the possibility NEXT that contains a value. once it retrieves this value, it will do the   
    ##same thing
    ##this exact methodology will repeat itself all the way up the tree.
    ##it will first walk down until it hits a complete board
    ##it will then return that value up to the value it came from
    ##it will then check the next elemetn in the list if it exists.
    ##so you will have a cascading effect of
    ## [singleHERE] ------> [double1 HERE, double2] ------> [triple1HERE, tripl2, triple3]
    ## where singleHERE is the value following down the tree of the first element
    ## and single here will return a single element list of some value,
    ## double1HERE will be = the value of singleHERE, becuase its the max of its respective list
    ## double list will populate with the 2 values that were retrieved by the previously outlined   
    ## methodology
    ##between double to triple, it will take the max of double, and feed it into the tripl1HERE,
    ##aka, the value that this cascadingeffect came from.
    ##once it has returned this triple value, it will append that max value into a list of the scores,
    ##and moves onto triple2, and create a whole new tree, and follow the same process
    
    ## you cant just do max_value=0 because the first value in the scores COULD be zero.
    ##that will ruin everything and you wont get a max. you coudl get a list of all negative
    ##values. so just get the first element and compare it against everything else.
    ##works just fine 
   
   ##  if curr player is x's
    if player_moving == player_to_optimize:
        return max(scores)

    ## O's
    else:
       return min(scores)

    
   
## break all these checks into x/o
def O_checks(board):

    ## quadrant 2 diag for o
    if board[0][0]==1 and board[1][1]==1 and board[2][2]==1:
        
        return True
    
    ##quadrant 1 diag for o
    if board[0][2]==1 and board[1][1]==1 and board[2][0]==1:

       
        return True
    
    ## 1st col win condition for O
    if board[0][0]==1 and board[1][0]==1 and board[2][0]==1:
       
        return True

    ## 2nd column win for o
    if board[0][1]==1 and board[1][1]==1 and board[2][1]==1:

        
        return True
    
    # 3rd column with for x 
    if board[0][2]==1 and board[1][2]==1 and board[2][2]==1:
        
        return True
    
    ## 1st row win condition for O
    if board[0][0]==1 and board[0][1]==1 and board[0][2]==1:
        
        return True

    ## 2nd row win for o
    if board[1][0]==1 and board[1][1]==1 and board[1][2]==1:

        
        return True
    
     ## 3rd row with for x 
    if board[2][0]==1 and board[2][1]==1 and board[2][2]==1:
        
        return True
    

def X_checks(board):

    ## 1st col win for x
    if board[0][0]==0 and board[1][0]==0 and board[2][0]==0:
        return True

    ## 2nd column win for x
    if board[0][1]==0 and board[1][1]==0 and board[2][1]==0:
        
        return True

    ## 3rd column with for x 
    if board[0][2]==0 and board[1][2]==0 and board[2][2]==0:
        
        return True
    
    ##quadrant 1 diag for x
    if board[0][2]==0 and board[1][1]==0 and board[2][0]==0:
        
        return True

    ##quadrant 2 diag for x
    if board[0][0]==0 and board[1][1]==0 and board[2][2]==0:
        
        return True
    
    ## 1st row win for x
    if board[0][0]==0 and board[0][1]==0 and board[0][2]==0:
        
        return True

    ## 2nd row win for x
    if board[1][0]==0 and board[1][1]==0 and board[1][2]==0:
        
        return True

    ## 3rd row with for x 
    if board[2][0]==0 and board[2][1]==0 and board[2][2]==0:
       
        return True


def tie_checks(board):
    
    for row in board:
        for column in row:
            if column is None:
                return False
    
    else:
        
        return True
    

board=blank_board()

render(board)
print('***WELCOME TO TIC TAC TOE, X GO FIRST***')

##true is O
##false is X 

current_player=True

while True: 
    
    current_player= not current_player

    while True:
        #versus mode inputs
        if current_player==True:
            move_coord=human_player(board,current_player)
            time.sleep(1)

        if current_player==False:
            move_coord=minimax_ai(board,current_player)
            time.sleep(1)

        
        #bot inputs
        # move_coord=random_ai(board,current_player)

        # move_coord=finds_winning_moves_ai(board,current_player)

        # move_coord=finds_winning_and_losing_moves(board,current_player)
        
        if is_valid_move(board,move_coord) is True:
            break
        else: 
            print('Invalid move! (occupied cell or out of bounds) try again:')


    board=make_move(board,move_coord,current_player)

    render(board)

    winchecking1=X_checks(board)
    winchecking2=O_checks(board)
    tiechecking=tie_checks(board)

    if winchecking1 is True:
        print('X WINS')
        print('***Game Complete***')
        break
        
        
        
    if winchecking2 is True:
        print('O WINS')
        print('***Game Complete***')
        break
    
    if tiechecking is True:
        print('Tie Game')
        print('***Game Complete***')
        break
        
        
    