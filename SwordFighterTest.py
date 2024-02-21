import pygame, sys, random, math

def falling(sprite,obsticles):
    falling = True
    
    for surface in obsticles: # iterates through all platforms
        # checks to see if a falling object is in rage with a platform to be able to land on it.
        if sprite.rect.bottom+5 >= (surface.rect.top) and sprite.rect.bottom-5 <= (surface.rect.top) and sprite.rect.right >= (surface.rect.left) and sprite.rect.left <= (surface.rect.right):
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
        self.jumping=False #This is used to make sure a mob class doesn't jump in mid air (maybe more than twice).
        self.direction = random.choice([1,-1])

    def move(self,deltax,deltay):
        #make a collision function (make logic in game loop)
        if self.rect.left < 0 or self. rect.right>1200:
            deltax *=-5
        self.rect.centerx = self.rect.centerx+deltax*self.direction
        #Create a jump function or make the logic here.


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Player,self).__init__()

        self.image = pygame.Surface([45,50],pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("pink")
        self.rect = self.image.get_rect(center = (x,y))
        self.jumping=False
    
    def move(self,deltax,deltay):
        # Add an animation (Flip between frames each time the fucntion is called on or not)
        self.rect.center = (deltax+self.rect.centerx,self.rect.centery)



#  Game initializing

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fighter_test")
clock = pygame.time.Clock()
running = True
#Surface creation
platformlist=pygame.sprite.Group()
platformlist.add(Platform(100,500,100,50))
platformlist.add(Platform(600, 300,120,120))
enemylist=pygame.sprite.Group()
enemylist.add(Enemystart(100,100))
player=Player(600,200)
enemylist.add(player)

while running: #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        if pygame.key.get_pressed()[pygame.K_a]==True and pygame.key.get_pressed()[pygame.K_d] == False:
            player.move(-5,0)
        elif pygame.key.get_pressed()[pygame.K_d]==True and pygame.key.get_pressed()[pygame.K_a]==False:
            player.move(5,0)
            #Finnish control mapping.
    
    screen.fill("white")
    # --render objects here--
    platformlist.draw(screen)
    enemylist.draw(screen)
    for enemy in enemylist:
        if falling(enemy,platformlist) == True:
            enemy.rect.center = (enemy.rect.centerx,enemy.rect.centery+5)
        else:
            if enemy != player:
                enemy.move(1,0)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()