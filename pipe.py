import pygame
import random

class Pipe:
    def __init__(self):
        self.x = 800
        self.gap_y = random.randint(200, 400)
        self.width = 100
        self.height = 600
        self.velocity = 5
        self.passed = False
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        self.bottom_rect = pygame.Rect(self.x, self.gap_y + 200, self.width, self.height)

    def update(self):
        self.x -= self.velocity
        self.top_rect.topleft = (self.x, 0)
        self.bottom_rect.topleft = (self.x, self.gap_y + 200)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.top_rect)
        pygame.draw.rect(screen, (0, 255, 0), self.bottom_rect)

    def off_screen(self):
        return self.x + self.width < 0

    def passed_by(self, bird):
        if not self.passed and self.x + self.width < bird.x:
            self.passed = True
            return True
        return False

    def collides_with(self, bird):
        return self.top_rect.colliderect(bird.rect) or self.bottom_rect.colliderect(bird.rect)
