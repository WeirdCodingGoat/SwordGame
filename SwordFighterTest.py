import pygame, sys, random, math

# pygame documentation: https://www.pygame.org/docs/
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super(Square,self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.convert_alpha()
        self.image.fill("brown")
        self.rect = self.image.get_rect(center = (x,y))

class Enemystart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Enemystart,self).__init__()
        self.image = pygame.Surface((10,10),pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (x,y))
        self.jumping=False
        self.direction = random.choice([1,-1])

    def move(self,deltax,deltay):
        #make a collision function (make logic in game loop)
        if self.rect.left < 0 or self. rect.right>1200:
            deltax *=-5

enemylist=pygame.sprite.Group
enemylist.add(Enemystart(100,100))
pygame.init()
screen = pygame.display.set_mode((1200,640))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    screen.fill("white")
    # --render objects here--
    enemylist.draw()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()