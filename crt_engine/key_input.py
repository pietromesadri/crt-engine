import pygame

class KeyInput:
    def __init__(self) -> None:
        self.keys_pressed = []

    def event_handler(self) -> int:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keys_pressed.append(event.key)
            if event.type == pygame.KEYUP:
                self.keys_pressed.remove(event.key)
            if event.type == pygame.QUIT:
                return 0

        return 1
