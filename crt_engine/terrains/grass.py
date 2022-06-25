from terrains.terrain import Terrain
import pygame, pathlib

class Grass(Terrain):
  def __init__(self, x: int = 0, y: int = 0) -> None:
    self.id: int = 1
    self.x: int = x
    self.y: int = y
    self.width: int = 50
    self.height: int = 50
    Terrain.__init__(self, self.id, self.width, self.height, self.x, self.y)
    self.type: str = "GRASS"
    self.image = pygame.image.load(f"{pathlib.Path(__file__).parent.parent.resolve()}/assets/grass.png").convert()