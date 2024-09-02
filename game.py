"""Module containing all in-game functionality."""

#Imported Modules
import pygame
import os
import random
pygame.init()

#Constants
sw = 1000
sh = 500
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 27
anbus = []
score = 0

#Custom events
S_HIT = pygame.USEREVENT+1
A_HIT = pygame.USEREVENT+2

#loading all images for animations

R_RUN = [pygame.image.load(os.path.join('images','run1.png')),
     pygame.image.load(os.path.join('images','run2.png')),
     pygame.image.load(os.path.join('images','run3.png'))]

L_RUN = [pygame.transform.flip(pygame.image.load(os.path.join('images','run1.png')),True,False),
     pygame.transform.flip(pygame.image.load(os.path.join('images','run2.png')),True,False),
     pygame.transform.flip(pygame.image.load(os.path.join('images','run3.png')),True,False)]

JUMP = pygame.image.load(os.path.join('images','land.png'))

STAND = [pygame.image.load(os.path.join('images','stand1.png')),
       pygame.image.load(os.path.join('images','stand2.png')),
       pygame.image.load(os.path.join('images','stand3.png'))]

J_ATTACK = [pygame.image.load(os.path.join('images','jumpattack1.png')),
          pygame.image.load(os.path.join('images','jumpattack2.png')),
          pygame.image.load(os.path.join('images','jumpattack3.png')),
          pygame.image.load(os.path.join('images','jumpattack4.png')),
          pygame.image.load(os.path.join('images','jumpattack5.png'))]

CHIDORI = [pygame.image.load(os.path.join('images','chidori1.png')),
         pygame.image.load(os.path.join('images','chidori2.png')),
         pygame.image.load(os.path.join('images','chidori3.png')),
         pygame.image.load(os.path.join('images','chidori4.png')),
         pygame.image.load(os.path.join('images','chidori5.png')),
         pygame.image.load(os.path.join('images','chidori6.png')),
         pygame.image.load(os.path.join('images','chidori7.png')),
         pygame.image.load(os.path.join('images','chidori8.png')),
         pygame.image.load(os.path.join('images','chidori9.png')),
         pygame.image.load(os.path.join('images','chidori10.png')),
         pygame.image.load(os.path.join('images','chidori11.png')),
         pygame.image.load(os.path.join('images','chidori12.png')),
         pygame.image.load(os.path.join('images','chidori13.png')),
         pygame.image.load(os.path.join('images','chidori14.png')),
         pygame.image.load(os.path.join('images','chidori15.png')),
         pygame.image.load(os.path.join('images','chidori16.png')),
         pygame.image.load(os.path.join('images','chidori17.png')),
         pygame.image.load(os.path.join('images','chidori18.png')),
         pygame.image.load(os.path.join('images','chidori19.png')),
         pygame.image.load(os.path.join('images','chidori20.png')),
         pygame.image.load(os.path.join('images','chidori21.png'))]

C_TOUSEN = [pygame.image.load(os.path.join('images','chidoritousen1.png')),
          pygame.image.load(os.path.join('images','chidoritousen2.png')),
          pygame.image.load(os.path.join('images','chidoritousen3.png')),
          pygame.image.load(os.path.join('images','chidoritousen4.png')),
          pygame.image.load(os.path.join('images','chidoritousen5.png'))]

SNAKE_FIST = [pygame.image.load(os.path.join('images','snakefist1.png')),
            pygame.image.load(os.path.join('images','snakefist2.png')),
            pygame.image.load(os.path.join('images','snakefist3.png')),
            pygame.image.load(os.path.join('images','snakefist4.png')),
            pygame.image.load(os.path.join('images','snakefist5.png')),
            pygame.image.load(os.path.join('images','snakefist6.png'))]

HAND_SIGN = [pygame.image.load(os.path.join('images','handsigns1.png')),
           pygame.image.load(os.path.join('images','handsigns2.png')),
           pygame.image.load(os.path.join('images','handsigns3.png')),
           pygame.image.load(os.path.join('images','handsigns4.png'))]

KICK = [pygame.image.load(os.path.join('images','kick1.png')),
      pygame.image.load(os.path.join('images','kick2.png')),
      pygame.image.load(os.path.join('images','kick3.png')),
      pygame.image.load(os.path.join('images','kick4.png'))]

