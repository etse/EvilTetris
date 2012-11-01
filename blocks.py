
class Block:
  def __init__(self, board):
    self._layout = [[0 for x in xrange(3)] for y in xrange(3)]
    self._x = 5
    self._y = 0
    self._board = board
    
  def __str__(self):
    return "A blank block"
    
  def __repr__(self):
    return self.__str__()
    
  def moveLeft(self):
    pass
    
  def moveRight(self):
    pass
    
  def moveDown(self, step=0.1):
   pass
    
  def rotate(self):
    self._layout = zip(*self._layout[::-1])
    
  def getFitness(self):
    pass
    
  def printLayout(self):
    for row in self._layout:
      print row


class IBlock(Block):
  def __init__(self, board):
    Block.__init__(self, board)
    self._layout = [[0 for x in xrange(4)] for y in xrange(4)]
    self._layout[0][2] = 1
    self._layout[1][2] = 1
    self._layout[2][2] = 1
    self._layout[3][2] = 1
    
class SquereBlock(Block):
  def __init__(self, board):
    Block.__init__(self, board)
    self._layout = [[1 for x in xrange(2)] for y in xrange(2)]
    
class ZBlock(Block):
  def __init__(self, board):
    Block.__init__(self, board)
    self._layout[0][0] = 1
    self._layout[0][1] = 1
    self._layout[1][1] = 1
    self._layout[1][2] = 1
    
  def rotate(self):
    Block.rotate(self)
    if not 1 in self._layout[0]:
      self._layout = self._layout[1:3] + [[0 for x in xrange(3)]]
      
class ZInverseBlock(Block):
  def __init__(self, board):
    Block.__init__(self, board)
    self._layout[1][0] = 1
    self._layout[1][1] = 1
    self._layout[0][1] = 1
    self._layout[0][2] = 1
    
  def rotate(self):
    Block.rotate(self)
    if not 1 in self._layout[0]:
      self._layout = self._layout[1:3] + [[0 for x in xrange(3)]]

class TBlock(Block):
  def __init__(self, board):
    Block.__init__(self, board)
    self._layout[1][0] = 1
    self._layout[0][1] = 1
    self._layout[1][1] = 1
    self._layout[2][1] = 1

class LBlock(Block):
  def __init__(self, board):
    Block.__init__(self, board)
    self._layout[1][0] = 1
    self._layout[1][1] = 1
    self._layout[1][2] = 1
    self._layout[2][2] = 1
    
class LInverseBlock(LBlock):
  def __init__(self, board):
    LBlock.__init__(self, board)
    self._layout[2][2] = 0
    self._layout[2][0] = 1

if __name__ == '__main__':
  block1 = ZInverseBlock(None)
  for x in xrange(4):
    block1.printLayout()
    block1.rotate()
    print "Rotating"

