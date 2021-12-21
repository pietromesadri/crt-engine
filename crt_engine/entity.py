import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, id: int, width: int, height: int, x: int = 0, y: int = 0):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.collided = False
        self.interact = False
        self.moving = []
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def set_pos(self, x_cood: int, y_coord: int) -> None:
        self.x = x_cood
        self.y = y_coord
        self.rect.update(self.x, self.y, self.width, self.height)
    
    def move(self, direction: int, active: bool) -> None:
        if direction == 1:
            self.move_up = active
            if self.collided:
                self.set_pos(self.x, self.y + self.speed)
        elif direction == 2:
            self.move_down = active
            if self.collided:
                self.set_pos(self.x, self.y - self.speed)
        elif direction == 3:
            self.move_right = active
            if self.collided:
                self.set_pos(self.x - self.speed, self.y)
        elif direction == 4:
            self.move_left = active
            if self.collided:
                self.set_pos(self.x + self.speed, self.y)
            
    def update(self, frame_time: int):
        self.moving = []
        if self.move_up:
            self.moving.append(1)
            self.y -= self.speed * frame_time / 20
        if self.move_down:
            self.moving.append(2)
            self.y += self.speed * frame_time / 20
        if self.move_right:
            self.moving.append(3)
            self.x += self.speed * frame_time / 20
        if self.move_left:
            self.moving.append(4)
            self.x -= self.speed * frame_time / 20
        self.rect.update(self.x, self.y, self.width, self.height)