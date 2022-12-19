from asyncio import events
import pygame

from dino_runner.components import text_utils
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS , GAME ,CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstaculomanager import ObstacleManager
from dino_runner.components.power_up.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.y_pos_nuve = 100
        self.x_pos_nuve = 0

        self.points = 0
        self.running = True #texto
        self.death_count = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()

        pygame.mixer.music.load("sound/MusicFondo.wav")
        

 
    def run(self):
        self.create_comment()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def create_comment(self):
        self.power_up_manager.reset_power_ups(self.points)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.obstacle_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_nuve()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        self.player.check_lives()#vidas cunatas tienes

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
    
    def draw_nuve(self):
        image_height = CLOUD.get_height()
        self.screen.blit(CLOUD, (self.x_pos_nuve, self.y_pos_nuve))
        self.screen.blit(CLOUD, (image_height + self.x_pos_nuve, self.y_pos_nuve))
        if self.x_pos_nuve <= -image_height:
            self.screen.blit(CLOUD, (image_height + self.x_pos_nuve, self.y_pos_nuve))
            self.x_pos_nuve = 1000
        self.x_pos_nuve -= self.game_speed


    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 5
        score, score_rect = text_utils.get_score_element(self.points)
        self.player.check_visibility(self.screen)
        self.screen.blit(score, score_rect)

    def show_menu(self, death_count):
        self.running = True
        self.screen.fill((255, 255, 255))
        self.print_menu_elements(self.death_count)
        pygame.display.update()
        self.handle_key_events_on_menu()
        pygame.mixer.music.play(-1)#sonido
        pygame.mixer.music.set_volume(0.1)



    def print_menu_elements(self, death_count = 0):
        half_screen_height = SCREEN_HEIGHT // 2

        if death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press any Key to Start")
            self.screen.blit(text, text_rect)
      
            text_rect_dino = text_utils.get_dino_elemen()
            self.screen.blit(ICON  , text_rect_dino)


        elif death_count > 0:
            text, text_rect = text_utils.get_centered_message("Press any Key to Restart")
            score, score_rect = text_utils.get_centered_message("Your score was: " + str(self.points), height = half_screen_height + 50)

            text_death , text_death_rect = text_utils.get_number_dead(self.death_count )
            self.screen.blit(text_death, text_death_rect)

            text_rect_dino = text_utils.get_dino_elemen()
            self.screen.blit(ICON  , text_rect_dino)

            text_game = text_utils.get_game_hover()
            self.screen.blit(GAME  , text_game)

            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                self.points = 0
                self.run()
