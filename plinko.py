import sys, pygame, random, time


pygame.init() #initializes the game


white = (255,255,255) #theese are RGB color things
green = (0,255,0)
blue = (0,0,255)
red = (255, 0, 0)
black= (0,0,0)

board_x = 205
board_y = 0
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
gameExit=False #when to end game


myfont=pygame.font.SysFont(None, 20)
myfont2=pygame.font.SysFont(None, 32)

block_x = 870
block_y = 50
#vblock=pygame.draw.circle(screen, red, (block_x, block_y), 30)

move = False
tick = 0
moves = 8
move_y = 4
move_x = -3.8

while not gameExit: #unless gameExit is true
    #print move, moves
    print block_x, block_y
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                gameExit=True
                

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        move = True
        block_x = 870
        block_y = 50
        moves = 8

    if move:
        if (block_y - 50) % 80 == 0:
            moves -= 1
            tick = 0
            choice = random.randint(1, 2)
            #choice = 2
            if choice == 1:
                move_x *= -1
        block_y += move_y
        block_x += move_x
    if moves == 0:
        move = False
                
                
                
    screen.fill(white)#background color
    #block=pygame.draw.circle(screen, red, (block_x, block_y), 50)
    screen.blit(board_pic, (board_x, board_y))
    screen.blit(ball_pic, (block_x, block_y))
    hGap = 150
    vGap = 82
    middle = 881
    for i in range(7):
        for j in range(i+1):
            if (i%2==0):
                screen.blit(peg_pic, (middle-(i/2*hGap)+(j*hGap),95+(i*vGap)))
            else:
                screen.blit(peg_pic, (middle-((i+1)/2*hGap)+(j*hGap)+(hGap/2), 95+(i*vGap)))

    for i in range(9):
        pygame.draw.circle(screen, black, (board_x + ((i + 1) * 140), board_y + board_height), 2)
        
    pygame.display.update() #updates the display
    clock.tick(30) #frames per second
    
pygame.quit()
quit()
