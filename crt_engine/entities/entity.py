import pygame

class Entity(pygame.sprite.Sprite):

    # initial parameters
    def __init__(self, id: int, width: int, height: int, x: int = 0, y: int = 0) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.max_health = 100
        self.health = 100
        self.type = ""
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.collided = False
        self.interact = False
        self.active = False
        self.moving = []
        self.speed = 0.4
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
    def update(self, input_keys, frame_time: int):
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
