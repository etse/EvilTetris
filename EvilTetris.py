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
        self.speed = 5
        self.allowedBlocks = getAllBlocks()
        pygame.init()
        
    def start(self):
        window = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        pygame.display.set_caption('Evil Tetris') 
        self.screen = pygame.display.get_surface()
        self.board = Board()
        self.block = None
        self._run()
        
    def _run(self):
        self._running = True
        frameCount = 0
        downCount = 0
        
        while self._running:
            for event in pygame.event.get(): 
                self.onEvent(event)
                
            self.board.draw(self.screen, 30, 30)    
            if self.block is not None:
                self.block.draw(self.screen, 30, 30)
                if frameCount % int(10 / self.speed) == 0:
                    if self.block.moveDown():
                        downCount = 0
                    elif downCount < 4:
                        downCount += 1
                    else:
                        self.board.addBlock(self.block)
                        self.block = self.getNextBlock()
            else:
                self.block = self.getNextBlock()
                
            frameCount += 1
            pygame.display.flip()             
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
        
    def onFinish(self):
        pygame.display.quit()
        pygame.quit()
        
    def getNextBlock(self):
        blockNum = random.randrange(0, len(self.allowedBlocks))
        return self.allowedBlocks[blockNum](self.board)
        
if __name__ == '__main__':
    game = Tetris(450, 20*30)
    game.start()
    
