from terrains.terrain import Terrain

class Metal(Terrain):
  def __init__(self, x: int = 0, y: int = 0) -> None:
    self.id: int = 3
    self.x: int = x
    self.y: int = y
    self.width: int = 100
    self.height: int = 100
    Terrain.__init__(self, self.id, self.width, self.height, self.x, self.y)
    self.type: str = "metal"