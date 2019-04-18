import sys
import pygame


pygame.init() #initializes the game


white = (255,255,255) #theese are RGB color things
green = (0,255,0)
blue = (0,0,255)
black= (0,0,0)


screen = pygame.display.set_mode((1800,1000)) #game window dimensions
screen_rect=screen.get_rect()
pygame.display.set_caption('Plinko')#game name
clock=pygame.time.Clock() #chooses the FPS

gameExit=False #when to end game


myfont=pygame.font.SysFont(None, 20)
myfont2=pygame.font.SysFont(None, 32)


block=pygame.draw.rect(screen, white, (550, 297, 24,24))
block_x = 290
block_y = 10
speed = 0
move = False
while not gameExit: #unless gameExit is true
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                gameExit=True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        move = True

    if move:
        speed+=0.1

    block_y+=speed
    screen.fill(white)#background color
    pygame.draw.rect(screen, blue, (block_x,block_y,20,20))
    pygame.display.update() #updates the display
    clock.tick(80) #frames per second
pygame.quit()
quit()
