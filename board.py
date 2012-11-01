import pygame
from copy import deepcopy

class Board:
    def __init__(self):
        self._board = [[None for x in xrange(10)] for y in xrange(22)]
    
    def getBrick(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(self._board[0]) or y >= len(self._board):
            return False
        return self._board[int(y)][int(x)]
        
    def addBlock(self, block):
        posx = int(block._x)
        posy = int(block._y+0.5)
        
        for x in xrange(len(block.layout)):
            for y in xrange(len(block.layout[0])):
                if block.layout[x][y] > 0:
                    self._board[posy+y][posx+x] = block.color
                                        
    def draw(self, screen, width, height):
        rect = pygame.Rect(0, 0, width, height)
        for x in xrange(len(self._board[0])):
            for y in xrange(2, len(self._board)):
                rect.topleft = (x*width, (y-2)*height)
                if self._board[y][x] is not None:
                    screen.fill(self._board[y][x], rect)
                else:
                    screen.fill((60, 60, 60), rect)
                    
    def removeRows(self):
        num = 0
        for row in list(self._board):
            if None not in row:
                num += 1
                self._board.remove(row)
                self._board = [[None for x in range(10)]] + self._board
        return num
        
    def getNumRemoves(self):
        num = 0
        for row in list(self._board):
            if None not in row:
                num += 1
        return num
        
    def getBadness(self, block):
        backup = deepcopy(self._board)
        self.addBlock(block)
        count = 0
        
        for y in xrange(len(self._board)-1):
            for x in xrange(len(self._board[0])):
                if self.getBrick(x, y) is not None:
                    if self.getBrick(x, y+1) is None:
                        count -= 1
                        
        count += 5 * self.getNumRemoves()                
        self._board = backup                
        return count
        
            
