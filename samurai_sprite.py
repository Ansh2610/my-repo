import pygame
from pygame.locals import *
from PIL import Image
import spritesheet

SIZE_MULTIPLIER = 1.9
BG = (0,0,0)
X_DIM = 96
Y_DIM = 84

def get_idle_images():
    samurai_idle_right_images = []
    samurai_idle_left_images = []
    for i in range(6):
        ss_url = "character_sprites/Samurai/Idle.png"
        ss = spritesheet.spritesheet(ss_url)
        x_coord = (X_DIM/4 + i*X_DIM*4/3)
        y_coord = 128-Y_DIM
        coords = (x_coord,y_coord, X_DIM,Y_DIM)
        image = ss.image_at(coords).convert_alpha()
        image.set_colorkey(BG)
        bigger_img = pygame.transform.scale(image, (image.get_width()*SIZE_MULTIPLIER, image.get_height()*SIZE_MULTIPLIER))
        samurai_idle_right_images.append(bigger_img)
        bigger_img = pygame.transform.flip(bigger_img, True, False)
        samurai_idle_left_images.append(bigger_img)

    return (samurai_idle_right_images, samurai_idle_left_images)


def get_running_images():
    samurai_running_right_images = []
    samurai_running_left_images = []
    for i in range (8):
        ss_url = "character_sprites/Samurai/Run.png"
        ss = spritesheet.spritesheet(ss_url)
        x_coord = (X_DIM/4 + i*X_DIM*4/3)
        y_coord = 128-Y_DIM
        coords = (x_coord,y_coord, X_DIM,Y_DIM)
        image = ss.image_at(coords).convert_alpha()
        image.set_colorkey(BG)
        bigger_img = pygame.transform.scale(image, (image.get_width()*SIZE_MULTIPLIER, image.get_height()*SIZE_MULTIPLIER))
        samurai_running_right_images.append(bigger_img)
        bigger_img = pygame.transform.flip(bigger_img, True, False)
        samurai_running_left_images.append(bigger_img)


    return (samurai_running_right_images, samurai_running_left_images)

def get_attack_1_images():
    samurai_attack_1_right_images = []
    samurai_attack_1_left_images = []
    for i in range (6):
        ss_url = "character_sprites/Samurai/Attack_1.png"
        ss = spritesheet.spritesheet(ss_url)
        x_coord = (X_DIM/4 + i*X_DIM*4/3)
        y_coord = 128-Y_DIM
        coords = (x_coord,y_coord, X_DIM,Y_DIM)
        image = ss.image_at(coords).convert_alpha()
        image.set_colorkey(BG)
        bigger_img = pygame.transform.scale(image, (image.get_width()*SIZE_MULTIPLIER, image.get_height()*SIZE_MULTIPLIER))
        samurai_attack_1_right_images.append(bigger_img)
        bigger_img = pygame.transform.flip(bigger_img, True, False)
        samurai_attack_1_left_images.append(bigger_img)

    return (samurai_attack_1_right_images, samurai_attack_1_left_images)

def get_attack_2_images():
    samurai_attack_2_right_images = []
    samurai_attack_2_left_images = []
    for i in range (4):
        ss_url = "character_sprites/Samurai/Attack_2.png"
        ss = spritesheet.spritesheet(ss_url)
        x_coord = (X_DIM/4 + i*X_DIM*4/3)
        y_coord = 128-Y_DIM
        coords = (x_coord,y_coord, X_DIM,Y_DIM)
        image = ss.image_at(coords).convert_alpha()
        image.set_colorkey(BG)
        bigger_img = pygame.transform.scale(image, (image.get_width()*SIZE_MULTIPLIER, image.get_height()*SIZE_MULTIPLIER))
        samurai_attack_2_right_images.append(bigger_img)
        bigger_img = pygame.transform.flip(bigger_img, True, False)
        samurai_attack_2_left_images.append(bigger_img)


    return (samurai_attack_2_right_images, samurai_attack_2_left_images)

def get_attack_3_images():
    samurai_attack_3_right_images = []
    samurai_attack_3_left_images = []
    for i in range (3):
        ss_url = "character_sprites/Samurai/Attack_3.png"
        ss = spritesheet.spritesheet(ss_url)
        x_coord = (X_DIM/4 + i*X_DIM*4/3)
        y_coord = 128-Y_DIM
        coords = (x_coord,y_coord, X_DIM,Y_DIM)
        image = ss.image_at(coords).convert_alpha()
        image.set_colorkey(BG)
        bigger_img = pygame.transform.scale(image, (image.get_width()*SIZE_MULTIPLIER, image.get_height()*SIZE_MULTIPLIER))
        samurai_attack_3_right_images.append(bigger_img)
        bigger_img = pygame.transform.flip(bigger_img, True, False)
        samurai_attack_3_left_images.append(bigger_img)


    return (samurai_attack_3_right_images, samurai_attack_3_left_images)

def get_jump_images():    
    samurai_jump_right_images = []
    samurai_jump_left_images = []
    for i in range (12):
        ss_url = "character_sprites/Samurai/Jump.png"
        ss = spritesheet.spritesheet(ss_url)
        x_coord = (X_DIM/4 + i*X_DIM*4/3)
        y_coord = 128-Y_DIM
        coords = (x_coord,y_coord, X_DIM,Y_DIM)
        image = ss.image_at(coords).convert_alpha()
        image.set_colorkey(BG)
        bigger_img = pygame.transform.scale(image, (image.get_width()*SIZE_MULTIPLIER, image.get_height()*SIZE_MULTIPLIER))
        samurai_jump_right_images.append(bigger_img)
        bigger_img = pygame.transform.flip(bigger_img, True, False)
        samurai_jump_left_images.append(bigger_img)

    return (samurai_jump_right_images, samurai_jump_left_images)