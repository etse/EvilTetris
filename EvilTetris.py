import pygame
from pygame.locals import *
from board import *
from blocks import *
import random

class Tetris:
    def __init__(self, screen_width, screen_height):
        self._screenHeight = screen_height
        self._screenWidth = screen_width
        self.clock = pygame.time.Clock()
        self.speed = 1
        self.allowedBlocks = getAllBlocks()
        pygame.init()
        
    def start(self):
        window = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        pygame.display.set_caption('Evil Tetris') 
        self.screen = pygame.display.get_surface()
        self._font = pygame.font.SysFont("Times new roman", 20)

        self._run()
        
    def _run(self):
        self.board = Board()
        self.block = None
        self.notNext = None
        self._running = True
        frameCount = 1
        downCount = 0
        self.score = 0
        
        while self._running:
            for event in pygame.event.get(): 
                self.onEvent(event)
                
            self.board.draw(self.screen, 30, 30)    
            if self.block is not None:
                self.block.draw(self.screen, 30, 30)
                self.notNext.draw(self.screen, 20, 20)
                if frameCount % int(25 / self.speed) == 0:
                    if self.block.moveDown():
                        downCount = 0
                    elif downCount < 1:
                        downCount += 1
                    else:
                        self.board.addBlock(self.block)
                        self.block = self.getNextBlock()
                        rows = self.board.removeRows()
                        if rows > 0:
                            self.addScore(rows)
            else:
                self.block = self.getNextBlock()
                
            frameCount += 1
            self.drawScore()
            pygame.display.flip()    
            self.screen.fill((0,0,0))         
            self.clock.tick(50)
                        
        self.onFinish()
        
    def onEvent(self, event):
        if event.type == QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.block.rotate()
            elif event.key == pygame.K_LEFT:
                self.block.moveLeft()
            elif event.key == pygame.K_RIGHT:
                self.block.moveRight()
            elif event.key == pygame.K_DOWN:
                self.block.moveDown()
            elif event.key == pygame.K_SPACE:
                self.block.moveToBottom()
                self.board.addBlock(self.block)
                self.block = self.getNextBlock()
                rows = self.board.removeRows()
                if rows > 0:
                    self.addScore(rows)
        
    def onFinish(self):
        pygame.display.quit()
        pygame.quit()
        
    def addScore(self, rows):
        self.score += (rows ** 2) + self.speed
        self.speed = 1 + int(self.score / 15)
        
    def getNextBlock(self):
        blockNum = random.randrange(0, len(self.allowedBlocks)-2)       
        self.allowedBlocks = sorted(self.allowedBlocks, key=lambda x: x(self.board).getFitness())
        self.notNext = self.allowedBlocks[-1](self.board)
        self.notNext._y = 5
        self.notNext._x = 17
        return self.allowedBlocks[blockNum](self.board)
        
    def drawScore(self):
        text = ("Score: %d" % self.score)
        label = self._font.render(text, 0, (255,255,255))
        self.screen.blit(label, (self._screenWidth - 120, self._screenHeight - 200))
        
        
if __name__ == '__main__':
    game = Tetris(450, 20*30)
    game.start()
    
    
