import pygame

class Renderer:
    def __init__(self, title: str, width: int, height: int) -> None:
        pygame.display.init()
        pygame.font.init()
        self.title: str = title
        self.width: int = width
        self.height: int = height
        self.world_coord: list = [0, 0]
        self.camera: list = [0, 0]
        self.main_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def clear_surface(self, surface: pygame.Surface, color) -> None:
        surface.fill(color)
        
    def update(self) -> None:
        pygame.display.flip()

    def render(self, object: pygame.Surface, xcoord: int, ycoord: int) -> None:
        self.main_display.blit(object, (xcoord - self.camera[0], ycoord - self.camera[1]))
        
    def create_surface(self, width: int, height: int) -> pygame.Surface:
        return pygame.Surface((width, height))

    def get_map_index(self, tile_size: int) -> list:
        self.camera = [self.world_coord[0] % tile_size, self.word_coord[1] % tile_size]
        return [self.world_coord[0] / tile_size, self.world_coord[1] / tile_size]
