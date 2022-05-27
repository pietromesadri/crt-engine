from entities.entity import Entity

class Character(Entity):
  def __init__(self, id: int, width: int, height: int, x: int = 0, y: int = 0,
               speed: float = 0.4, max_health: int = 100, health: int = 100) -> None:
    self.id: int = id
    self.width: int = width
    self.height: int = height
    self.x: int = x
    self.y: int = y
    self.speed: float = speed
    self.max_health: int = max_health
    self.health: int = health
    Entity.__init__(self, self.id, self.width, self.height, self.x, self.y,
                    self.speed, self.max_health, self.health)
    