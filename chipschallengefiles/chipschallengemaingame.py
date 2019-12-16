import pygame, random, sys
from pygame.locals import *
from pygame.font import *
from pygame import *
from pygame.sprite import *
pygame.init()
#colors
blue = (0, 0, 255)
grey = (128, 128, 128)
white = (255, 255, 255)
brown = (139,69,19)
orange = (255,156,71)
black = (0, 0, 0)
transparent = (0, 0, 0, 0)
#tiles
wall = image.load('wall_block.jpg')
walk = image.load('walk_block.jpg')
goldkey = image.load('gold_key.png')
mcsprite = image.load('maincharacter.jpg')
hint = image.load('hint_block.png')
door = image.load('door_block.jpg')
fireext = image.load('extinguisher.png')
fire = image.load('fire.png')
finish = image.load('finalportal.png')
map = image.load('map.png')
finishinv = image.load('finishinv.png')
fireextinv = image.load('extinguisherinventory.png')
hinttext = image.load('hinttext.png')
enemy = image.load('ghost.png')
ice = image.load('ice.jpg')
spike = image.load('spike.png')
timefont = pygame.font.SysFont("monospace", 40)
blocksize = 142
playerstartylevel1 = 5
playerstartxlevel1 = 3
clock = time.Clock()
level1 = open('level1.txt')
level2 = open('level2.txt')
level1matrix = []
level2matrix = []
for line in level1:
    level1matrix.append(line.rstrip().split())
for line in level2:
    level2matrix.append(line.rstrip().split())
inventorymatrix = ['0']

display.set_caption('chippersons challenge')
screen = display.set_mode((1400, 994))
draw.rect(screen, orange, (0, 0, 994, 994))
draw.rect(screen, blue, (1000, 200, 400, 794))
draw.rect(screen, grey, (1050, 550, 300, 300))

pygame.display.update()

song1 =pygame.mixer.music.load('giornopiano.wav')
pygame.mixer.music.set_volume(.1)


pygame.mixer.music.play(-1, 0)

