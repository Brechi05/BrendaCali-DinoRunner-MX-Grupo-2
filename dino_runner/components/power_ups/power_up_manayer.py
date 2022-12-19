from asyncio import shield
import random
import pygame

from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0 # cuando quiero que aparezca
        self.points = 0

    def update(self, point, game_speed, player):
        self.generate_power_ups(point)
        for powerup in self.power_ups:                  # sabe dibujarse y  se dibuja en esa pantall
            powerup.update(game_speed, self.power_ups)

            if (player.dino_rect.colliderect(powerup.rect)):
                powerup.start_time = pygame.time.get_ticks()
                player.shield = True
                player.type = powerup.type
                powerup.start_time = pygame.time.get_ticks()
                player.shield_time_up = powerup.start_time + ((random.randint(5,8) * 1000)) # el tiempo que estara con poderr
                self.power_ups.remove(powerup)


    def draw(self, screen):
        for powerup in self.power_ups:
            powerup.draw(screen)

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appers == self.points:       
                self.when_appers = random.randint(self.when_appers + 150, 500 + self.when_appers)
                self.power_ups.append(Shield())