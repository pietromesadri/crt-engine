import pygame

class Terrain(pygame.sprite.Sprite):

    # initial parameters
    def __init__(self, id: int, width: int = 10, height: int = 10, x: int = 0, y: int = 0) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.type = ""
        self.image = pygame.Surface([self.width, self.height])
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)