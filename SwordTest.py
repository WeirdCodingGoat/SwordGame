import pygame, sys, random, math

def slash(sword,objects):
    sword.swing = True
    pass


def falling(sprite,obsticles):
    falling = True

    for surface in obsticles: # iterates through all platforms
        # checks to see if a falling object is in range with a platform to be able to land on it.
        if surface.solid or surface.semisolid:
            if sprite.rect.bottom+5 >= (surface.rect.top) and sprite.rect.bottom-5 <= (surface.rect.top) and sprite.rect.right > (surface.rect.left) and sprite.rect.left < (surface.rect.right):
                    falling = False
                    sprite.rect.bottom = (surface.rect.top)
    return falling

def player_move(player,obsticles):
    #Input documentation: https://www.pygame.org/docs/ref/key.html
    if pygame.key.get_pressed()[pygame.K_a]==True and pygame.key.get_pressed()[pygame.K_d] == False:
        player.move(-3,0)
        oldmansword.side=42
    elif pygame.key.get_pressed()[pygame.K_d]==True and pygame.key.get_pressed()[pygame.K_a]==False:
        player.move(3,0)
        oldmansword.side=-42
        
   # if pygame.key.get_pressed()[pygame.K_w]==True:
    #  print(player.jumps)
     # if falling(player,platformlist) != True or player.jumps <1: #Checks if player has jumped 2 times consecuativly. ("or" mut be bugging it)
      #  player.jumps+=1
       # jump(player,obsticles)


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
        


class Enemystart(pygame.sprite.Sprite): # add two other functions in this class for different types of enemies and add health
    # attribute.

    def __init__(self,x,y,type):
        super(Enemystart,self).__init__()
        
        #if type == "zombie":
        self.hp=3
        self.image = pygame.Surface([50,50],pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (x,y))
        self.jumping=False #This is used to make sure a mob class doesn't jump in mid air (maybe more than twice).
        self.direction = random.choice([1,-1])
        self.name = type

    def move(self,deltax,deltay):
        #make a collision function (make logic in game loop)
        if self.rect.left < 0 or self. rect.right>1200:
            deltax *=-5
        self.rect.centerx = self.rect.centerx+deltax*self.direction
        #Create a jump function or make the logic here.


class Sword(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Sword,self).__init__()

        self.image = pygame.Surface([22,45],pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("blue")
        self.rect = self.image.get_rect(center = (x,y))
        self.frame=0
        self.swing=False
        self.hit=False
        self.side=30


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Player,self).__init__()

        self.cycle = ["1walk.png","3walk.png"]
        #self.image = pygame.image.load('background.png')
        self.image = pygame.Surface([46,60],pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("#ff42ba")
        self.rect = self.image.get_rect(center = (x,y))
        self.jumping=False
        self.jumps=0
        self.name = "player"
        self.frame=0
        self.hp=3
    
    def move(self,deltax,deltay):
        # Add an animation (Flip between frames each time the fucntion is called on or not)
        self.rect.centerx = deltax+self.rect.centerx
        if deltay:
            
            self.rect.centery = +self.rect.centery
            # If gravity interupts jump, hashtag the "and jump" part of the checking for falling.
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
#Enemy and player creation
enemylist=pygame.sprite.Group()
enemylist.add(Enemystart(100,100,"zombie"))
player=Player(600,200)
enemylist.add(player)
hit_list=[]
#Sword creation
oneswordgroup=pygame.sprite.Group()
oldmansword=Sword(400,300)
oneswordgroup.add(oldmansword)
# Loading resources https://www.pygame.org/docs/tut/ChimpLineByLine.html?highlight=background
# Putting it all together https://www.pygame.org/docs/tut/MoveIt.html?highlight=animation
background = pygame.image.load('background.png')
size = background.get_size()
size = (size[0] * 1 , size[1] * 1) # Size modifier for image.
background = pygame.transform.scale(background, size) #Find the window size and devide the background image by it. x/x2 y/y2
background=background.convert()
score=0

while running: #Game loop
    for event in pygame.event.get():
        #Event documentation: https://www.pygame.org/docs/ref/key.html
        #https://www.pygame.org/docs/ref/event.html?highlight=event#module-pygame.event
         #https://www.geeksforgeeks.org/how-to-get-keyboard-input-in-pygame/ (event.key)
        if event.type == pygame.QUIT:
            running = False

    
        player_move(player,platformlist) # Jittery movment could be stopped if movement was done by the frame. This goes to fallimg too.
        player_move(player,platformlist)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                                         # add specify key and continue to test. (maybe put sword further away) -Done, though experiminiting would be fun.
                slash(oldmansword,enemylist)

    
    screen.blit(background, (0, 0))
    # --render objects here--
    if pygame.font:
        font = pygame.font.Font(None, 32)
        text = font.render(str(score), True, ("white"))
        textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
        screen.blit(text, textpos)

    platformlist.draw(screen)  # Rendering should be put into a function for readability in loop and ease of change.
    enemylist.draw(screen)

    if oldmansword.swing:
        oldmansword.rect.centerx = player.rect.centerx-oldmansword.side
        oldmansword.rect.centery = player.rect.centery
        oneswordgroup.draw(screen)
        oldmansword.frame+=1
        

        print(oldmansword.frame)
        
        if oldmansword.hit == False:
            for enemy in enemylist:
                if enemy != player:
                # https://www.pygame.org/docs/ref/sprite.html?highlight=collide#pygame.sprite.groupcollide

                    if pygame.sprite.collide_rect(oldmansword, enemy):
                        enemy.hp-=1
                        oldmansword.hit = True
                        enemy.image = pygame.Surface([50,50],pygame.SRCALPHA,32)
                        enemy.image.convert_alpha()
                        enemy.image.fill("blue")
                        hit_list.append(enemy)
                        if enemy.hp <1:    # Create enemies and append them to a list after all die.
                            enemy.kill()
                            score+=10
        if oldmansword.frame==30:
            oldmansword.swing = False
            oldmansword.hit=False
            oldmansword.frame=0
            for enemy in hit_list:
                enemy.image = pygame.Surface([50,50],pygame.SRCALPHA,32)
                enemy.image.convert_alpha()
                enemy.image.fill("red")
                hit_list=[]

        
        
    
    for enemy in enemylist:
        if falling(enemy,platformlist) == True and not enemy.jumping: #and enemy.jumping == False:
            enemy.rect.center = (enemy.rect.centerx,enemy.rect.centery+5)


        if enemy == player and falling(enemy,platformlist) != False: # Resets jump count once landed (Not working) mabye change the "!" to "="?
          # Also check for where it cares about the jumps.
          enemy.jumps=0
        else:
            if enemy != player:
                enemy.move(1,0)
        if enemy.rect.centery> 700:
          enemy.rect.center = random.choice([(100,100),(600,200)])
        if enemy != player:
            if player.frame==30: 
                if pygame.sprite.collide_rect(player, enemy):
                    player.hp-=1
                    if player.rect.centerx <= enemy.rect.centerx:
                        player.rect.centerx-=40
                        oldmansword.side=42
                    else:
                        player.rect.centerx+=40
                        oldmansword.side=42
                                    #   Set up Player invinsability timer!!!
                        #   oldmansword.swing = False
                        #  oldmansword.hit=False
                        #  oldmansword.frame=0
                    if player.hp <1:
                        print(player.hp)
                        player.jumping=True
                    player.frame=0
                    player.jumps=1
        if player.jumps==1 and player.frame<29:
            player.frame+=1
        else:
            player.jumps=0
            



    pygame.display.flip()

    clock.tick(60)

pygame.quit()
