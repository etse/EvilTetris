
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
    pass
    
    
