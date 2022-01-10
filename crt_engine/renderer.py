import pygame

class Renderer:
    def __init__(self, title: str, width: int, height: int):
        pygame.display.init()
        pygame.font.init()
        self.title = title
        self.width = width
        self.height = height
        self.main_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def clear_surface(self, surface: pygame.Surface, color) -> None:
        surface.fill(color)
        
    def update(self) -> None:
        pygame.display.flip()
        
    def create_surface(self, width: int, height: int) -> pygame.Surface:
        return pygame.Surface((width, height))
