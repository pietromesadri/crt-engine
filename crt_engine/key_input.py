import pygame

class KeyInput:
  def __init__(self) -> None:
    self.keys_pressed: list = []

  def event_handler(self) -> int:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        self.keys_pressed.append(event.key)
      if event.type == pygame.KEYUP:
        if event.key in self.keys_pressed: self.keys_pressed.remove(event.key)
      if event.type == pygame.QUIT:
        return 0
    return 1

  def get_mouse_pos(self) -> tuple[int, int]:
    return pygame.mouse.get_pos()
    
