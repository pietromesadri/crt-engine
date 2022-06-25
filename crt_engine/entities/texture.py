import pygame, pathlib

class Texture:
  def __init__(self, id: int, image: pygame.Surface, width: int, height: int, x: int, y: int) -> None:
    self.id: int = id
    self.width: int = width
    self.height: int = height
    self.x: int = x
    self.y: int = y
    self.image: pygame.Surface = image

  def get_surface(self) -> pygame.Surface:
    result: pygame.Surface = pygame.Surface([self.width, self.height])
    result.set_colorkey((0,0,0))
    result.blit(self.image, (0, 0), (self.width*self.x, self.height*self.y, self.width*(self.x+1), self.height*(self.y+1)))
    result = pygame.transform.scale(self.image, (self.width, self.height))
    return result
