import pygame

class button(object):
    def __init__(self,text,x,y,width,height,alpha=255):
        self._text = text
        self._bcolor = (0,0,0)
        self._tcolor = (255,255,255)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._alpha = alpha
        self._font = pygame.font.SysFont('comicsansms', 20)
        
    def drawButton(self, display):
        self.s = pygame.Surface((self._width,self._height))
        self.s.set_alpha(self._alpha)
        self.s.fill(self._bcolor)
        display.blit(self.s,(self._x,self._y))
        self.text_surf = self._font.render(self._text, True, self._tcolor)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = ((self._x+(self._width/2)),(self._y+(self._height/2)))
        display.blit(self.text_surf,self.text_rect)

    def checkClicked(self, cur):
        if self._x + self._width > cur[0] > self._x and self._y + self._height > cur[1] > self._y:
            return(True)
        else:
            return(False)
    def setTextColor(self, color):
        self._tcolor = color
    def setBackColor(self, color):
        self._bcolor = color
    def setFont(self, font):
        self._font = font
    def setAlpha(self, alpha):
        self._alpha = alpha
