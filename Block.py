import pygame
import os
from enum import Enum

########NOTE:
########    Blocks are the 1x1 blocks, the one that makes up the grid
########    Tetras are the ones made up by 4 blocks making weird shapes

class Block(pygame.sprite.Sprite):
    def __init__ (self,block_type, xy):
        # just the basic building block of tetras, makes up the grid
        pygame.sprite.Sprite.__init__(self)
        self.block_type=block_type
        if block_type==1:
            self.image =pygame.image.load( os.path.join( 'basic_block1.bmp' ))
        elif block_type==2:
            self.image =pygame.image.load( os.path.join( 'basic_block2.bmp' ))
        elif block_type==3:
            self.image =pygame.image.load( os.path.join( 'basic_block3.bmp' ))
        elif block_type==4:
            self.image =pygame.image.load( os.path.join( 'basic_block4.bmp' ))
        elif block_type==5:
            self.image =pygame.image.load( os.path.join( 'basic_block5.bmp' ))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = xy

    def transform(self,block_type):
        self.block_type=block_type
        if block_type==1:
            self.image =pygame.image.load( os.path.join( 'basic_block1.bmp' ))
        elif block_type==2:
            self.image =pygame.image.load( os.path.join( 'basic_block2.bmp' ))
        elif block_type==3:
            self.image =pygame.image.load( os.path.join( 'basic_block3.bmp' ))
        elif block_type==4:
            self.image =pygame.image.load( os.path.join( 'basic_block4.bmp' ))
        elif block_type==5:
            self.image =pygame.image.load( os.path.join( 'basic_block5.bmp' ))
        self.image.convert()
