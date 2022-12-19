import pygame

from dino_runner.utils.constants import  SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
black_color = (0, 0, 0)


def get_score_element(point):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render("Points: " + str(point), True, black_color)
    text_rect = text.get_rect()
    text_rect.center= [950, 40]
    
    return text, text_rect

def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_WIDTH // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)

    return text, text_rect

def get_dino_elemen():
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render("Dino : " , True, black_color)
    text_rect = text.get_rect()
    text_rect.center= [550, 250]
    return  text_rect 


def get_number_dead(death):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(" number of deaths : " + str(death), True, black_color)
    text_rect = text.get_rect()
    text_rect.center= [550, 450]

    return text, text_rect

def get_game_hover():
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render("Dino : " ,True, black_color)
    text_rect = text.get_rect()
    text_rect.center= [380, 150]

    return  text_rect 

