import pygame, sys, random, math

def jump(sprite,obsticles):
    obsticle=0
    
    sprite.jumping=True
    ypos1=sprite.rect.top
  #  for surface in obsticles:
   #     if surface.solid:
    #        if surface.rect.bottom < ypos1-20 and surface.rect.right > sprite.rect.left and surface.rect.left < sprite.rect.right:
     #           obsticle=surface
   # if type(obsticle) != type(int(1)):
    #    while sprite.rect.top > ypos1-10 and sprite.rect.top != obsticle.rect.bottom:
     #       if sprite.rect.top < obsticle.rect.bottom:
      #          sprite.rect.top-=4
       #     elif sprite.rect.top-4 > obsticle.rect.bottom and obsticle.rect.right > sprite.rect.left and obsticle.rect.left < sprite.rect.right:
        #        sprite.rect.top-=4
         #   else:
          #      sprite.rect.top=obsticle.rect.bottom
    # Make sure to check for jumping up into an object from adjacent placement.
    while sprite.rect.top > ypos1-80:
      sprite.rect.top-=4
      
    sprite.jumping=False

#    if type(obsticle) != type(int(1)):
 #       while sprite.rect.top < ypos1-10 and sprite.rect.top-4 > obsticle.rect.bottom or obsticle.rect.right < obsticle.rect.left or obsticle.rect.left > sprite.rect.right:
  #          sprite.rect.top-=4
   #     if sprite.rect.top -3 <= obsticle.rect.bottom 
    


def falling(sprite,obsticles):
    falling = True

    for surface in obsticles: # iterates through all platforms
        # checks to see if a falling object is in rage with a platform to be able to land on it.
        if surface.solid or surface.semisolid:
            if sprite.rect.bottom+5 >= (surface.rect.top) and sprite.rect.bottom-5 <= (surface.rect.top) and sprite.rect.right > (surface.rect.left) and sprite.rect.left < (surface.rect.right):
                    falling = False
                    sprite.rect.bottom = (surface.rect.top)
    return falling

def player_move(player,obsticles):
    if pygame.key.get_pressed()[pygame.K_a]==True and pygame.key.get_pressed()[pygame.K_d] == False:
        player.move(-3,0)
    elif pygame.key.get_pressed()[pygame.K_d]==True and pygame.key.get_pressed()[pygame.K_a]==False:
        player.move(3,0)
    if pygame.key.get_pressed()[pygame.K_w]==True:
      print(player.jumps)
      if falling(player,platformlist) != True or player.jumps <1: #Checks if player has jumped 2 times consecuativly. ("or" mut be bugging it)
        player.jumps+=1
        jump(player,obsticles)


# pygame documentation: https://www.pygame.org/docs/
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super(Platform,self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.convert_alpha()
        self.image.fill("brown")
        self.rect = self.image.get_rect(center = (x,y))
        self.solid = True
        self.semisolid = True
        




class Enemystart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Enemystart,self).__init__()
        
        self.image = pygame.Surface([50,50],pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (x,y))
        self.jumping=False #This is used to make sure a mob class doesn't jump in mid air (maybe more than twice).
        self.direction = random.choice([1,-1])
        self.name = "enemy"

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
        self.image.fill("#ff42ba")
        self.rect = self.image.get_rect(center = (x,y))
        self.jumping=False
        self.jumps=0
        self.name = "player"
    
    def move(self,deltax,deltay):
        # Add an animation (Flip between frames each time the fucntion is called on or not)
        self.rect.centerx = deltax+self.rect.centerx
        if deltay:
            
            self.rect.centery = +self.rect.centery
            # If gravity interupts jump un hashtag the and jump part of the checking for falling.
            # Maybe use a while loop.




#  Game initializing

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fighter_test")
clock = pygame.time.Clock()
running = True
#Surface creation
platformlist=pygame.sprite.Group()
platformlist.add(Platform(100,500,100,50))
platformlist.add(Platform(370,420,300,50))
platformlist.add(Platform(600, 300,120,120))
enemylist=pygame.sprite.Group()
enemylist.add(Enemystart(100,100))
player=Player(600,200)
enemylist.add(player)

while running: #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        player_move(player,platformlist)
        player_move(player,platformlist)
    
    screen.fill("white")
    # --render objects here--
    platformlist.draw(screen)
    enemylist.draw(screen)
    for enemy in enemylist:
        if falling(enemy,platformlist) == True and not enemy.jumping: #and enemy.jumping == False:
            enemy.rect.center = (enemy.rect.centerx,enemy.rect.centery+5)
        if enemy == player and falling(enemy,platformlist) != False: # Resets jump count once landed (Not working)
          
          enemy.jumps=0
        else:
            if enemy != player:
                enemy.move(1,0)
        if enemy.rect.centery> 700:
          enemy.rect.center = random.choice([(100,100),(600,200)])
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
