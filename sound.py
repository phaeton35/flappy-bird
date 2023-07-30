import pygame

class Sound:
    def __init__(self):
        self.flap_sound = pygame.mixer.Sound('flap.wav')
        self.score_sound = pygame.mixer.Sound('score.wav')
        self.game_over_sound = pygame.mixer.Sound('game_over.wav')

    def play_flap(self):
        self.flap_sound.play()

    def play_score(self):
        self.score_sound.play()

    def play_game_over(self):
        self.game_over_sound.play()
