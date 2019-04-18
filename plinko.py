import sys, pygame, random, time


pygame.init() #initializes the game


white = (255,255,255) #theese are RGB color things
green = (0,255,0)
blue = (0,0,255)
red = (255, 0, 0)
black= (0,0,0)


screen = pygame.display.set_mode((1800, 1000)) #game window dimensions
screen_rect=screen.get_rect()
pygame.display.set_caption('Plinko')#game name
clock=pygame.time.Clock() #chooses the FPS

gameExit=False #when to end game


myfont=pygame.font.SysFont(None, 20)
myfont2=pygame.font.SysFont(None, 32)

block_x = 900
block_y = 50
block=pygame.draw.circle(screen, red, (block_x, block_y), 30)

move = False
tick = 0
moves = 8
move_y = 5
move_x = 5

while not gameExit: #unless gameExit is true
    print move, moves
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                gameExit=True
                

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        move = True
        block_x = 900
        block_y = 50

    if move:
        if tick > 15:
            tick = 0
            choice = random.randint(1, 2)
            if choice == 1:
                move_x *= -1
        block_y += move_y
        block_x += move_x

                
                
                
    screen.fill(white)#background color
    block=pygame.draw.circle(screen, red, (block_x, block_y), 50)
    pygame.display.update() #updates the display
    clock.tick(30) #frames per second
    
pygame.quit()
quit()