SWORD = [pygame.image.load(os.path.join('images','sword1.png')),
       pygame.image.load(os.path.join('images','sword3.png')),
       pygame.image.load(os.path.join('images','sword4.png')),
       pygame.image.load(os.path.join('images','sword5.png')),
       pygame.image.load(os.path.join('images','sword6.png')),
       pygame.image.load(os.path.join('images','sword7.png')),
       pygame.image.load(os.path.join('images','sword8.png')),
       pygame.image.load(os.path.join('images','sword9.png')),
       pygame.image.load(os.path.join('images','sword10.png')),
       pygame.image.load(os.path.join('images','sword11.png')),
       pygame.image.load(os.path.join('images','sword12.png')),
       pygame.image.load(os.path.join('images','sword13.png')),
       pygame.image.load(os.path.join('images','sword14.png')),
       pygame.image.load(os.path.join('images','sword15.png')),
       pygame.image.load(os.path.join('images','sword16.png')),
       pygame.image.load(os.path.join('images','sword17.png'))]

E_RUN = [pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join('images','erun1.png')),True,False),(80,122)),
       pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join('images','erun2.png')),True,False),(80,122)),
       pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join('images','erun3.png')),True,False),(80,122)),
       pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join('images','erun4.png')),True,False),(80,122))]

E_SWORD=[pygame.transform.flip(pygame.image.load(os.path.join('images','esword1.png')),True,False),
         pygame.transform.flip(pygame.image.load(os.path.join('images','esword2.png')),True,False),
         pygame.transform.flip(pygame.image.load(os.path.join('images','esword3.png')),True,False),
         pygame.transform.flip(pygame.image.load(os.path.join('images','esword4.png')),True,False)]

bg = pygame.transform.scale(pygame.image.load(os.path.join('images','45908.jpg')),(sw,sh))
shuriken_img = pygame.transform.scale(pygame.image.load(os.path.join('images','shuriken.png')),(20,20))

#loading fonts
HEALTH_FONT = pygame.font.SysFont('comic sans',40)
LOSE_FONT = pygame.font.SysFont('comic sans',80)
SCORE_FONT = pygame.font.SysFont('comic sans',40)
CHAKRA_FONT = pygame.font.SysFont('comic sans',40)

#loading sounds
BG_TRACK = pygame.mixer.Sound(os.path.join('sounds','raidenf.mp3'))
hit = pygame.mixer.Sound(os.path.join('sounds','hit.mp3'))
lose = pygame.mixer.Sound(os.path.join('sounds','naruto-trap.mp3'))

#main screen and caption
win = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("SASUKE RUN!")

#Classes

