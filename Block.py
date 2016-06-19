import pygame
import os
from enum import Enum

########NOTE:
########    Blocks are the 1x1 blocks, the one that makes up the grid
########    Tetras are the ones made up by 4 blocks making weird shapes

class BlockColor(Enum):
    Red = 1
    Yellow = 2
    Blue = 3
    Green = 4
    Transparent = 5

class Block(pygame.sprite.Sprite):
    def __init__ (self,block_type, xy):
        # just the basic building block of tetras, makes up the grid
        pygame.sprite.Sprite.__init__(self)
        self.block_type=block_type
        if block_type==BlockColor.Red:
            self.image =pygame.image.load( os.path.join( 'basic_block1.bmp' ))
        elif block_type==BlockColor.Yellow:
            self.image =pygame.image.load( os.path.join( 'basic_block2.bmp' ))
        elif block_type==BlockColor.Blue:
            self.image =pygame.image.load( os.path.join( 'basic_block3.bmp' ))
        elif block_type==BlockColor.Green:
            self.image =pygame.image.load( os.path.join( 'basic_block4.bmp' ))
        elif block_type==BlockColor.Transparent:
            self.image =pygame.image.load( os.path.join( 'basic_block5.bmp' ))
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = xy

    def transform(self,block_type):
        self.block_type=block_type
        if block_type==BlockColor.Red:
            self.image =pygame.image.load( os.path.join( 'basic_block1.bmp' ))
        elif block_type==BlockColor.Yellow:
            self.image =pygame.image.load( os.path.join( 'basic_block2.bmp' ))
        elif block_type==BlockColor.Blue:
            self.image =pygame.image.load( os.path.join( 'basic_block3.bmp' ))
        elif block_type==BlockColor.Green:
            self.image =pygame.image.load( os.path.join( 'basic_block4.bmp' ))
        elif block_type==BlockColor.Transparent:
            self.image =pygame.image.load( os.path.join( 'basic_block5.bmp' ))
        self.image.convert()
