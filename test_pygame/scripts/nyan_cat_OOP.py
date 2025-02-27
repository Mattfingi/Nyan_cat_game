#oop test

from random import randint
import os
import pygame, sys

pygame.init()
pygame.font.init()
pygame.display.init()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Game constants
size = width,  height = 960, 540
screen = pygame.display.set_mode(size)
black = 0, 0, 0
background = pygame.image.load("../assets/nyan_cat_background.png")
clock = pygame.time.Clock()

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#Events
coin_pop = pygame.USEREVENT + 1
pygame.time.set_timer(coin_pop, 5000)

#Classes

class cat():


    def __init__(self, speed: float):
        self.cat_sprite = pygame.image.load("../assets/nyan_catbg.png")
        self.catrect = self.cat_sprite.get_rect()
        self.speed = speed

    def movement(self):
        key = pygame.key.get_pressed()
        self.direction = [0, 0]

        if key[pygame.K_UP] == True:
            self.direction[1] = -1
        if key[pygame.K_DOWN] == True:
            self.direction[1] = 1

        if key[pygame.K_LEFT] == True:
            self.direction[0] = -1

        if key[pygame.K_RIGHT] == True:
            self.direction[0] = 1

        self.x_movement = self.direction[0] * self.speed
        self.y_movement = self.direction[1] * self.speed
        # print(f"{self.x_movement, self.y_movement}")

        self.catrect = self.catrect.move(self.x_movement, self.y_movement)

class coin():

    def __init__(self):
        self.coin_sprite = pygame.image.load("../assets/coin_mario.webp")
        self.coin_sprite = pygame.transform.scale(self.coin_sprite, (100, 100))
        self.coin_rect = self.coin_sprite.get_rect()
        self.coin_rect = (randint(0, width), randint(0, height))

nyan_cat = cat(5)
coin_exist = False

#Main loop
while True:
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            sys.exit()

        if event.type == coin_pop:
            coin1 = coin()
            coin_exist = True

    nyan_cat.movement()

    screen.fill(black)
    screen.blit(background, (0, 0))
    if coin_exist:
        # screen.blit(coin1.coin_sprite, coin1.coin_rect)
        coin1.draw
    screen.blit(nyan_cat.cat_sprite, nyan_cat.catrect)

    pygame.display.flip()
    clock.tick(30)