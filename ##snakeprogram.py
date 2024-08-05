##programs for advanced beginners

import os

import random

class AppleClass: 
    def __init__(self,height, width):
        self.height=height
        self.width=width
        self.apple_coord=(None,None)
        self.score=0
                 

    def generate_apple(self): 
    
        random_y=random.randint(0,self.height-1)
        random_x=random.randint(0,self.width-1)

        self.apple_coord=(random_y,random_x)


    def remove_apple(self):
        ##syntax to access another method within the same class
        self.generate_apple()
        self.score+=1
        print('Score:',self.score)
        
   

    

class SnakeClass:

    #takes in (body, dir) from Gameclass constructor initializing
    def __init__(self, body, direction):
        self.body= body
        self.direction= direction
         
    def take_step(self, position,apple_coord) :

        #YOU CANT DO THIS. THIS CONCATENATES THE TUPLES INTO (3,0,1,0)
        ## DONT DO THIS 
        # new_element= self.body[-1]+position

        new_element=(self.body[-1][0]+position[0],self.body[-1][1]+position[1])

        ##checks if you went into body and fixes the last element
        ##accepting negative values on the board and teleporting
        ##the rest of the body 

        loseconditions=self.body[:-1]
     
        if new_element == self.body[-2]:
            return
        
        for tuple in loseconditions:
            if new_element == tuple:
                print('Game Over: Collided with Body!!')
                exit() 
            if new_element[0] < 0 or new_element[1] < 0:
                print('Game Over: Collided with Wall!!')
                exit()

        if new_element == self.body[-1]:
            return
                

        self.body.append(new_element)

        if self.head() != apple_coord:
            self.body=self.body[1:]
            return False
        else:
            self.body=self.body[:]
            return True
            

        
        
    def set_direction(self, direction): 
        self.direction=direction

        return self.direction

    def head(self):

        return self.body[-1]
    
    #provides a way to access the body 
    def bodymeth(self):

        return self.body[:]


# UP=(0,1)
# DOWN=(0,-1)
# LEFT=(0,-1)
# RIGHT=(0,1)

class GameClass :

    ## constructor takes (self, arg1, arg2) 

    def __init__(self,height,width) :
        self.height=height
        self.width=width
        #args (body, direction)
        self.snake=SnakeClass([(0,0),(1,0),(2,0),(3,0)],UP)
        self.apple=AppleClass(height,width)


    ## making a 2d matrix
    def board_matrix(self):

    
        outerlist=[]
        

        ##populate a 2x2 matrix with None
        for y in range(self.height):
        
            innerlist=[]
            for x in range(self.width):
                innerlist.append(None)

            outerlist.append(innerlist)

        
        
        ##you must explicity return the outerlist or else python just wont do it
        ## when you try to render with this matrix we constructed in def render(self)
        ##you get a Nonetype object error if you dont add this
        return outerlist 
    
    def inputstream(self):


        ##take an input from the user and .upper to convert every input to upper case
        ##because our logic runs off uppercase comparisons

        self.apple.generate_apple()
        score=0

        while True:

            dirinput=input('WASD to move the snake:', ).upper()

            if dirinput== 'W':
                ##feed in our take_step method from the snake class
                ##that takes a positional input and returns an updated body
                inputmovement=UP

            elif dirinput== 'A':
                inputmovement=LEFT

            elif dirinput== 'S':
                inputmovement=DOWN

            elif dirinput== 'D':
                inputmovement=RIGHT

            elif dirinput=='':
                try:
                    inputmovement=direction
                except: 
                    continue

            else: 
                print('WASD only')
                continue 
            
            ##put these results into take_step method to calculate motion

           
            direction=self.snake.set_direction(inputmovement)
            
            ##go into function that calculates new body
            ##check for loss conditions, etc

            applecoord=self.apple.apple_coord

            if self.snake.take_step(inputmovement,applecoord) is True:
                self.apple.remove_apple()



            ##check if the head is on the apple, 
            ##if it did, generate a new apple and extend the body
            # if self.snake.head() == self.apple.apple_coord:
            #     self.apple.remove_apple()
            #     score+=1
            #     

            ## update the render with new snake values 
            self.render()
            
        

    def render(self):

        #calls an empty 2x2 matrix with None occupying all spaces from board_matrix

        board=self.board_matrix()
        
        ## you cant do this because python thinks this is a method inside of GameClass
        #snakesbody=self.bodymeth()
        snakesbody=self.snake.bodymeth()
        lensnake=len(snakesbody)

        ##make the terminal appearance clearer
        os.system('cls' if os.name == 'nt' else 'clear')

        ##prints a top border +--+ based off the width fed into the object argument
        top_bottom_border='+' + '-'*self.width*2 + '+'

       ##store the apples coords
        y,x=self.apple.apple_coord
        

        ##skips the first render, only prints when the game starts
        if y !=None or x != None:
            board[y][x]='*'

        for tupval in snakesbody: 

            #returns a pair of tuples
            y,x= tupval
            ## board[x (what list)][y what column]
            ## set it = to whatever you want to replace it with 
            ## x, y is pointing towards what exactly we want to replace in our board
            try:
                board[y][x]='O'
            
            ##lose condition for collision with wall for 
            ##body, head bug fixed in the take_step method 
            except: 
                
                if IndexError:
                    print('YOU LOSE')
                    exit()
            
            if tupval == snakesbody[-1]:
                board[y][x]='X'


        print(top_bottom_border)
        
        #each row, print a |, add spaces based off width, and add a | to close
        for row in board :
            print('|',end='')
            for column in row :
                if column == None:
                    print('  ',end='')
                elif column=='O':
                    print('O ', end='')
                elif column== 'X' : 
                    print('X ', end='')
                elif column =='*':
                    print('* ',end='')
            
            print('|')
 
        print(top_bottom_border)
        
        
#(y,x)
UP=(-1,0)
DOWN=(1,0)
LEFT=(0,-1)
RIGHT=(0,1)
    
            

##game becomes an object of the GameClass, feed it height, width
game=GameClass(8,20)

game.render()
print('Once you have inputted a move, you can keep hitting enter\n to move in the same direction you last moved in!')

game.inputstream()





