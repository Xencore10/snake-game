import pygame
import time
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (213, 50, 80)
yellow = (255, 255, 102)
green = (0,255,0)

dis_width = 200
dis_height = 160

dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Misha')
game_over=False

snake_block = 10


clock = pygame.time.Clock()

font_style = pygame.font.SysFont('arial', 14)
score_font = pygame.font.SysFont('bahnschrift', 14)
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [0, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0
    snake_speed = 15
    snake_list = []
    lenght_of_snake = 1

    xfood = round(random.randrange(0, dis_width - snake_block)/10.0) * 10.0 
    yfood = round(random.randrange(0, dis_height - snake_block)/10.0) * 10.0 

    helper = {'x' :True, 'y' :True,}
    while not game_over:
        
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", yellow)
            Your_score(lenght_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_speed = 5
                if event.key == pygame.K_LEFT and helper['x']:
                    x1_change = -snake_block
                    y1_change = 0
                    helper['x'] = False
                    helper['y'] = True 
                elif event.key == pygame.K_RIGHT and helper['x']:
                    x1_change = snake_block
                    y1_change = 0
                    helper['x'] = False
                    helper['y'] = True
                elif event.key == pygame.K_UP and helper['y']:                        
                    y1_change = -snake_block
                    x1_change = 0
                    helper['y'] = False
                    helper['x'] = True
                elif event.key == pygame.K_DOWN and helper['y']:
                    y1_change = snake_block
                    x1_change = 0
                    helper['y'] = False
                    helper['x'] = True
        
        dis.fill(blue)
        pygame.draw.rect(dis, green, [xfood, yfood, snake_block, snake_block])

        x1 += x1_change
        y1 += y1_change
        #if x1 >= dis_width or x1 < 0  or y1 >= dis_height or y1 < 0:
            #game_close = True
        if x1 > (dis_width) and x1_change == snake_block:
            x1 = 0 
        if x1 < 0 and x1_change == -snake_block:
            x1 = dis_width - snake_block

        if y1 > (dis_height) and y1_change == snake_block:
            y1 = 0
        if y1 < 0 and y1_change == -snake_block:
            y1 = dis_height - snake_block
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(lenght_of_snake - 1)
        
        pygame.display.update()

        if x1 == xfood and y1 == yfood:
            xfood = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            yfood = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            lenght_of_snake +=1

        clock.tick(snake_speed)
        
    pygame.quit()
    quit()
gameLoop()

