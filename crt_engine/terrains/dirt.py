from terrains.terrain import Terrain

class Dirt(Terrain):
  def __init__(self, x: int = 0, y: int = 0):
    self.id = 2
    self.x = x
    self.y = y
    self.width = 100
    self.height = 100
    Terrain.__init__(self, self.id, self.width, self.height, self.x, self.y)
    self.type = "dirt"