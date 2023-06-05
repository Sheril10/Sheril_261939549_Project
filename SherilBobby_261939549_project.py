import pygame
import sys
import random
import time
pygame.font.init()



pygame.init()

width = 800
height = 600
window1= pygame.display.set_mode((width,height))
spaceship_icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(spaceship_icon)

bg=pygame.image.load("bg.jpg")

aestroid_icon=pygame.image.load("aestroid.png")
alien_icon=pygame.image.load("alien.png")
powerup_icon=pygame.image.load("powerup.png")
bonus_icon=pygame.image.load("bonus.png")
bullet_icon = pygame.image.load("bullet.png")
font= pygame.font.SysFont("times roman",40)

'''
class Enemy:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
class Aestroids(Enemy):
    def __init__(self,x,y):
        super().__init__(x,y)

class Aliens(Enemy):
    def __init__(self,x,y):
        super().__init__(x,y)


        


        
        

class Plus:
class Powerup:
class Bonus:
'''



class Life:
    lives = 5
    level = 1
    def lifedrop(self):
        if Life.lives>0:
            Life.lives = Life.lives - 1
    def lifeplus(self):
        Life.lives = 5
    def game_over():
        self.gameover = font.render("GAME OVER",1, (255,255,255))
        window1.blit(self.gameover, (340, 250))
                
class Player(Life):
    allscore = []
    def __init__(self):
        self.score = 0
        
    def scoring():
        self.score= self.score+1
        while collision:
            self.scoring()
        self.appendscore()
        self.set_score()
    def appendscore(self):
        Player.allscore.append(self.score)
    def gethighscore(self):
        return max(Player.allscore)
    def set_score(self):
        self.score=0
    def show_score(self):
        self.scoreb = font.render("Points: " + str(self.score),True, (255, 255, 255))
        window1.blit(self.scoreb ,(360,10)) 
    
class Spaceship(Player):
    spaceship = pygame.transform.smoothscale(spaceship_icon,(70,60))
    changex = 8
    def __init__(self,x=360,y=500):
        self.x = x
        self.y = y
        
    def moveleft(self):
        self.x = self.x - Spaceship.changex  
        return self.x
    def moveright(self):
        self.x = self.x + Spaceship.changex
    def moveup(self):
        self.y = self.y - Spaceship.changex  
        return self.y
    def movedown(self):
        self.y = self.y + Spaceship.changex
        return self.y
    def show_spaceship(self):
        window1.blit(self.spaceship,(self.x,self.y))
    def getx(self):
        return self.x
    def gety(self):
        return self.y
class Enemy(Life):
    
    def __init__(self):
        self.x = random.randint(0,800)
        self.y = random.randint(0,600)
    def move(self):
        self.y = self.y + 1
        
    def showenemy(self):
        pass
        
class Aestroid(Enemy):
    aestroid = pygame.transform.smoothscale(aestroid_icon,(70,60))
    
    def showenemy(self):
        window1.blit(self.aestroid,(self.x,self.y))

class Alien(Enemy):
    alien = pygame.transform.smoothscale(alien_icon,(70,60))
    
    def __init__(self):
        super().__init__()
        
    def showenemy(self):
        window1.blit(self.alien,(self.x,self.y))


class Bullet:
    bullet=pygame.transform.smoothscale(bullet_icon,(70,60))
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
            self.y = self.y - 100
    def draw(self):
        window1.blit(self.bullet,(self.x, self.y))
    def remove(self,obj):
        if self.y>300 and self.y<500:
            listofbullet.remove(obj)
        
def collision(self,x1,x2,y1,y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance <= 50:
        return True
    else:
        return False

        
def main():
    Sobj=Spaceship()
    Pobj=Player()
    listofenemy=[]
    listofbullet=[]
    
    def enemymaking():
        for i in range(0,15):
            Aobj = Aestroid()
            A2obj = Alien()
            listofenemy.append(Aobj)
            listofenemy.append(A2obj)
    enemymaking()       
    windowclose = True
    frames = 60
    clock=pygame.time.Clock()
    Life.level= 1
    Life.lives = 5
    
    

    def window2():
        window1.blit(bg,(0,0)) 
        showlives= font.render(f"Lives: {Life.lives}", 1, (255,255,255))
        showlevel= font.render(f"Level: {Life.level}", 1, (255,255,255))
##        showscore= font.render(f"Score: {Pobj.score}", 1, (255,255,255))
        window1.blit(showlives, (10, 10))
##        window1.blit(showscore, (360, 10))
        Pobj.show_score()
        window1.blit(showlevel, (650, 10))
        window1.blit(Sobj.spaceship,(Sobj.x,Sobj.y))
        
        for i in listofenemy:
            i.showenemy()
            i.move()
        for i in listofbullet:
                i.draw()
        pygame.display.update()
    
    while windowclose:
        clock.tick(frames)
        if len(listofenemy) == 0:
            Life.level = Life.level+1
            enemymaking()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                windowclose = False
                
        A=pygame.key.get_pressed()
        if A[pygame.K_SPACE]:
            def bulletmaking():
                for i in range (0,15):
                    Bobj= Bullet(Sobj.getx(),Sobj.gety())
                    listofbullet.append(Bobj)
            bulletmaking()
            for i in listofbullet:
                i.move() 
                
        if A[pygame.K_LEFT] and Sobj.x > 0:
            Sobj.moveleft()
        if A[pygame.K_RIGHT] and Sobj.x < 720:
            Sobj.moveright()
        if A[pygame.K_UP] and Sobj.y > 300:
            Sobj.moveup()
        if A[pygame.K_DOWN] and Sobj.y < 500:
            Sobj.movedown()
        
        
        for event in pygame.event.get():     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and Sobj.x > 0:
                    Sobj.moveleft() 
                if event.key == pygame.K_RIGHT and Sobj.x < 720:
                    Sobj.moveright()
                if event.key == pygame.K_UP and Sobj.y > 300:
                    Sobj.moveup()
                if event.key == pygame.K_DOWN and Sobj.y < 500:
                    Sobj.movedown()
                
        if listofenemy[-1].y > height:
            listofenemy=[]
        window1.blit(bg,(0,0))
        Sobj.show_spaceship()
        window2()
        pygame.display.update()   
main()

