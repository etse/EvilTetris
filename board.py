
class Board:
    def __init__(self):
        self._board = [[0 for x in xrange(30)] for y in xrange(10)]
    
    def getBrick(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(self._board) or y >= len(self._board[0]):
            return False
        return self._board[int(x)][int(y)]
        
    def addBlock(self, block, posx, posy):
        for x in xrange(len(block.layout)):
            for y in xrange(len(block.layout[0])):
                if block.layout[x][y] > 0:
                    self._board[posx+x][posy+y] = block.color
