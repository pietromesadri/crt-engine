import pygame

class Entity(pygame.sprite.Sprite):

    # initial parameters
    def __init__(self, id: int = 1, width: int = 1, height: int = 1, x: int = 0, y: int = 0,
                 speed: float = 0.0, max_health: int = 100, health: int = 100) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.id: int = id
        self.width: int = width
        self.height: int = height
        self.x: int = x
        self.y: int = y
        self.max_health: int = max_health
        self.health: int = health
        self.type: str = ""
        self.move_up: bool = False
        self.move_down: bool = False
        self.move_left: bool = False
        self.move_right: bool = False
        self.collided: bool = False
        self.interact: bool = False
        self.active: bool = False
        self.moving: list = []
        self.speed: float = speed
        self.image = pygame.Surface([self.width, self.height])
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def set_pos(self, x_cood: int, y_coord: int) -> None:
        self.x = x_cood
        self.y = y_coord
        self.rect.update(self.x, self.y, self.width, self.height)

    # control entity movement
    def move(self, direction: int, frame_time) -> None:
        if direction == 1:
            self.move_up = self.active
            if self.collided:
                self.y += self.speed * frame_time
        elif direction == 2:
            self.move_down = self.active
            if self.collided:
                self.y -= self.speed * frame_time
        elif direction == 3:
            self.move_right = self.active
            if self.collided:
                self.x -= self.speed * frame_time
        elif direction == 4:
            self.move_left = self.active
            if self.collided:
                self.x += self.speed * frame_time

    # function called by sprite groups 
    def update(self, input_keys, frame_time: int) -> None:
        self.moving = []
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
