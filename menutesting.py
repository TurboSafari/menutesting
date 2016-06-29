#!/usr/bin/env python
import pygame,sys,time,random, buttons

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

def drawMenu():
    # draw main menu
    # possibly refined to get rid of hard coding
    x = ((display_width/2)-75)
    y = ((display_height/2)-100)
    s = pygame.Surface((150,180))   # the size of your rect
    s.set_alpha(200)                # alpha level
    s.fill(gray)                    # this fills the entire surface
    game_display.blit(s, (x,y))     # adds to screen
    butt = []
    for i in range(5):
        butt.append(buttons.button('Continue',x+5,y+5+(i*35),140,30))
        butt[i].setFont(small_font)
        butt[i].setTextColor((0,255,0))
        butt[i].setBackColor((0,0,255))
        butt[i].setHover(gray,True)
        butt[i].setAlpha(50)
        butt[i].drawButton(game_display)
        cur = pygame.mouse.get_pos()            
        click = pygame.mouse.get_pressed()
        if pygame.mouse.get_pressed() == (1,0,0):
            if butt[i].checkClicked():
                print 'clicked'
    pygame.display.update()

def drawScrollWindow(slide_pos):
    width = 165
    height = 145
    x = (display_width-width-50)
    y = (display_height-height-50)
    s = pygame.Surface((width,height))
    bag_slot = []
    for i in range(60): bag_slot.append(buttons.button(str(i),x,y,30,30))#initalize bag slots
    bag_length = len(bag_slot)
    bar_size = ((height-40)/((bag_length/4)-3))+1
    s.set_alpha(200)
    s.fill(gray)
    game_display.blit(s,(x,y))

    slide_up =  buttons.button('/\\',x+width-20,y+5,15,15)#scroll up object
    slide_up.drawButton(game_display)
    slide_down = buttons.button('\\/',x+width-20,y+height-20,15,15)#scroll down object
    slide_down.drawButton(game_display)

    if pygame.mouse.get_pressed() == (1,0,0): #scroll bar event handling
        if 0 < slide_pos:
            if slide_up.checkClicked():
                slide_pos -= 1
        if slide_pos < ((bag_length/4)-4):
            if slide_down.checkClicked():
                slide_pos += 1
    
    slide_bar = buttons.button('',x+width-20,y+20+(slide_pos*bar_size),15,bar_size)#create slide bar object
    slide_bar.drawButton(game_display)#display slide bar

    #display bag slots
    for iy in range(4):
        for ix in range(4):
            bag_slot[(iy*4)+(slide_pos*4)+ix].setX(x+5+(ix*35))
            bag_slot[(iy*4)+(slide_pos*4)+ix].setY(y+5+(iy*35))
            bag_slot[(iy*4)+(slide_pos*4)+ix].drawButton(game_display)
                                        
    return(slide_pos)
       
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

        game_display.blit(img,(0,0))
        if back_pack:
            slide_pos = drawScrollWindow(slide_pos)
        if menu:
            drawMenu()
        pygame.display.update()
        clock.tick(fps)

gameLoop()
