from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

# Generic
class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image  # para generalizar la imagen
        self.type = type    # que me diga tipo de dato que usare
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH#posicion maxima de la pantalla

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()# se elimina el ultimo de la lista

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect) # se repetira en cada objeto