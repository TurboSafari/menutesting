#!/usr/bin/env python
import pygame,sys,time,random
from buttons import button

# menu testing

pygame.init()


white = (255,255,255)
gray = (100,100,100)
lgray = (200,200,200)
black = (0,0,0)
lblack = (40,40,40)


display_width = 900
display_height = 500
game_display = pygame.display.set_mode((display_width,display_height))

img = pygame.image.load('banshee_1.jpg')

small_font = pygame.font.SysFont('comicsansms', 20)
medium_font = pygame.font.SysFont('comicsansms', 50)
large_font = pygame.font.SysFont('comicsansms', 80)

fps = 30
clock = pygame.time.Clock()

def drawScrollWindow(slide_pos):
    width = 165
    height = 145
    x = (display_width-width-50)
    y = (display_height-height-50)
    s = pygame.Surface((width,height))
    bag_slot = []
    for i in range(60):
        bag_slot.append(str(i))
    bag_length = len(bag_slot)
    bar_size = ((height-40)/((bag_length/4)-3))+1
    s.set_alpha(200)
    s.fill(gray)
    game_display.blit(s,(x,y))

    drawButton('',x+width-20,y+20+(slide_pos*bar_size),15,bar_size,black,black) #draw slide bar

    slide_pos += drawSlidBar('/\\',x+width-20,y+5,15,15,black,'up',slide_pos,bag_length) #draw scroll arrow
    slide_pos += drawSlidBar('\\/',x+width-20,y+height-20,15,15,black,'down',slide_pos,bag_length)
    
    for iy in range(4):
        for ix in range(4):
            #draw buttons in window aka back pack slots special event handling to come
            drawButton(bag_slot[(iy*4)+(slide_pos*4)+ix],(x+5+(ix*35)),(y+5+(iy*35)),30,30,black,lblack)
    return(slide_pos)
    
def drawMenu():
    # draw main menu
    # possibly refined to get rid of hard coding
    x = ((display_width/2)-75)
    y = ((display_height/2)-100)
    s = pygame.Surface((150,180))   # the size of your rect
    s.set_alpha(200)                # alpha level
    s.fill(gray)                    # this fills the entire surface
    game_display.blit(s, (x,y))     # adds to screen

    butt = button('Continue',x+5,y+5,140,30)
    butt.setFont(small_font)
    butt.setTextColor((0,255,0))
    butt.setBackColor((0,0,255))
    butt.setAlpha(50)
    butt.drawButton(game_display)
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        if butt.checkClicked(cur):
            print 'clicked'


    pygame.display.update()
    
def drawSlidBar(text,x,y,width,height,color,action,pos,bag_length):
    # draws slide bar and defines event handling
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(game_display,color,(x,y,width,height))
    buttonText(text,(255,255,255),x,y,width,height)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            if action == 'up':
                if pos > 0:
                    clock.tick(10)
                    return(-1)
                
            if action == 'down':
                if pos < (bag_length/4)-4:
                    clock.tick(10)
                    return(1)

    return(0)
    
    
def drawButton(text,x,y,width,height,inactive_color,active_color,action=None):
    # draws button and defines event handling
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(game_display,active_color,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == 'play':
                gameLoop()
            if action == 'quit':
                gameQuit()

    else:
        pygame.draw.rect(game_display,inactive_color,(x,y,width,height))
    buttonText(text,(255,255,255),x,y,width,height)

def buttonText(msg,color,x,y,width,height,size='small'):
    # centers text on buttons
    textSurf, textRect = textObjects(msg,color,size)
    textRect.center = ((x+(width/2)),y+(height/2))
    game_display.blit(textSurf, textRect)
    
def textObjects(text, color, size):
    # font size handling and returns text on screen
    if size == 'small':
        textSurface = small_font.render(text, True, color)
    elif size == 'medium':
        textSurface = medium_font.render(text, True, color)
    elif size == 'large':
        textSurface = large_font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def gameQuit():
    # quit game
    pygame.quit()
    sys.exit()
    quit()
    
def gameLoop():
    # main event handling
    menu = False
    back_pack = False
    slide_pos = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if menu == True:
                        menu = False
                    elif menu == False:
                        menu = True
                if event.key == pygame.K_b:
                    if back_pack == True:
                        back_pack = False
                    elif back_pack == False:
                        back_pack = True

        #game_display.fill(white)
        game_display.blit(img,(0,0))
        if back_pack:
            slide_pos = drawScrollWindow(slide_pos)
        if menu:
            drawMenu()
        pygame.display.update()
        clock.tick(fps)

gameLoop()
