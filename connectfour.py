# Connect Four
### To play ###
# define board size. b = Board(6,7)
# define computer player:
# po = ('O', tiebreakmethod 'RIGHT' or 'LEFT' or 'RANDOM', # of ply)
# b.playGame('human', po)


import random

class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """returns opposite player's playing piece"""
        if self.ox == "O":
            return "X"
        elif self.ox == "X":
            return "O"
        else:
            return "Error."
        
    def scoreBoard(self,b):
        """returns float of score of input b(Board); 100.0 if win for self,
        0.0 if loss for self, 50.0 otherwise"""
        opp = self.oppCh()
        if b.winsFor(self.ox) == True:
            return 100.0
        elif b.winsFor(opp) == True:
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self,scores):
        """input scores: nonempty list of floats(List)
        returns column number of highest score; if tie:
        returns column number of best score using tbt method"""

        maxIndices = []
        mx = max(scores)
        for x in range(len(scores)):
            if mx == scores[x]:
                maxIndices += [x]
        #return maxIndices
        if len(maxIndices) == 1:
            return maxIndices[0]
        else:
            if self.tbt == "RIGHT":
                return maxIndices[len(maxIndices)-1]
            elif self.tbt == "LEFT":
                return maxIndices[0]
            elif self.tbt == "RANDOM":
                c = random.choice(range(len(maxIndices)))
                return maxIndices[c]

    def scoresFor(self,b):
        """returns list of scores for moving into each possible column"""

        opp = self.oppCh()
        scores = [50]*b.width
        for col in range(b.width):
            if b.winsFor(self.ox) == True:
                scores[col] = 100.0
            elif b.winsFor(self.oppCh()) == True:
                scores[col] = 0.0
            elif b.allowsMove(col) == False:
                scores[col] = -1.0
            elif self.ply == 0:
                scores[col] = self.scoreBoard(b)
            else:
                b.addMove(col,self.ox)
                opp = Player(self.oppCh(),self.tbt,self.ply-1)
                s = opp.scoresFor(b)
                scores[col] = (100 - max(s))
                b.delMove(col)
        return scores


    def nextMove(self,b):
        """returns column number (int) that Player chooses to move to; input b: object of type Board"""
        return self.tiebreakMove(self.scoresFor(b))
     
class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range( H ):
            s += '|'   # add the spacer character
            for col in range( W ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*(W+1)+ '\n' + ' '
        for x in range(W):
            s += str(x%10) + ' '

        # add the bottom of the board
        # and the numbers underneath here
        
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ """
        H = self.height
        for row in range(H-1,-1,-1):
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                break

    def clear(self): 
        """ clears board"""
        H = self.height
        W = self.width
        for row in range(H):
            for col in range(W):
                self.delMove(col)


    def allowsMove( self, col ):
        """ returns True if a move to col is allowed
            in the board represented by self
            returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '
    

    def isFull( self ):
        """ returns True if the board is full """
        for col in range( self.width ):
            if self.allowsMove( col ):
                return False
        return True


    def delMove(self,c):
        """deletes top checker from column c"""
        H = self.height
        for row in range(H):
            #print row
            #print c
            #print self.data[row][c]
            if self.data[row][c] != ' ':
             #   print 'if'
                self.data[row][c] = ' '
                break
                

    def winsFor(self,ox):
        """checks if ox has won 4 in a row/col/diagonal"""
        # check for horizontal wins
        H = self.height
        W = self.width
        for row in range(0,H):
            for col in range(0,W-3):
                if self.data[row][col] == ox and \
                   self.data[row][col+1] == ox and \
                   self.data[row][col+2] == ox and \
                   self.data[row][col+3] == ox:
                    return True
        # check vertical
        for row in range(0,H-3):
            for col in range(0,W):
                if self.data[row][col] == ox and \
                   self.data[row+1][col] == ox and \
                   self.data[row+2][col] == ox and \
                   self.data[row+3][col] == ox:
                    return True
        #check southeast
        for row in range(0,H-3):
            for col in range(0,W-3):
                if self.data[row][col] == ox and \
                   self.data[row+1][col+1] == ox and \
                   self.data[row+2][col+2] == ox and \
                   self.data[row+3][col+3] == ox:
                    return True
        #check southwest
        for row in range(0,H-3):
            for col in range(W-4,W):
                if self.data[row][col] == ox and \
                   self.data[row+1][col-1] == ox and \
                   self.data[row+2][col-2] == ox and \
                   self.data[row+3][col-3] == ox:
                    return True
        return False

                    

    def hostGame(self):
        """hosts a full game of Connect Four"""
        print 'Welcome to Connect Four!' + '\n'
        print self
        while self.winsFor('O') == False and self.winsFor('X')== False and \
              self.isFull()==False:
            X = input("X's choice:")
            while self.allowsMove(X) == False:
                print 'Try again!'
                X = input("X's choice:")
            if self.allowsMove(X) == True and self.isFull() == False:
                self.addMove(X,'X')
                print b
            if self.winsFor('X') == True:
                print b
                print "X wins -- Congratulations!"
                break
            if self.isFull() == True:
                print b
                print "Game over! Tie!"
                break
            O = input("O's choice:")
            while self.allowsMove(O) == False:
                print 'Try again!'
                O = input("O's choice:")
            if self.allowsMove(O) and self.isFull() == False:
                self.addMove(O,'O')
                print b
            if self.winsFor('O') == True:
                print b
                print "O wins -- Congratulations!"
                break
            if self.isFull() == True:
                print b
                print "Game over! Tie!"
                break
        return


                

 
    
    def playGame(self,px,po):
        """hosts a game with players px and po. If either is human, asks for inputs"""

        nextCheckerToMove = 'X'

        while True:
            if nextCheckerToMove == 'X':
                plr = px
            else:
                plr = po
        
            # print the board
            print self
            if plr != 'human':
            # get the next move from the computer
                col = -1
                while not self.allowsMove( col ):
                    col = plr.nextMove(self)
                self.addMove( col, nextCheckerToMove )
            else:
                col = -1
                while not self.allowsMove( col ):
                    col = input('Next col for ' + nextCheckerToMove + ': ')
                self.addMove( col, nextCheckerToMove )
         

            # check if the game is over
            if self.winsFor( nextCheckerToMove ):
                print self
                print '\n' + nextCheckerToMove + ' wins! Congratulations!\n\n'
                break
            if self.isFull():
                print self
                print '\nThe game is a tie.\n\n'
                break

            # switch players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
            else:
                nextCheckerToMove = 'X'
            
                
        print 'See ya later!'
