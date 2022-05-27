from entities.character import Character
from terrains.grass import Grass

class Loader:
  def __init__(self) -> None:
    self.terrains: list = []
    self.consumables: list = []
    self.entities: list = []

  def get_item(self, index: int, items: list) -> list:
    return list(filter(lambda x: x.id == index, items))
