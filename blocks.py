import pygame

class Block:
    def __init__(self, board):
        self.layout = [[0 for x in xrange(3)] for y in xrange(3)]
        self._x = 4
        self._y = 0
        self._board = board
        self.color = (255, 0, 255)
    
    def __str__(self):
        return "A blank block"
    
    def __repr__(self):
        return self.__str__()
    
    def moveLeft(self):
        if self._testPossible(self.layout, self._x-1, self._y):
            self._x -= 1
    
    def moveRight(self):
        if self._testPossible(self.layout, self._x+1, self._y):
            self._x += 1
    
    def moveDown(self, step=1):
        if self._testPossible(self.layout, self._x, self._y+step):
            self._y += step
            return True
        return False
        
    def moveToBottom(self):
        while self.moveDown():
            continue
    
    def rotate(self):
        newlayout = zip(*self.layout[::-1])
        if self._testPossible(newlayout, int(self._x), int(self._y)) == True:
            self.layout = newlayout
            
    def _testPossible(self, layout, posx, posy):
        for x in xrange(len(layout)):
            for y in xrange(len(self.layout[0])):
                if layout[x][y] == 0 or posy+y <= 0:
                    continue
                brick = self._board.getBrick(posx+x, posy+y)
                
                if brick == False:
                    return False     
                if brick > 0 and layout[x][y] is not None:
                    return False
                    
        return True
    
    def getFitness(self):
        bestCost = -1000
        for r in xrange(4):
            self._x = 0
            for x in xrange(10):
                self.moveRight()
                self.moveToBottom()
                cost = self._board.getBadness(self)
                
                if cost > bestCost:
                    bestCost = cost
                                        
            self._y = 1
            self.rotate()
        return bestCost
    
    def printLayout(self):
        for row in self.layout:
            print row
            
    def draw(self, screen, width, height):
        rect = pygame.Rect(0, 0, width, height+1)
        for x in xrange(len(self.layout)):
            for y in xrange(len(self.layout[0])):
                if self.layout[x][y] > 0:
                    rect.topleft = (int((self._x+x)*width), int((self._y+y-2)*height))
                    screen.fill(self.color, rect)

class IBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self._y = -2
        self.layout = [[0 for x in xrange(4)] for y in xrange(4)]
        self.layout[1][0] = 1
        self.layout[1][1] = 1
        self.layout[1][2] = 1
        self.layout[1][3] = 1
        self.color = (0, 255, 255)
        
    def __str__(self):
        return "An I block"
        
    def rotate(self):
        newlayout = zip(*self.layout[::1])
        if self._testPossible(newlayout, int(self._x), int(self._y)) == True:
            self.layout = newlayout
    
class SquereBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout = [[1 for x in xrange(2)] for y in xrange(2)]
        self.color = (90, 90, 230)
        
    def __str__(self):
        return "A squere block"
    
class ZBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[0][0] = 1
        self.layout[0][1] = 1
        self.layout[1][1] = 1
        self.layout[1][2] = 1
        self.color = (0, 255, 0)
        
    def __str__(self):
        return "A Z block"
      
class ZInverseBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[1][0] = 1
        self.layout[1][1] = 1
        self.layout[0][1] = 1
        self.layout[0][2] = 1
        self.color = (100, 150, 255)
        
    def __str__(self):
        return "An inversed Z block"

class TBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[1][0] = 1
        self.layout[0][1] = 1
        self.layout[1][1] = 1
        self.layout[2][1] = 1
        self.color = (255, 255, 255)
        
    def __str__(self):
        return "A T block"

class LBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[1][0] = 1
        self.layout[1][1] = 1
        self.layout[1][2] = 1
        self.layout[2][2] = 1
        self.color = (120, 170, 150)
        
    def __str__(self):
        return "A L block"
    
class LInverseBlock(LBlock):
    def __init__(self, board):
        LBlock.__init__(self, board)
        self.layout[2][2] = 0
        self.layout[2][0] = 1
        self.color = (50, 170, 255)
        
    def __str__(self):
        return "An inversed L block"

def getAllBlocks():
    return [IBlock, SquereBlock, ZBlock, ZInverseBlock, TBlock, LBlock, LInverseBlock]

if __name__ == '__main__':
    from board import *
    block1 = ZInverseBlock(Board())
    for x in xrange(40):
        #block1.printLayout()
        #block1.rotate()
        block1.moveRight()
        print "Now at", block1._x
        print "Rotating."
