import pygame
from bird import Bird
from pipe import Pipe
from score import Score
from sound import Sound

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = [Pipe()]
        self.score = Score()
        self.sound = Sound()
        self.game_over = False

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()
                    self.sound.play_flap()
                elif event.key == pygame.K_r:
                    self.restart()

    def update(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()
            if pipe.off_screen():
                self.pipes.remove(pipe)
                self.pipes.append(Pipe())
            if pipe.passed_by(self.bird):
                self.score.increment()
                self.sound.play_score()
            if pipe.collides_with(self.bird) or self.bird.y < 0 or self.bird.y > 550:
                self.sound.play_game_over()
                pygame.time.delay(3000)  # Delay for 3 seconds
                self.restart()
                # self.game_over = True


    def draw(self):
        self.screen.fill((255, 255, 255))
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()

    def restart(self):
        self.bird = Bird()
        self.pipes = [Pipe()]
        self.score.reset()
        self.game_over = False

