from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

FONT_STYLE = 'freesansbold.ttf'
text_black_color = (0, 0, 0) #RGB 

def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)

    text = font.render(message, True, text_black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return (text, text_rect)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)

    text = font.render('Points: ' + str(points), True, text_black_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return (text, text_rect)

