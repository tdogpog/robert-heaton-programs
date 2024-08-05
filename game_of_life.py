import random
import time 
import os 

## game of life

## 0 or 1 live neighbors, dead
## 2 or 3 live neighbors, stay alive
## 3 or more live neighbors, die 
# if dead, exactly 3 alive neighbors, come alive  

##goals:
## build a data structuer to store the board state
##print to the terminal somehow
#calculate the next board state given intial values
#run the game forever

def dead_state(height,width):

    boardstate=[]

    for y in range(height):
        innerlist=[]
        for x in range(width):
           innerlist.append(0)
        boardstate.append(innerlist)

    ##this is what the random_state call will return, our board 
    return boardstate


        
def random_state(height,width):

    ##returns the blank board with all values zero 
    state=dead_state(height, width)

    for y in range(height):
        for x in range(width):
            state[y][x]=round(random.random())

    ##this is what the call will return 
    return state


def next_board_state(initialboard):

    ##generate a new board that we are going to write each result to
    ##this stops us from overwriting the initialboard and ruining our data
    ##so we pull initial data, read it and do calculations, and store output
    ##in this board to prevent messing with our dataset

    ##you're able to call a new blank board everytime and update it according to what is fed in
    ##because you dont need to display the history of what has occured in each step
    ##you only need to display the real time simulation of what happened between two time steps
    
    new_board=dead_state(len(initialboard),len(initialboard[0]))


    for y in range(len(initialboard)):
        
        for x in range(len(initialboard[y])):
            liveneighbors=0

            ##brilliant way to count in a circle around a given cell rather
            ##than tedious elif chains
            ##looks aroung using range -1,0,1, exlucdes 0,0
            ##because that would just return x,y of the cell itself
            ##adds the i, j to the xy we are on, and then does an if check
            ##that checks if its within the constraints of the board
            ##then, stoers that in liveneighbors for the conditions below
            ##live neighbors will reset every iteration in here

            for i in range(-1,2):
                for j in range(-1,2):
                    if i== 0 and j==0:
                        continue
                    nx=x+i
                    ny=y+j
                    if 0<= nx <len(initialboard[0]) and 0 <= ny <len(initialboard):
                        liveneighbors += initialboard[ny][nx]


            ##based off if the cell is dead or alive, what do we do with    
            ##our liveneighbor calculations
                        
            if initialboard[y][x]==1:
                if liveneighbors<2 or liveneighbors>3:
                    new_board[y][x]=0

                else: 
                    new_board[y][x]=1
            else:
                if liveneighbors==3:
                    new_board[y][x]=1

    return new_board



def render(someboard):

    ##function from os library that clears the screen every new iteration


    os.system('cls')

    print('+'+'-'*len(someboard[0])+'+')

    for x in range(len(someboard)):
        print('|',end='')
        for y in range(len(someboard[x])):
            if someboard[x][y]== 0:
                ##dead cells
                print('.',end='')
            elif someboard[x][y] == 1:
                ## live cells
                print('#',end='')
           
        print('|',end='')
        print()

    print('+'+'-'*len(someboard[0])+'+')


    return someboard


height=10   
width=30


initial_board=random_state(height,width)

render(initial_board)


while True: 
    
    ## import from the time library the adds a delay so we can see 
    ## whats on the screen
    time.sleep(0.2)

    nextboard=next_board_state(initial_board)

    render(nextboard)

    initial_board=nextboard 


