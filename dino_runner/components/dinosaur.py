from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components import text_utils
from dino_runner.utils.constants import RUNNING, JUMPING, DEFAULT_TYPE
from dino_runner.utils.constants import RUNNING, JUMPING, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, JUMPING_SHIELD
import pygame
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5   
    Y_POS_DUCK = 340  #  agachar


    def __init__(self):
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}  # dino run 1 > hace referencia a la imagen patita derecha }
        self.type = DEFAULT_TYPE
        self.image = self.run_image[self.type][0]
        self.dino_rect = self.image.get_rect() # que muestre el dino
        self.dino_rect.x = self.X_POS  # para posicionarlas en el juego
        self.dino_rect.y = self.Y_POS
        
        self.jump_vel = self.JUMP_VEL

        self.step_index = 0  # indice de pasos del dino
        self.dino_run = True  
        self.dino_jump = False
        self.dino_duck = False   # variable bolleana
         
         
        self.shield= False  
        self.shield_time_up=  0   # para q paradew
        self.has_powerup=False

    def update(self, user_input): # adei > 
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()        #
        if self.dino_duck:
            self.duck()
        if user_input[pygame.K_DOWN] and not self.dino_jump: # tecla  para saltar
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 10:     # para actualixzarse , cuando de 10 pasos v
            self.step_index = 0 # empezar con patita derecha

    def draw(self, screen): #>dibujo para mandar a la pantalla
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y)) # posion carteciana 

    def event(self): 
        pass

    def run(self): # la imagen va ir cambiando depende la posicion de 0
        #self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]# si es menor a 5 va tomar la otra imagen 1
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()  # definir el tamaño
        self.dino_rect.x = self.X_POS    # actualizar posiciones
        self.dino_rect.y = self.Y_POS
        self.step_index += 1 # ir sumando de 1 en 1

    def jump(self):# para saltar
        self.image = self.jump_image[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4 # TAMAÑO DE SALTO
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL: # vuelve a su posicion inicial
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
     # TAREA
    def duck(self):    # usamos dos imagenes para sus patitas
       
        self.image = self.duck_image[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index +=1

    def check_visibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0: # SI ES MAYOR A 0 MOSTRAR MENSAJE
                font = pygame.font.Font("freesansbold.ttf",18)
                text = font.render(f'Shield enable for {time_to_show}',True,(0,0,0))
                text_rect = text.get_rect()
                text_rect.center=(500,40)
                screen.blit(text, text_rect)
            else:
                self.shield = False
                if self.type == SHIELD_TYPE:
                    self.type = DEFAULT_TYPE