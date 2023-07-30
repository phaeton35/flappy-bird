import pygame

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def draw(self, screen):
        text = self.font.render(str(self.value), True, (0, 0, 0))
        screen.blit(text, (400, 50))
