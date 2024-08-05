
from settings import *



class Player(pygame.sprite.Sprite):
    
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        