#class for main character
class player():
    
    #default values
    def __init__(self):
        self.x = 100
        self.y = 350
        self.vel = 10
        self.dash = 0
        self.dmg = 0
        self.width = 90
        self.height = 132
        self.health = 5
        self.isMove = False
        self.isJump = False
        self.isChakra = False
        self.chakra = 0
        self.chidori = False
        self.c_tousen = False
        self.damage = False
        self.j_attack = False
        self.snake_fist = False
        self.sword = False
        self.kick = False
        self.moveCount = 0
        self.isStand = True
        self.jumpCount = 9
        self.walkCount = 0
        self.standCount = 0
        self.left = False
        self.right = False
        self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
        
    #drawing animations
    def draw_sasuke(self,win):
            self.dmg = 0
            if self.walkCount + 1 >= 9:
                self.walkCount = 0
            
            if self.standCount + 1 >= 9:
                self.standCount = 0
    
            if not(self.isStand) and not self.isMove:
                if self.left:
                    win.blit(L_RUN[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(R_RUN[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
                elif self.isJump:
                    if self.isJump:
                        win.blit(JUMP,(self.x,self.y))
            
            elif self.isStand and not self.isMove:
                win.blit(STAND[self.standCount//9],(self.x,self.y))
                self.standCount+=1
            self.hitbox=pygame.Rect(self.x,self.y,self.width,self.height)
        
    #drawing special moves
    def drawMoves(self,win):      
        
        #sword attacks
        if self.sword:
            self.hitbox = pygame.Rect(self.x,self.y,self.width+15,self.height)
            self.dmg = 1
            if self.moveCount+1 >= 48:
                self.moveCount = 0
                self.chakra -= 2
                self.sword = False
                self.isMove = False
            self.left = self.right = self.isStand = False
            win.blit(SWORD[self.moveCount//3],(self.x,self.y))
            self.moveCount += 1
        
        #kick
        if self.kick:
            self.hitbox=pygame.Rect(self.x,self.y,self.width+5,self.height+5)
            self.dmg=1
            if self.moveCount+1>=9:
                self.moveCount=0
                self.kick=False
                self.isMove=False
            self.left=self.right=self.isStand=False
            win.blit(KICK[self.moveCount//3],(self.x,self.y))
            self.moveCount+=1
        
       #charging chakra
        if self.isChakra:
            self.dmg = 0
            if self.moveCount+1 >= 12:
                self.moveCount = 0
            self.left = self.right = self.isStand = False
            win.blit(HAND_SIGN[self.moveCount//3],(self.x,self.y))
            self.moveCount += 1
        self.isChakra = False
        
        #chidori
        if self.chidori:
            if self.moveCount > 40:
                self.dmg = 5
            if self.moveCount+1 >= 84:
                self.moveCount = 0
                self.chakra -= 15
                self.chidori = False
                self.isMove = False
            self.left = self.right = self.isStand = False
            win.blit(CHIDORI[self.moveCount//4],(self.x,self.y))
            self.moveCount += 1
            if self.moveCount > 44:
                self.x += 4
        
        #snake fist
        if self.snake_fist:
            self.hitbox = pygame.Rect(self.x,self.y,self.width+10,self.height)
            self.dmg = 3
            if self.moveCount+1 >= 24:
                self.moveCount = 0
                self.chakra -= 5
                self.snake_fist = False
                self.isMove = False
            self.left = self.right = self.isStand = False
            win.blit(SNAKE_FIST[self.moveCount//4],(self.x,self.y))
            self.moveCount += 1
        
        #chidori tousen 
        if self.c_tousen:
            self.hitbox = pygame.Rect(self.x,self.y,sw,self.height-10)
            self.dmg = 1
            if self.moveCount+1 >= 20:
                self.moveCount = 0
                self.chakra -= 10
                self.c_tousen = False
                self.isMove = False
            self.left = self.right = self.isStand = False
            win.blit(C_TOUSEN[self.moveCount//4],(self.x,self.y))
            self.moveCount += 1
        
#class for enemies
class anbu():
    
    def __init__(self):
        self.x = sw
        self.y = 350
        self.vel = 10
        self.dmg = 1
        self.width = 90
        self.height = 132
        self.health = 1
        self.isMove = False
        self.sword = False
        self.kick = False
        self.moveCount = 0
        self.walkCount = 0
        self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
        
    def moves(self,SASUKE,win):

        #checking whether enemy is near player or not
        if (self.x-40) > SASUKE.x or (self.x-40) < SASUKE.x:
            self.x -= self.vel    
            if self.walkCount >= 7:
                self.walkCount = 0
            win.blit(E_RUN[self.walkCount//4],(self.x,self.y))
            self.walkCount += 1
        
        elif (self.x-40) == SASUKE.x:
            if self.moveCount < 6:
                self.y = 284
            elif 6<self.moveCount < 18:
                self.y = 317
            if self.moveCount >= 23:
                self.moveCount = 0
            win.blit(E_SWORD[self.moveCount//6],(self.x,self.y))
            self.moveCount += 1
            self.hitbox = pygame.Rect(self.x,self.y,self.width+40,self.height)
        self.y = 350
            
#class for projectiles
class projectile():
    
    def __init__(self):
        self.x = sw
        self.y = random.randint(250,400)
        self.vel = 6+(score//27)
        self.width = 20
        self.height = 20
        self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
        
    def draw(self,win):
        win.blit(shuriken_img,(self.x,self.y))
        self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
        
#Functions

#handles movement and collision of projectiles
def handle_shuriken(shurikens,SASUKE):
    for shuriken in shurikens:
        shuriken.x -= shuriken.vel
        
        #checking for collisions
        if (SASUKE.hitbox).colliderect(shuriken.hitbox):
            pygame.event.post(pygame.event.Event(S_HIT))
            hit_shuriken=shurikens.index(shuriken)
            shurikens.remove(shuriken)
            
        #deleting shurikens that go out of the visible screen 
        elif shuriken.x == 0:
            shurikens.remove(shuriken)
            
#handles movement and collision of enemies
def handle_anbu(anbus,SASUKE):
    
    global score
    
    #collisions
    for anbu in anbus:
        if (SASUKE.hitbox).colliderect(anbu.hitbox):
            pygame.event.post(pygame.event.Event(A_HIT))
            if SASUKE.dmg > 0:
                anbu.health -= SASUKE.dmg
                hit.play()
            elif SASUKE.dmg < 1:
                if anbu.moveCount == 20:
                    SASUKE.health -= anbu.dmg
                    hit.play()

        elif anbu.x == 0:
            anbus.remove(anbu)
            
        #if anbus dies
        if anbu.health == 0:
            score += 15
            hit_anbu = anbus.index(anbu)
            anbus.remove(anbu)
    
#controls game exit sequence
def GameOver(win,text):
    
    draw_lose = LOSE_FONT.render(text,1,BLACK)
    win.blit(draw_lose,(sw//2-draw_lose.get_width()//2,sh//2-draw_lose.get_height()//2))
    lose.play()
    pygame.display.update()
    pygame.time.delay(10000)
    
#handles drawing on the main screen
def draw_window(win,SASUKE,shurikens,anbus):
    
    win.blit(bg,(0,0))
    SASUKE.draw_sasuke(win)
    SASUKE.drawMoves(win)
    SASUKE_HEALTH_TEXT = HEALTH_FONT.render('HEALTH : '+str(SASUKE.health),1,BLACK)
    SASUKE_CHAKRA_TEXT = HEALTH_FONT.render('CHAKRA : '+str(SASUKE.chakra//1),1,BLACK)
    draw_score = SCORE_FONT.render('SCORE : '+str(score//1),1,BLACK)
    
    win.blit(SASUKE_HEALTH_TEXT,(sw-SASUKE_HEALTH_TEXT.get_width()-60,10))
    win.blit(SASUKE_CHAKRA_TEXT,(sw-SASUKE_HEALTH_TEXT.get_width()-60,15+SASUKE_HEALTH_TEXT.get_height()))
    win.blit(draw_score,(10,10))
    
    for shuriken in shurikens:
        shuriken.draw(win)
    
    for anbu in anbus:
        anbu.moves(SASUKE,win)    
        
    pygame.display.update()
    
#main game loop
def main(acc = 6):
    
    global score,spawnCount
    run = True
    fin = False
    spawnCount1 = 0
    spawnCount2 = 0
    clock=pygame.time.Clock()
    shurikens = []
    anbus = []
    hit_shuriken = 0
    SASUKE = player()
    BG_TRACK.play()
    
    #game loop
    while run:
        clock.tick(FPS)
        
        #checking for events
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            #player collision
            if event.type == S_HIT:
                if SASUKE.dmg == 0:
                    hit.play()
                    SASUKE.health -= 1
                else:
                    for shuriken in shurikens:
                        shurikens.pop(hit_shuriken)
                        score += 5
        
        #keyboard inputs
        
        keys = pygame.key.get_pressed()
        
        #move right
        if keys[pygame.K_d] and SASUKE.x+SASUKE.vel+SASUKE.width<sw:
            SASUKE.x += SASUKE.vel
            SASUKE.right = True   
            SASUKE.left = False
            SASUKE.isStand = False             
        
        #move left
        elif keys[pygame.K_a] and SASUKE.x>0:
            SASUKE.x -= SASUKE.vel
            SASUKE.left = True
            SASUKE.right = False
            SASUKE.isStand = False
            
        #kick
        elif keys[pygame.K_e]:
            SASUKE.kick = True
            SASUKE.isMove = True
            
        #sword
        elif keys[pygame.K_q]:
            SASUKE.sword = True
            SASUKE.isMove = True
            
        #charge chakra
        elif keys[pygame.K_s]:
            SASUKE.isChakra = True
            SASUKE.chakra += 1/13
            
        #chidori
        elif keys[pygame.K_c] and SASUKE.chakra>14:
            SASUKE.isMove = SASUKE.chidori = True
            
        #chidori tousen
        elif keys[pygame.K_v] and SASUKE.chakra>10:
            SASUKE.isMove = SASUKE.c_tousen = True
            
        #snake fist
        elif keys[pygame.K_b] and SASUKE.chakra>5:
            SASUKE.isMove = SASUKE.snake_fist = True
            
        else:
            SASUKE.isStand = True
            SASUKE.walkCount = 0

        #player jump
        if not SASUKE.isJump:
            if keys[pygame.K_SPACE] and not SASUKE.isMove:
                SASUKE.isJump = True
                SASUKE.isStand = False
                SASUKE.width = SASUKE.height = 90
                SASUKE.left = SASUKE.right = False
                SASUKE.standCount = SASUKE.runCount = 0
                
        else:
            SASUKE.left = SASUKE.right = False
            if SASUKE.jumpCount >= -9:
                neg = 1
                if SASUKE.jumpCount < 0:
                    neg =- 1
                SASUKE.y -= (SASUKE.jumpCount**2)*0.5*neg
                SASUKE.jumpCount -= 1
            else:
                SASUKE.isJump = False
                SASUKE.jumpCount = 9
                SASUKE.isStand = True
              
        #spawning projectiles
        if spawnCount1 // (27*random.randint(2,4)) == 1:
            spawnCount1 = 0
            shurikens.append(projectile())
        
        #spawning enemies
        if score > 300:
            if spawnCount2 // (27*random.randint(2,4))== 1:
                spawnCount2 = 0
                anbus.append(anbu())
            spawnCount2 += 1
            
        #checking player health 
        if SASUKE.health == 0:
            BG_TRACK.stop()
            GameOver(win,"YOU LOSE!")
            score = 0
            fin = True
            
            #back to starting screen
            import menu
            break
            
        score+=1/(27/4)
        spawnCount1+=1
    
        handle_shuriken(shurikens,SASUKE)
        handle_anbu(anbus,SASUKE)
        draw_window(win,SASUKE,shurikens,anbus)
    
