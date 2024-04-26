import pygame, math

# player size= x42,y60 (y600/30) (x800/23) (for scalling levels from ASCII layout) 
# file reading https://www.w3schools.com/python/python_file_open.asp

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super(Platform,self).__init__()
        self.image = pygame.Surface((width,height))
        adjust=(math.sqrt((width)^2+(height)^2))
        self.image.convert_alpha()
        self.image.fill("brown")
        self.rect = self.image.get_rect(center = (x+adjust,y+adjust))
        self.solid = True
        self.semisolid = True

def load_level(level):
    levels=open("level_maps.txt","r")
    header=(level*20)+1
    platforms=[]
    platform=[]
    cordinates=[]

    for row in 20:
        for character in 40:
            if len(cordinates) == 0 and levels.readline(row)(character) == "-": 
                #bug might appear when program reads cordinates and adds more objects when reading 
                #a line with filler for a block.
                cordinates.append((character,row))
            elif len(cordinates) >0 and not levels.readline(row)(character) == "-":
                cordinates.append("end") # Maybe replace this with another flag/word?


        # look in platforms to not make duplicates (use inequalities), 
        # Append cordinates to "platform" down to the bottom of the platform,
        # Take the first and the last cordinates and append them to platforms as [(x1,y1),(x2,y2)]
        # enemy format = "["Enemy type",(x,y)]" 
            
        platforms.append(cordinates)
        cordinates=[]

