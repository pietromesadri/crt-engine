import pygame
import pathlib
from terrains.metal import Metal
from terrains.grass import Grass
from terrains.dirt import Dirt
from renderer import Renderer
from entities.character import Character 
from entities.entity import Entity
from entities.texture import Texture
from key_input import KeyInput
from loader import Loader



class Engine:
  # initial parameters
  def __init__(self, fps: int) -> None:
    self.version: str = "0.0.2"
    self.title: str = "CRT Engine"
    self.renderer: Renderer = Renderer(f"{self.title} v{self.version}", 800, 600)
    self.key_input: KeyInput = KeyInput()
    self.loader: Loader = Loader()
    self.clock = pygame.time.Clock()
    self.font = pygame.font.SysFont("consolas", 50)
    self.fps: int = fps
    self.running: bool = True
    self.debug_info: bool = False
    self.game_state: str = ""
    self.edit_mode: bool = False
    self.icon = pygame.image.load(f"{pathlib.Path(__file__).parent.resolve()}/assets/icon.jpg")
    pygame.display.set_icon(self.icon)
    
  def run(self) -> int:
    """ placeholder for loading everything necessary
      currently manually loading for testing
    """
    player1: Character = Character(1, 40, 60, 100, 200)
    player1.type = "player"
    
    chest_image = pygame.image.load(f"{pathlib.Path(__file__).parent.resolve()}/assets/chest.png").convert()
    apple_image = pygame.image.load(f"{pathlib.Path(__file__).parent.resolve()}/assets/apple.png").convert()
    head_texture = pygame.image.load(f"{pathlib.Path(__file__).parent.resolve()}/assets/head_human.png").convert()
    body_texture = pygame.image.load(f"{pathlib.Path(__file__).parent.resolve()}/assets/body_human.png").convert()

    player1.head = Texture(0, head_texture, player1.width, player1.height/2, 0, 0).get_surface()
    player1.body = Texture(0, body_texture, player1.width, player1.height/2, 1, 1).get_surface()
    player1.create_image()
    grass_tile: Grass = Grass()
    grass_tile.scale_terrain(1)
    metal_tile: Metal = Metal()
    metal_tile.scale_terrain(1)
    dirt_tile: Dirt = Dirt()
    dirt_tile.scale_terrain(1)
    paused_text = self.font.render("PAUSED", True, (200, 200, 50))
    player_info = pygame.font.SysFont("consolas", 15)
    fps_info = pygame.font.SysFont("consolas", 20)
    player_info_text = player_info.render(f"{player1.type}: {player1.id}", True, (0, 0, 255))
    items = pygame.sprite.Group()
    consumables = pygame.sprite.Group()
    for i in range(2, 12):
      chest = Entity(2, 50, 50, i*50, 100)
      chest.image = Texture(2, chest_image, chest.width, chest.height, 0, 0).get_surface()
      items.add(chest)
      apple = Entity(3, 30, 30, i*50, 200)
      apple.image = Texture(3, apple_image, apple.width, apple.height, 0, 0).get_surface()
      consumables.add(apple)
    time = pygame.time.get_ticks()
    old_time = pygame.time.get_ticks()
    player1.active = True
    map_test = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [3,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1],
          [1,1,1,1,2,2,2,2,2,2,2,2,2,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    self.game_state = "running"
    self.loader.entities.append(player1)
    self.loader.terrains.append(grass_tile)
    self.loader.terrains.append(dirt_tile)
    self.loader.terrains.append(metal_tile)
    # start of the engine run (overhead) -> loading states
    while self.running:
      self.clock.tick(self.fps)
      mouse_pos = self.key_input.get_mouse_pos()
      fps_text = fps_info.render(f"{int(self.clock.get_fps())} FPS", True, (0,0,0))
      time_text = fps_info.render(f"{pygame.time.get_ticks()//1000} s", True, (0,0,0))
      mouse_pos_text_x = fps_info.render(f"X: {mouse_pos[0] // grass_tile.width}", True, (0,0,0))
      mouse_pos_text_y = fps_info.render(f"Y: {mouse_pos[1] // grass_tile.width}", True, (0,0,0))
      self.font.render
      self.running = self.key_input.event_handler()
      # main loop
      if self.game_state == "running":
        self.renderer.clear_surface(self.renderer.main_display, (0,0,0))
        selected_tiles = []
        for y_i, y in enumerate(map_test):
          for x_i, x in enumerate(y):
            tile = self.loader.get_item(x, self.loader.terrains)[0]
            self.renderer.render(tile.image, x_i*tile.width, y_i*tile.height)
            if mouse_pos[0] // tile.width == x_i and mouse_pos[1] // tile.height == y_i:
              selected_tiles.append((x_i*tile.width, y_i*tile.height, tile.width, tile.height))
            tile_text = self.font.render(f"{x}", True, (255, 255, 255))
            #if self.debug_info: self.renderer.render(tile_text, x_i*50+5, y_i*50+5)
        self.game_state = "paused" if pygame.K_ESCAPE in self.key_input.keys_pressed else "running"
        self.renderer.camera[0] = 100 
        if pygame.K_f in self.key_input.keys_pressed:
          self.debug_info = not self.debug_info
          self.key_input.keys_pressed.remove(pygame.K_f)
        if self.game_state == "paused": self.key_input.keys_pressed.remove(pygame.K_ESCAPE)
        collisions = pygame.sprite.spritecollide(player1, items, False)
        interactions = pygame.sprite.spritecollide(player1, items, False, collided=pygame.sprite.collide_circle)
        consumed = pygame.sprite.spritecollide(player1, consumables, True)
        player1.collided = False
        if len(collisions):
          player1.collided = True
          for dir in player1.moving:
            player1.move(dir, time)
        if len(interactions) and player1.interact:
          for rects in interactions:
            self.renderer.clear_surface(rects.image, (0, 255, 255))

        player1.update(self.key_input.keys_pressed, time)
        items.draw(self.renderer.main_display)
        consumables.draw(self.renderer.main_display)

        for rects in interactions:
          pygame.draw.rect(self.renderer.main_display, (255,0,0), rects.rect, 3)
        if len(selected_tiles): pygame.draw.rect(self.renderer.main_display, (0,0,255), selected_tiles[0], 3)
        keys_text = fps_info.render(f"K{self.key_input.keys_pressed}", True, (0,0,0))
        self.renderer.render_to_screen(player1.image, player1.x, player1.y)
        if self.debug_info:
            self.renderer.render_to_screen(player_info_text, player1.x-10, player1.y-20)
            self.renderer.render_to_screen(fps_text, self.renderer.width - 100, 50)
            self.renderer.render_to_screen(time_text, self.renderer.width - 100, 75)
            self.renderer.render_to_screen(mouse_pos_text_x, self.renderer.width - 100, 100)
            self.renderer.render_to_screen(mouse_pos_text_y, self.renderer.width - 100, 125)
            self.renderer.render_to_screen(keys_text, self.renderer.width - 100, 150)
      elif self.game_state == "paused":
        self.game_state = "running" if pygame.K_ESCAPE in self.key_input.keys_pressed else "paused"
        if self.game_state == "running": self.key_input.keys_pressed.remove(pygame.K_ESCAPE)
        self.renderer.main_display.blit(paused_text, (int(self.renderer.width/2), int(self.renderer.height/2)))
      self.renderer.update()
      time = pygame.time.get_ticks() - old_time
      old_time = pygame.time.get_ticks()
    pygame.quit()
    return 0
