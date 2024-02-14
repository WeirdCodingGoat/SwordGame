import pygame, sys, random, math

def falling(sprite,obsticles):
    falling = True
    # The tops of a surface in obsticles.
    top=()
    top2=()
    # The bottoms of sprites
    bottom=()
    bottom2=()
    for surface in obsticles:
        top=(surface.rect.top,surface.rect.left)
        top2=(surface.rect.top,surface.rect.right)
        bottom=(sprite.rect.bottom,sprite.rect.left)
        bottom2=(sprite.rect.bottom,sprite.rect.right)

        # Clipline will not be the most fit for this instance.
        if sprite.rect.clipline(top,bottom) or sprite.rect.clipline(top2,bottom2):
                falling = False
                sprite.rect.bottom = (surface.rect.top)
    return falling



# pygame documentation: https://www.pygame.org/docs/
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super(Platform,self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.convert_alpha()
        self.image.fill("brown")
        self.rect = self.image.get_rect(center = (x,y))

class Enemystart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Enemystart,self).__init__()
        
        self.image = pygame.Surface([50,50],pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (x,y))
        self.jumping=False
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = random.choice([1,-1])

    def move(self,deltax,deltay):
        #make a collision function (make logic in game loop)
        if self.rect.left < 0 or self. rect.right>1200:
            deltax *=-5

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fighter_test")
clock = pygame.time.Clock()
running = True
platformlist=pygame.sprite.Group()
platformlist.add(Platform(100,500,100,50))
enemylist=pygame.sprite.Group()
enemylist.add(Enemystart(100,100))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    screen.fill("white")
    # --render objects here--
    platformlist.draw(screen)
    enemylist.draw(screen)
    for enemy in enemylist:
        if falling(enemy,platformlist) == True:
            enemy.rect.center = (enemy.rect.centerx,enemy.rect.centery-5)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()