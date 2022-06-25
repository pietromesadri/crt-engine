from entities.entity import Entity
from entities.texture import Texture
import pygame

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
    self.head: Texture = None
    self.body: Texture = None
    self.state: str = "STOPPED"
    self.frame_update: float = pygame.time.get_ticks()
    Entity.__init__(self, self.id, self.width, self.height, self.x, self.y,
          self.speed, self.max_health, self.health)

  def create_image(self) -> None:
    self.image: pygame.Surface = pygame.Surface([self.width, self.height])
    self.image.set_colorkey((0,0,0))
    self.image.blit(self.head, (0, 0))
    self.image.blit(self.body, (0, self.height/2))
    self.rect = self.image.get_rect()

  def update(self, input_keys, frame_time: int) -> None:
    self.moving = []
    self.frame_update = pygame.time.get_ticks()
    if pygame.K_w in input_keys:
      self.moving.append(1)
      self.y -= self.speed * frame_time
    if pygame.K_s in input_keys:
      self.moving.append(2)
      self.y += self.speed * frame_time
    if pygame.K_d in input_keys:
      self.moving.append(3)
      self.x += self.speed * frame_time
    if pygame.K_a in input_keys:
      self.moving.append(4)
      self.x -= self.speed * frame_time
    self.rect.update(self.x, self.y, self.width, self.height)