def main():
    pygame.mixer.music.set_volume(.1)
    enemyy = 26
    enemyx = 3
    enemyright = True
    firstlevel = True
    running = True
    haskey = False
    hasext = False
    count = 0
    inventorycount = 0
    startingx = 3
    startingy = 3
    spotcountx = 0
    spotcounty = 0
    iceloop = False
    xpos = playerstartxlevel1
    ypos = playerstartylevel1
    level2startx = 3
    level2starty = 5
    while running:

        while ((time.get_ticks() <= 240000)):
            if (firstlevel == True):

                draw.rect(screen, blue, (1000, 0, 400, 200))

                draw.line(screen, white, (1050, 650), (1350, 650), 1)
                draw.line(screen, white, (1050, 750), (1350, 750), 1)
                draw.line(screen, white, (1150, 550), (1150, 850), 1)
                draw.line(screen, white, (1250, 550), (1250, 850), 1)
                timer1 = time.get_ticks() / 1000
                labeltimer = timefont.render("Time: " + str(timer1), 1, white)
                screen.blit(labeltimer, (1070, 20))
                display.update()

                if count == 0:
                    drawboard(ypos, xpos)
                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                    display.update()
                    count = 1
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                        sys.exit()
                    elif event.type == KEYDOWN:
                        haskey = False
                        hasext = False

                        if event.key == K_w:
                            if(level1matrix[ypos-1][xpos] != '0'):
                                if (enemyx == 4):
                                    enemyright = True
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx+=1
                                elif (enemyx == 20):
                                    enemyright = False
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx-=1
                                elif(enemyx < 20 and enemyright == True and enemyx!=4):
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx+=1
                                elif(enemyx < 20 and enemyright == False and enemyx!=4):
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx-=1
                                if(level1matrix[ypos-1][xpos] == 'T' or 'K' ):
                                    inventory(level1matrix[ypos-1][xpos], ypos-1, xpos, inventorycount)
                                    inventorycount = len(inventorymatrix)-1
                                if (level1matrix[ypos - 1][xpos] == 'D'):
                                    check = 0
                                    while (haskey == False and check < inventorycount+1):
                                        if (inventorymatrix[check] == 'K'):
                                            ypos -= 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            haskey = True

                                            level1matrix[ypos][xpos] = 'R'
                                            inventorymatrix[check] = '0'

                                            if (check <= 3):
                                                screen.blit(finishinv, (1050 + ((check - 1) * 100), 550))
                                            if (check > 3 and check <= 6):
                                                screen.blit(finishinv, (1050 + ((check - 4) * 100), 650))
                                            if (check > 6):
                                                screen.blit(finishinv, (1050 + ((check - 7) * 100), 750))
                                            pygame.display.update()
                                        check += 1
                                if (level1matrix[ypos-1][xpos] == 'F'):
                                    check = 0
                                    while (hasext == False and check<inventorycount+1):
                                        if(inventorymatrix[check] == 'T'):
                                            ypos -= 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            hasext = True
                                            level1matrix[ypos][xpos] = 'R'
                                            pygame.display.update()
                                        check += 1
                                elif (level1matrix[ypos - 1][xpos] != 'D'):
                                    ypos -= 1
                                    drawboard(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()
                                pygame.display.update()
                        if event.key == K_s:
                            if(level1matrix[ypos+1][xpos] != '0'):

                                if (enemyx == 4):
                                    enemyright = True
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx += 1
                                elif (enemyx == 20):
                                    enemyright = False
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx -= 1
                                elif (enemyx < 20 and enemyright == True):
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx += 1
                                elif (enemyx < 20 and enemyright == False):
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx -= 1
                                if (level1matrix[ypos + 1][xpos] == 'T' or 'K' or 'M'):
                                    inventory(level1matrix[ypos + 1][xpos], ypos+1, xpos, inventorycount)
                                    inventorycount = len(inventorymatrix)-1
                                if (level1matrix[ypos+1][xpos] == 'D' ):
                                    check = 0
                                    while(haskey == False and check<inventorycount+1):
                                        if (inventorymatrix[check] == 'K'):
                                            ypos += 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            haskey = True
                                            level1matrix[ypos][xpos] = 'R'
                                            inventorymatrix[check] = '0'

                                            if (check <= 3):
                                                screen.blit(finishinv, (1050 + ((check - 1) * 100), 550))
                                            if (check > 3 and check <= 6):
                                                screen.blit(finishinv, (1050 + ((check - 4) * 100), 650))
                                            if (check > 6):
                                                screen.blit(finishinv, (1050 + ((check - 7) * 100), 750))

                                            pygame.display.update()
                                        check += 1
                                if (level1matrix[ypos + 1][xpos] == 'F'):
                                    check = 0
                                    while (hasext == False and check<inventorycount+1):
                                        if(inventorymatrix[check] == 'T'):
                                            ypos+= 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            hasext = True
                                            level1matrix[ypos][xpos] = 'R'
                                            pygame.display.update()

                                        check += 1
                                elif (level1matrix[ypos+1][xpos] != 'D'):
                                    ypos += 1
                                    drawboard(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()
                                pygame.display.update()
                        if event.key == K_a:
                            if(level1matrix[ypos][xpos-1] != '0'):

                                if (enemyx == 4):
                                    enemyright = True
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx += 1
                                elif (enemyx == 20):
                                    enemyright = False
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx -= 1
                                elif (enemyx < 20 and enemyright == True):
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx += 1
                                elif (enemyx < 20 and enemyright == False):
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx -= 1
                                if (level1matrix[ypos][xpos-1] == 'T' or 'K' or 'M'):
                                    inventory(level1matrix[ypos][xpos-1], ypos, xpos-1, inventorycount)
                                    inventorycount = len(inventorymatrix)-1
                                if (level1matrix[ypos][xpos-1] == 'D'):
                                    check = 0
                                    while (haskey == False and check < inventorycount+1):
                                        if (inventorymatrix[check] == 'K'):
                                            xpos -= 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            haskey = True
                                            level1matrix[ypos][xpos] = 'R'
                                            inventorymatrix[check] = '0'

                                            if (check <= 3):
                                                screen.blit(finishinv, (1050 + ((check - 1) * 100), 550))
                                            if (check > 3 and check <= 6):
                                                screen.blit(finishinv, (1050 + ((check - 4) * 100), 650))
                                            if (check > 6):
                                                screen.blit(finishinv, (1050 + ((check - 7) * 100), 750))

                                            pygame.display.update()
                                        check += 1
                                if (level1matrix[ypos][xpos - 1] == 'F'):
                                    check = 0
                                    while (hasext == False and check < inventorycount + 1):
                                        if (inventorymatrix[check] == 'T'):
                                            xpos -= 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            hasext = True
                                            level1matrix[ypos][xpos] = 'R'
                                            pygame.display.update()

                                        check += 1
                                elif (level1matrix[ypos][xpos-1] != 'D'):
                                    xpos -= 1
                                    drawboard(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()
                                pygame.display.update()
                        if event.key == K_d:
                            if(level1matrix[ypos][xpos+1] != '0'):

                                if (enemyx == 4):
                                    enemyright = True
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx += 1
                                elif (enemyx == 20):
                                    enemyright = False
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx -= 1
                                elif (enemyx < 20 and enemyright == True):
                                    moveenemy(enemyy, enemyx, True)
                                    enemyx += 1
                                elif (enemyx < 20 and enemyright == False):
                                    moveenemy(enemyy, enemyx, False)
                                    enemyx -= 1
                                if (level1matrix[ypos][xpos + 1] == 'T' or 'K' or 'M'):
                                    inventory(level1matrix[ypos][xpos + 1], ypos, xpos+1, inventorycount)
                                    inventorycount = len(inventorymatrix)-1
                                if (level1matrix[ypos][xpos+1] == 'D'):
                                    check = 0
                                    while (haskey == False and check < inventorycount+1):
                                        if (inventorymatrix[check] == 'K'):
                                            xpos += 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            haskey = True
                                            level1matrix[ypos][xpos] = 'R'
                                            inventorymatrix[check] = '0'

                                            if (check <= 3):
                                                screen.blit(finishinv, (1050 + ((check - 1) * 100), 550))
                                            if (check > 3 and check <= 6):
                                                screen.blit(finishinv, (1050 + ((check - 4) * 100), 650))
                                            if (check > 6):
                                                screen.blit(finishinv, (1050 + ((check - 7) * 100), 750))

                                            pygame.display.update()
                                        check += 1
                                if (level1matrix[ypos][xpos + 1] == 'F'):
                                    check = 0
                                    while (hasext == False and check<inventorycount+1):
                                        if(inventorymatrix[check] == 'T'):
                                            xpos+= 1
                                            drawboard(ypos, xpos)
                                            drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                            hasext = True
                                            level1matrix[ypos][xpos] = 'R'
                                            pygame.display.update()

                                        check += 1
                                elif (level1matrix[ypos][xpos+1] != 'D' or 'F'):
                                    xpos += 1
                                    drawboard(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()
                                pygame.display.update()
                        if (level1matrix[ypos][xpos] == 'H'):
                            screen.blit(hinttext, (300, 200))
                        if (level1matrix[ypos][xpos]=='X'):
                            firstlevel = False
                            count = 0
                            ypos = level2starty
                            xpos = level2starty
                        pygame.display.update()
            elif(firstlevel == False):
                draw.rect(screen, blue, (1000, 0, 400, 200))

                draw.line(screen, white, (1050, 650), (1350, 650), 1)
                draw.line(screen, white, (1050, 750), (1350, 750), 1)
                draw.line(screen, white, (1150, 550), (1150, 850), 1)
                draw.line(screen, white, (1250, 550), (1250, 850), 1)
                timer1 = time.get_ticks() / 1000
                labeltimer = timefont.render("Time: " + str(timer1), 1, white)
                screen.blit(labeltimer, (1070, 20))
                display.update()
                if count == 0:
                    drawboard2(ypos, xpos)
                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                    display.update()
                    count = 1
                for event in pygame.event.get():
                    move = 0
                    if event.type == QUIT:
                        running = False
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_w:
                            if(level2matrix[ypos-1][xpos] != '0'):
                                if (level2matrix[ypos-1][xpos] == 'R'):
                                    ypos -= 1
                                    drawboard2(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()

                                if (level2matrix[ypos-1][xpos] == 'I'):
                                    if (level2matrix[ypos - 1][xpos] == 'I' or 'S'):
                                        iceloop = True
                                    while (iceloop == True):
                                        ypos -= 1
                                        drawboard2(ypos, xpos)
                                        drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                        pygame.display.update()

                                        if (level2matrix[ypos][xpos] == 'R'):
                                            iceloop = False
                                    move = 1
                            if (level2matrix[ypos][xpos] == 'X'):
                                haswon()
                            pygame.display.update()
                        if event.key == K_a:
                            if(level2matrix[ypos][xpos-1] != '0'):
                                if(level2matrix[ypos][xpos-1] == 'R'):

                                    xpos -= 1
                                    drawboard2(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()

                                elif(level2matrix[ypos][xpos-1] == 'I'):
                                    if (level2matrix[ypos][xpos - 1] == 'I' or 'S'):
                                        iceloop = True
                                    while (iceloop == True):

                                        xpos -= 1
                                        drawboard2(ypos, xpos)
                                        drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                        pygame.display.update()

                                        if (level2matrix[ypos][xpos] == 'R'):
                                            iceloop = False
                                    move = 1
                            if (level2matrix[ypos][xpos] == 'X'):
                                haswon()
                            pygame.display.update()
                        if event.key == K_s:

                            if(level2matrix[ypos+1][xpos] != '0'):

                                if(level2matrix[ypos+1][xpos] == 'I'):
                                    if (level2matrix[ypos+1][xpos] == 'I' or 'S'):
                                        iceloop = True
                                    while (iceloop == True):
                                        ypos += 1
                                        drawboard2(ypos, xpos)
                                        drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                        pygame.display.update()

                                        if (level2matrix[ypos][xpos] == 'R'):

                                            iceloop = False
                                elif (level2matrix[ypos+1][xpos] != 'S'):
                                    ypos += 1
                                    drawboard2(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()

                            if (level2matrix[ypos][xpos] == 'X'):
                                haswon()

                                pygame.display.update()
                        if event.key == K_d:

                            if(level2matrix[ypos][xpos+1] != '0'):
                                if(level2matrix[ypos][xpos+1] == 'R'):
                                    xpos += 1
                                    drawboard2(ypos, xpos)
                                    drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                    pygame.display.update()

                                elif (level2matrix[ypos][xpos + 1] == 'I'):
                                    if(level2matrix[ypos][xpos + 1] == 'I' or 'S'):
                                        iceloop = True
                                    while (iceloop == True):
                                        xpos += 1
                                        drawboard2(ypos, xpos)
                                        drawboy(startingy, startingx, ypos, xpos, firstlevel)
                                        pygame.display.update()

                                        if(level2matrix[ypos][xpos] == 'R'):
                                            iceloop = False

                            if (level2matrix[ypos][xpos] == 'X'):
                                haswon()
                            pygame.display.update()
                        if(level2matrix[ypos][xpos]=='X'):
                            haswon()
        running = False
        endgame()
def haswon():
    screen.fill(black)
    score = time.get_ticks() / 1000
    labelloss = timefont.render('Congratulation! you win with a score of: ' + str((240-score))+ '!', 1, white)
    screen.blit(labelloss, (53, 400))
    display.update()
    time.wait(5000)
    sys.exit()
def endgame():
    screen.fill(black)
    score = time.get_ticks()/1000
    labelloss = timefont.render('You ran out of time :(', 1, white)
    screen.blit(labelloss, (400, 400))
    display.update()
    time.wait(5000)
    sys.exit()
def endgamedeath():
    screen.fill(black)
    score = time.get_ticks() / 1000
    labelloss = timefont.render('You got killed :(', 1, white)
    screen.blit(labelloss, (400, 400))
    display.update()
    time.wait(5000)
    sys.exit()
def drawboard(y, x):
    draw.rect(screen, blue, (1000, 0, 400, 200))
    timer1 = time.get_ticks() / 1000
    labeltimer = timefont.render("Time: " + str(timer1), 1, white)
    screen.blit(labeltimer, (1070, 20))
    display.update()
    drawing = True
    while drawing:
        countx = 0
        county = 0
        for i in range(y-3, y+4):
            draw.rect(screen, blue, (1000, 0, 400, 200))
            timer1 = time.get_ticks() / 1000
            labeltimer = timefont.render("Time: " + str(timer1), 1, white)
            screen.blit(labeltimer, (1070, 20))
            display.update()
            for j in range(x-3, x+4):
                draw.rect(screen, blue, (1000, 0, 400, 200))
                timer1 = time.get_ticks() / 1000
                labeltimer = timefont.render("Time: " + str(timer1), 1, white)
                screen.blit(labeltimer, (1070, 20))
                display.update()
                if level1matrix[i][j] == '0':
                    screen.blit(wall, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level1matrix[i][j] == 'K':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(goldkey, (countx*blocksize+41, county*blocksize+41))
                    pygame.display.update()
                if level1matrix[i][j] == 'R':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level1matrix[i][j] == 'H':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(hint, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level1matrix[i][j] == 'D':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(door, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level1matrix[i][j] == 'T':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(fireext, (countx * blocksize+33, county * blocksize))
                    pygame.display.update()
                if level1matrix[i][j] == 'F':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(fire, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level1matrix[i][j] == 'X':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(finish, (countx * blocksize, county * blocksize+26))
                    pygame.display.update()
                if level1matrix[i][j] == 'M':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(map, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level1matrix[i][j] == 'G':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(enemy, (countx * blocksize-70, county * blocksize))
                if level1matrix[i][j] == 'L':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                pygame.display.update()
                countx+=1
            countx = 0
            county+=1
        pygame.display.update()
        drawing = False
def drawboard2(y, x):
    drawing = True
    draw.rect(screen, blue, (1000, 0, 400, 200))
    timer1 = time.get_ticks() / 1000
    labeltimer = timefont.render("Time: " + str(timer1), 1, white)
    screen.blit(labeltimer, (1070, 20))
    display.update()
    while drawing:
        draw.rect(screen, blue, (1000, 0, 400, 200))
        timer1 = time.get_ticks() / 1000
        labeltimer = timefont.render("Time: " + str(timer1), 1, white)
        screen.blit(labeltimer, (1070, 20))
        display.update()
        countx = 0
        county = 0
        for i in range(y - 3, y + 4):
            draw.rect(screen, blue, (1000, 0, 400, 200))
            timer1 = time.get_ticks() / 1000
            labeltimer = timefont.render("Time: " + str(timer1), 1, white)
            screen.blit(labeltimer, (1070, 20))
            display.update()
            for j in range(x - 3, x + 4):
                draw.rect(screen, blue, (1000, 0, 400, 200))
                timer1 = time.get_ticks() / 1000
                labeltimer = timefont.render("Time: " + str(timer1), 1, white)
                screen.blit(labeltimer, (1070, 20))
                display.update()
                if level2matrix[i][j] == '0':
                    screen.blit(wall, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level2matrix[i][j] == 'R':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level2matrix[i][j] == 'X':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(finish, (countx * blocksize, county * blocksize+26))
                    pygame.display.update()
                if(level2matrix[i][j]== 'I'):
                    screen.blit(ice, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                if level2matrix[i][j] == 'S':
                    screen.blit(walk, (countx * blocksize, county * blocksize))
                    screen.blit(spike, (countx * blocksize, county * blocksize))
                    pygame.display.update()
                pygame.display.update()
                countx+=1
            countx = 0
            county+=1
        pygame.display.update()
        drawing = False

def moveenemy(y, x, right):
    if(right == True):
        level1matrix[y][x]='L'
        level1matrix[y][x+1]='G'
        level1matrix[y][x-1] = 'R'
    elif(right == False):
        level1matrix[y][x+1] = 'R'
        level1matrix[y][x]='L'
        level1matrix[y][x-1]='G'
    display.update()
def drawboy(y, x, cy, cx, level1):
    screen.blit(mcsprite, (x*blocksize+36, y*blocksize+3.5))
    draw.rect(screen, blue, (1000, 0, 400, 200))
    timer1 = time.get_ticks() / 1000
    labeltimer = timefont.render("Time: " + str(timer1), 1, white)
    screen.blit(labeltimer, (1070, 20))
    display.update()
    if (level2matrix[cy][cx] == 'S' and level1 == False):
        endgamedeath()
    if(level1matrix[cy][cx-1]=='G'and level1matrix[cy][cx]=='L'):
        endgamedeath()
    elif(level1matrix[cy][cx+1]=='G' and level1matrix[cy][cx]=='L'):
        endgamedeath()
    elif(level1matrix[cy][cx]=='G'):
        endgamedeath()

def inventory(tile, y, x, i):
    inventorystartx = 1050
    inventorystarty = 550
    boxsize = 100
    pygame.display.update()
    if tile== 'K':
        inventorymatrix.append('K')
        if(len(inventorymatrix)<=4):
            screen.blit(goldkey, (inventorystartx + (i * boxsize + 20), inventorystarty + 20))
        elif(len(inventorymatrix)<=7):
            screen.blit(goldkey, (inventorystartx+((i-3)*boxsize+20), inventorystarty+(1*boxsize+20)))
        elif(len(inventorymatrix)<=10):
            screen.blit(goldkey, (inventorystartx+((i-6)*boxsize+20), inventorystarty+(2*boxsize+20)))
        level1matrix[y][x] = 'R'
        pygame.display.update()
    if tile=='T':
        inventorymatrix.append('T')
        if (len(inventorymatrix) <= 4):
            screen.blit(fireextinv, (inventorystartx + (i * boxsize + 30), inventorystarty + 10))
        elif (len(inventorymatrix) <= 7):
            screen.blit(fireextinv, (inventorystartx + ((i-3) * boxsize + 30), inventorystarty + (1 * boxsize + 10)))
        elif (len(inventorymatrix) <= 10):
            screen.blit(fireextinv, (inventorystartx + ((i-6) * boxsize + 30), inventorystarty + (2 * boxsize + 10)))
        level1matrix[y][x] = 'R'
        pygame.display.update()
main()