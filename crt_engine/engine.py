import pygame
import pathlib
from renderer import Renderer
from entities.character import Character 
from key_input import KeyInput


class Engine:
    # initial parameters
    def __init__(self, fps: int) -> None:
        self.version = "0.0.1"
        self.title = "CRT Engine"
        self.renderer = Renderer(f"{self.title} v{self.version}", 800, 600)
        self.key_input = KeyInput()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 50)
        self.fps = fps
        self.running = True
        self.game_state = ""
        print(pathlib.Path(__file__).resolve())
        self.icon = pygame.image.load(f"{pathlib.Path(__file__).parent.resolve()}/assets/icon.jpg")
        pygame.display.set_icon(self.icon)
        
    def run(self) -> int:
        """ placeholder for loading everything necessary
            currently manually loading for testing
        """
        player1 = Character(1, 40, 40)
        player1.type = "player"
        paused_text = self.font.render("PAUSED", True, (200, 200, 50))
        player_info = pygame.font.SysFont("consolas", 15)
        player_info_text = player_info.render(f"{player1.type}: {player1.id}", True, (0, 0, 255))
        items = pygame.sprite.Group()
        consumables = pygame.sprite.Group()
        for i in range(2, 12):
            items.add(Character(2, 50,50, i*50, 100))
            consumables.add(Character(3, 20, 20, i*50, 200))
        self.renderer.clear_surface(player1.image, (255, 0, 0))
        for item in items:
            self.renderer.clear_surface(item.image, (0, 0, 255))
        for cons in consumables:
            self.renderer.clear_surface(cons.image, (0, 255, 0))
        time = pygame.time.get_ticks()
        old_time = pygame.time.get_ticks()
        player1.active = True
        self.game_state = "running"
        # start of the engine run (overhead) -> loading states
        while self.running:
            self.clock.tick(self.fps)
            self.running = self.key_input.event_handler()
            # main loop
            if self.game_state == "running":
                self.renderer.clear_surface(self.renderer.main_display, (0,0,0))
                self.game_state = "paused" if pygame.K_ESCAPE in self.key_input.keys_pressed else "running"
                if self.game_state == "paused": self.key_input.keys_pressed.remove(pygame.K_ESCAPE)
                collisions = pygame.sprite.spritecollide(player1, items, False)
                interactions = pygame.sprite.spritecollide(player1, items, False, collided=pygame.sprite.collide_circle)
                consumed = pygame.sprite.spritecollide(player1, consumables, True)
                player1.collided = False
                if len(collisions):
                    player1.collided = True
                    for dir in player1.moving:
                        player1.move(dir, False)
                if len(interactions) and player1.interact:
                    for rects in interactions:
                        self.renderer.clear_surface(rects.image, (0, 255, 255))
                player1.update(self.key_input.keys_pressed, time)
                items.draw(self.renderer.main_display)
                consumables.draw(self.renderer.main_display)
                for rects in interactions:
                    pygame.draw.rect(self.renderer.main_display, (255,0,0), rects.rect, 3)
                self.renderer.main_display.blit(player1.image, (player1.x,player1.y))
                self.renderer.main_display.blit(player_info_text, (player1.x, player1.y - 30))
            elif self.game_state == "paused":
                self.game_state = "running" if pygame.K_ESCAPE in self.key_input.keys_pressed else "paused"
                if self.game_state == "running": self.key_input.keys_pressed.remove(pygame.K_ESCAPE)
                self.renderer.main_display.blit(paused_text, (int(self.renderer.width/2), int(self.renderer.height/2)))
            self.renderer.update()
            time = pygame.time.get_ticks() - old_time
            old_time = pygame.time.get_ticks()
        pygame.quit()
        return 0
