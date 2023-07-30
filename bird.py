import pygame

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0
        self.gravity = 1
        self.flap_power = 15
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def flap(self):
        self.velocity = -self.flap_power

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
