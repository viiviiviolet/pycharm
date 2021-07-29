import pygame

#initializing variables
turn = 'X'
winner = None
draw = None
width = 400
height = 400
background = (255, 255, 255)
line_color = (0, 0, 0)
start = False
fps = 30

# an object for a square of a 3x3 grid
class Space:
    #dictionary for converting integer states to the appropriate letters
    states = {
        0: 'X',
        1: 'O'
    }
    def __init__(self):
        self.spaceid = None
#for changing the state of a space
    def changestate(self, newstate):
        self.spaceid = newstate

#class for the entire game board
class Board:
    #2d matrix of spaces
    def __init__(self):
        self.boardarray = []
        self.row = []
        for i in range(3):
            self.row.append(Space)
        for i in range(3):
            self.boardarray.append(self.row)
    #check if a player has won
    def checkwin(self):
        for i in range(2):
            for x in self.boardarray:
                if self.boardarray[x][0] == self.boardarray[x][1] == self.boardarray[x][2] == i:
                    winner = i
                else:
                    winner = None
            for y in range(3):
                if self.boardarray[0][y] == self.boardarray[1][y] == self.boardarray[2][y] == i:
                    winner = i
                else:
                    winner = None
            if self.boardarray[0][0] == self.boardarray[1][1] == self.boardarray[2][2] == i:
                winner = i
            elif self.boardarray[2][0] == self.boardarray[1][1] == self.boardarray[0][2] == i:
                winner = i
            else:
                winner = None
    #check if there are no empty spaces
    def checkfull(self):
        for i in range(3):
            for x in range(3):
                if self.boardarray[i][x] == None:
                    full = False
                    break
                else:
                    full == True
            if full == False:
                break
        return full
    #check if it is a tie game
    def checktie(self):
        full = self.checkfull()
        win = self.checkwin()
        if full and not win:
            return True
        else:
            return False

#class for each player
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.score = 0
        self.name = ''
    def scorepoint(self):
        self.score += 1
    def changename(self, newname):
        self.name = newname

pygame.init()
screen = pygame.display.set_mode((width, height), 0, fps)
pygame.display.set_caption("Tic-Tac-Toe")
p1 = Player('X')
p2 = Player('O')
while start:

