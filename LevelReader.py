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

def load_level(selected):
    with open("level_maps.txt") as level:
        levels = level.read()
    header=(selected*20)+1
    print(levels)
    level.close()
    level=[[]]
    print(levels)
    for spot in levels:
        print(spot,levels.find(spot))
        if len(level[-1]) == 40:
            level.append([spot])
        else:
            level[-1].append(spot)
        
    print(level)
    platforms=[]
    platform=[]
    cordinates=[]
    check=1

    for row in range(header,header+20): # add a start and a stop (start:header) (stop=header+20)
        for character in range(40):
            print("row",row,"char",character)
            if len(cordinates) == 0 and level[row-1][character-1] == "-": 
                #bug might appear when program reads cordinates and adds more objects when reading 
                #a line with filler for a block.
                cordinates.append((character,row))


            elif len(cordinates) >0 and not level[row-1][character-1] == "-" and cordinates[-1]!="end":
                cordinates.append("end") # Maybe replace this with another flag/word?

        for land in platforms:
            for item in cordinates:  
                if item[0] >= land[0][0] and item[0] <= land[1][0] and item[1] >= land[0][1] and item[1] <= land[1][1]:
                    cordinates.pop(item)

        for cord in cordinates:
            if cord != "end":
                platform.append(cordinates.pop(cordinates.index(cord))) # Might need to make a condition where it 
                # makes sure that it's appending a full platform. Using the information provided
                # by checking each layer.

            else:
                for segment in platform: # Finding the lowest Y cord for platform.
                    check=1
                    while segment[1] + check != " ":
                        check+=1
                    if type(platforms[-1]) == type(1): #should result in null if none in list.
                        if check < platforms[-1]:
                            platforms[-1]=check # Might get an assignment error.
                    else:
                        platforms.append(check) # check this odd
                platforms.append([platform[0],(platform[-1][0],platforms.pop(check))])
                platform=[]
        # look in platforms to not make duplicates (use inequalities), 
        # Append cordinates to "platform" down to the bottom of the platform,
        # Take the first and the last cordinates and append them to platforms as [(x1,y1),(x2,y2)]
        # enemy format = "["Enemy type",(x,y)]" 
        cordinates=[]
    print(platforms)

load_level(0)
