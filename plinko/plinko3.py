import sys, pygame, random, time


pygame.init() #initializes the game

white = (255,255,255) #theese are RGB color things
green = (0,255,0)
blue = (0,0,255)
red = (255, 0, 0)
black= (0,0,0)

board_x = 205
board_y = 100
board_width = 1400
board_height = 700

screen = pygame.display.set_mode((1800, 1000)) #game window dimensions
screen_rect=screen.get_rect()
pygame.display.set_caption('Plinko')#game name
clock=pygame.time.Clock() #chooses the FPS
ball_pic = pygame.image.load("ball.png").convert_alpha()
board_pic = pygame.image.load("board.png").convert_alpha()
board_pic = pygame.transform.scale(board_pic, (board_width, board_height))
peg_pic = pygame.image.load("peg.png").convert_alpha()
peg_pic = pygame.transform.scale(peg_pic, (25, 25))
title_pic = pygame.image.load("Title.png").convert_alpha()
column_pic = pygame.image.load("col.png").convert_alpha()
column_pic = pygame.transform.scale(column_pic, (1200, 250))
bg_pic = pygame.image.load("background.png").convert_alpha()
bg_pic = pygame.transform.scale(bg_pic, (1800, 1000))

gameExit=False #when to end game


myfont=pygame.font.SysFont(None, 20)
myfont2=pygame.font.SysFont(None, 32)

block_x = 870
block_y = 150

move = False
tick = 0
moves = 8
move_y = 4
move_x = 3.8

options = [1,2,3,4,5,6,7,8]

points = [8,6,4,2,2,4,6,8]

count = {0:0, 2:0, 4:0, 6:0, 8:0}

def getCol():

    if block_x < 460:
        return 1
    elif block_x < 506:
        return 2
    elif block_x < 656:
        return 3
    elif block_x < 806:
        return 4
    elif block_x < 956:
        return 5
    elif block_x < 1106:
        return 6
    elif block_x < 1256:
        return 7
    else:
        return 8

def reset():
    global block_x
    global block_y
    global moves
    global move
    move = True
    block_x = 870
    block_y = 150
    moves = 8

trials = 0

while not gameExit: #unless gameExit is true

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                gameExit=True
                

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        reset()

    if move:
        if (block_y - 150) % 80 == 0:
            moves -= 1
            choice = random.randint(1, 2)
            if choice == 1:
                move_x *= -1
        block_y += move_y
        block_x += move_x
        
    if moves == 0:
        trials += 1
        move = False
        col = getCol()
        random.shuffle(options)
        c1 = options[0]
        c2 = options[1]
        if col == c1 or col == c2:
            #print "Success:", c1, c2, col
            point_now = points[col - 1]
            count[point_now] += 1
        else:
            count[0] += 1

                
    screen.blit(bg_pic, (0,0))
    screen.blit(column_pic, (285, 740))
    
    screen.blit(board_pic, (board_x, board_y))
    screen.blit(ball_pic, (block_x, block_y))
    screen.blit(title_pic, (625,-30))
    hGap = 150
    vGap = 82
    middle = 881
    for i in range(7):
        for j in range(i+1):
            if (i%2==0):
                screen.blit(peg_pic, (middle-(i/2*hGap)+(j*hGap),95+(i*vGap) + 100))
            else:
                screen.blit(peg_pic, (middle-((i+1)/2*hGap)+(j*hGap)+(hGap/2), 95+(i*vGap) + 100))

    

        
    pygame.display.update() #updates the display
    clock.tick(30) #frames per second

pygame.quit()
