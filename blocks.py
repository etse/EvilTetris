
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
    
    def moveDown(self, step=0.1):
        if self._testPossible(self.layout, self._x, self._y+step):
            self._y += step
    
    def rotate(self):
        newlayout = zip(*self.layout[::-1])
        if self._testPossible(newlayout, int(self._x), int(self._y)):
            self.layout = newlayout
            
    def _testPossible(self, layout, posx, posy):
        for x in xrange(len(self.layout)):
            for y in xrange(len(self.layout[0])):
                brick = self._board.getBrick(posx+x, posy+y)
                if brick is False:
                    return False
                    
                if brick > 0 and self.layout[x][y] > 0:
                    return False
        return True
    
    def getFitness(self):
        pass
    
    def printLayout(self):
        for row in self.layout:
            print row


class IBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self._y -= -4
        self.layout = [[0 for x in xrange(4)] for y in xrange(4)]
        self.layout[0][2] = 1
        self.layout[1][2] = 1
        self.layout[2][2] = 1
        self.layout[3][2] = 1
        
    def __str__(self):
        return "An I block"
    
class SquereBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout = [[1 for x in xrange(2)] for y in xrange(2)]
        
    def __str__(self):
        return "A squere block"
    
class ZBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[0][0] = 1
        self.layout[0][1] = 1
        self.layout[1][1] = 1
        self.layout[1][2] = 1
        
    def __str__(self):
        return "A Z block"
      
class ZInverseBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[1][0] = 1
        self.layout[1][1] = 1
        self.layout[0][1] = 1
        self.layout[0][2] = 1
        
    def __str__(self):
        return "An inversed Z block"

class TBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[1][0] = 1
        self.layout[0][1] = 1
        self.layout[1][1] = 1
        self.layout[2][1] = 1
        
    def __str__(self):
        return "A T block"

class LBlock(Block):
    def __init__(self, board):
        Block.__init__(self, board)
        self.layout[1][0] = 1
        self.layout[1][1] = 1
        self.layout[1][2] = 1
        self.layout[2][2] = 1
        
    def __str__(self):
        return "A L block"
    
class LInverseBlock(LBlock):
    def __init__(self, board):
        LBlock.__init__(self, board)
        self.layout[2][2] = 0
        self.layout[2][0] = 1
        
    def __str__(self):
        return "An inversed L block"

if __name__ == '__main__':
    from board import *
    block1 = ZInverseBlock(Board())
    for x in xrange(40):
        #block1.printLayout()
        #block1.rotate()
        block1.moveRight()
        print "Now at", block1._x
        print "Rotating."

