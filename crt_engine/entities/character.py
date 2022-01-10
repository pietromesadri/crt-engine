from entities.entity import Entity

class Character(Entity):
  def __init__(self, id: int, width: int, height: int, x: int = 0, y: int = 0):
    self.id = id
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    Entity.__init__(self, self.id, self.width, self.height, self.x, self.y)
    