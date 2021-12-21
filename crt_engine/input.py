import pygame

class Input:
    def __init__(self):
        self.active_object = None
        
    def event_handler(self) -> int:
        for event in pygame.event.get():
            if self.active_object:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.active_object.move(1, True)
                    if event.key == pygame.K_s:
                        self.active_object.move(2, True)
                    if event.key == pygame.K_d:
                        self.active_object.move(3, True)
                    if event.key == pygame.K_a:
                        self.active_object.move(4, True)
                    if event.key == pygame.K_f:
                        self.active_object.interact = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.active_object.move(1, False)
                    if event.key == pygame.K_s:
                        self.active_object.move(2, False)
                    if event.key == pygame.K_d:
                        self.active_object.move(3, False)
                    if event.key == pygame.K_a:
                        self.active_object.move(4, False)
                    if event.key == pygame.K_f:
                        self.active_object.interact = False
                    

            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
        return 1
