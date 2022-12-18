import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS



# donde iniciamos el juego
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE) # titulo
        pygame.display.set_icon(ICON)     #icono
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #para ver imagen
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20 

        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur() # instanciar para que funcione
        self.obstacle_manager = ObstacleManager()  # instanciar

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:  # setiando una variable
            self.events() # evemtos
            self.update() #aidei
            self.draw()   #drou
        pygame.quit()    # si no se cumple se cierra la pantalla

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self): # para que se actualice
        user_input = pygame.key.get_pressed()    # las 2 lineas para que sedivuje
        self.player.update(user_input)  
        self.obstacle_manager.update(self)

    def draw(self):       # levantamiento del camino  , pedimos que dibuje en la pantalla
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self): 
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
