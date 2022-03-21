import pygame
import random

pygame .init()

#rbg collour
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#screen size
screen_width = 1200
screen_higth = 600
gameWindow = pygame.display.set_mode((screen_width,screen_higth))

#titil
pygame.display.set_caption("Snake game")
pygame.display.update()

#snake size movement

#clock
clock = pygame.time.Clock()
#font a size
font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
     pygame.draw.rect(gameWindow,color, [x,y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to snake game ",black,350,200)
        text_screen("press Space bar to start ", black, 370, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit_game = True
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  gameloop()
        pygame.display.update()
        clock.tick(60)



#game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 70
    velocity_x = 0
    velocity_y = 0

    snake_list = []
    snake_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_higth / 2)
    score = 0

    snake_size = 10
    fps = 30  # fps rate game fast korar jonno

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("game over ! press Enter to continue",red,250,100)
                #game quit korar jonno
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                #game return korar jonno
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
              exit_game = True

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                            velocity_x = 5
                            velocity_y = 0
                    if event.key == pygame.K_a:
                            velocity_x = -5
                            velocity_y = 0
                    if event.key == pygame.K_w:
                            velocity_y = -5
                            velocity_x = 0
                    if event.key == pygame.K_s:
                            velocity_y = 5
                            velocity_x = 0




                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                 score +=1
                # print ("score: ",score * 10) # score koto koray barabo ta dakhar jonno

                 food_x = random.randint(20, screen_width / 2)
                 food_y = random.randint(20, screen_higth / 2)
                 snake_length +=5
            #colour add
                gameWindow.fill(white)
                text_screen("score: " + str(score * 10),red, 5, 5)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snake_list.append(head)

                if len(snake_list)>snake_length:
                    del snake_list[0]
                #snake ar ga a kamur laglay
                if head in snake_list[:-1]:
                    game_over = True



                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_higth:
                    game_over = True

                 #  pygame.draw.rect(gameWindow, black, [snake_x,snake_y,snake_size,snake_size])
                plot_snake(gameWindow,black,snake_list,snake_size)

        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()