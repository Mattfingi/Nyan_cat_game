import os
from random import randint
import sys, pygame
import pygame.freetype
pygame.init()
pygame.font.init()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Display
size = width, heigth = 960, 540
black = 0, 0, 0
screen = pygame.display.set_mode(size)

#Game Manager
score = 0

# Background
bg = pygame.image.load("../assets/nyan_cat_background.png")
# bg = pygame.transform.scale(bg, size)

# Nyan-Cat
cat = pygame.image.load("../assets/nyan_catbg.png")
 # cat = pygame.transform.scale(cat, (200, 100))
catrect = cat.get_rect()

# Coin
coin = pygame.image.load("../assets/coin_mario.webp")
coin = pygame.transform.scale(coin, (100, 100))
coinrect = coin.get_rect()
coinrect = (1000, 1000, 100, 100)
coin_pop = pygame.USEREVENT + 1
cling = pygame.mixer.Sound("../assets/coin.wav")

#Font
pixel_font = pygame.freetype.Font("../assets/PixelOperator8.ttf", 16)
text_area = pixel_font.render("Hello World", (255, 255, 255))

# Music
pygame.mixer.music.load("../assets/NyanCatoriginal.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Time related stuff
clock = pygame.time.Clock()
coin_timer = pygame.time.set_timer(coin_pop, 5000, 1)

# Main loop
while True:
    key = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            sys.exit()
        if event.type == coin_pop:
            coinrect = (randint(0, width), randint(0, heigth), 100, 100)

    speed = [0, 0]

    # Inputs
    if key[pygame.K_UP] == True:
        speed[1] = -5

    if key[pygame.K_DOWN] == True:
        speed[1] = 5

    if key[pygame.K_LEFT] == True:
        speed[0] = -5

    if key[pygame.K_RIGHT] == True:
        speed[0] = 5

    #Moving around
    catrect = catrect.move(speed)

    if catrect.colliderect(coinrect):
        print("Cling !")
        score += 1
        pygame.mixer.Sound.play(cling)
        # coinrect = (1000, 1000, 100, 100)
        pygame.event.post(pygame.event.Event(coin_pop))

    if catrect.right < 0:
        catrect.left = width
    if catrect.left >width:
        catrect.right = 0
    if catrect.top > heigth:
        catrect.bottom = 0
    if catrect.bottom < 0:
        catrect.top = heigth
    
    screen.fill(black)
    screen.blit(bg, (0, 0))
    screen.blit(coin, coinrect)
    screen.blit(cat, catrect)
    pixel_font.render_to(screen, catrect, "score : " + str(score), (255, 255, 255))
    # screen.fill("red", coinrect)
    pygame.display.flip()

    clock.tick(30)