import pygame

class Board:
    def __init__(self):
        self._board = [[None for x in xrange(22)] for y in xrange(10)]
    
    def getBrick(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(self._board) or y >= len(self._board[0]):
            return False
        return self._board[int(x)][int(y)]
        
    def addBlock(self, block):
        posx = int(block._x)
        posy = int(block._y+0.5)
        
        for x in xrange(len(block.layout)):
            for y in xrange(len(block.layout[0])):
                if block.layout[x][y] > 0:
                    self._board[posx+x][posy+y] = block.color
                    
    def draw(self, screen, width, height):
        rect = pygame.Rect(0, 0, width, height)
        for x in xrange(len(self._board)):
            for y in xrange(2, len(self._board[0])):
                rect.topleft = (x*width, (y-2)*height)
                if self._board[x][y] is not None:
                    screen.fill(self._board[x][y], rect)
                else:
                    screen.fill((50, 50, 50), rect)
