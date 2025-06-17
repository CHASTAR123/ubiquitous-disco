import pygame
pygame.init()

WIDTH, HEIGHT,title = 600,600,'classes'
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title)

screen.fill('red')
pygame.display.update()

class Circle():
    def __init__(self,r,x,y,c):
        self.rad = r
        self.x = x
        self.y = y
        self.c = c
        self.center =(x,y)

    def draw(self):
        pygame.draw.circle(screen,self.c,self.center,self.rad)

blue = Circle(50,200,200,'blue')
blue.x = 400
print(blue.x)
blue.draw()
        