import pygame


pygame.init()
(6, 0)
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel=10
        self.left = False
        self.right = False
        self.isJump = False
        self.jumpCount = 10
        self.walkcount = 10
        self.manstand = True
        self.hitbox = (self.x+17,self.y+11,29,52)

    def draw(self,win):
        if not self.manstand:
            if self.walkcount + 1>=27:
                self.walkcount = 0
            if self.left:
                win.blit(walkLeft[self.walkcount//3], (self.x,self.y))
                self.walkcount+=1
            elif self.right:
                win.blit(walkRight[self.walkcount//3], (self.x,self.y))
                self.walkcount+=1
            
            
        
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))
        self.hitbox = (self.x+17,self.y+11,29,52)
        pygame.draw.rect(win, (255,0,0),self.hitbox,2)
        
        
class Enemey(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]
    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path = [self.x,self.end]
        self.vel = 3
        self.walkcount = 0
        self.hitbox = (self.x + 20,self.y+2,31,57)
        self.health = (self.x + 20, self.hitbox[1]-20,40,10)
        self.score=100
        self.dead=False
        self.win=False
        
        
    def draw(self,win):
        if not self.dead:
            self.move()
        
            if(self.walkcount+1>=33):
                self.walkcount=0
            if self.vel>0:
                win.blit(self.walkRight[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            else:
                win.blit(self.walkLeft[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            self.hitbox = (self.x + 20,self.y+2,31,57)
            self.health = (self.x + 20, self.hitbox[1]-20,40,10)
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            self.healthc = pygame.draw.rect(win,(0,0,0),self.health,2)
        else:
            print("you won")
            self.win=True
            del self
        
        
        
            
        
            
    def move(self):
        if(self.vel > 0):
            if(self.x+self.vel<self.path[1]):
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkcount=0
        else:
            if(self.x - self.vel>self.path[0]):
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkcount=0
                

    def hit(self):
        print("HIT")
        if(self.score <=0):
            print("dead")
            self.dead=True
            
        else:
            self.score=self.score-33
            print("Dying")
            
        
        

    def __del__(self):
        print("deleted")
        
        



class projectile:
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.vel = 8 * facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
        

def redrawgameWindow():
    
    win.blit(bg , (0,0))
    man.draw(win)
    if not goblin.win:
        goblin.draw(win)
        
        
    
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
    
run = True
man = player(300,400,64,64)
goblin = Enemey(20,400,64,64,400)
bullets = []
while(run):
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x-bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
                
        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if man.right:
            facing = 1
        else:
            facing = -1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
    
    
    if keys[pygame.K_LEFT]:
        if man.x <= 0:
            man.x=man.x
            man.manstand= True
        else:
            man.x-= man.vel
            man.left = True
            man.right = False
            man.manstand = False
    
    elif keys[pygame.K_RIGHT]:
        if man.x >=460:
            man.x=man.x
            man.manstand = True
        else:
            man.x += man.vel
            man.right = True
            man.left = False
            man.manstand = False
    else:
        man.manstand = True
        man.walkcount = 0
        
    
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkcount = 0
            
    else:
        neg = 1
        if man.jumpCount<0:
            neg = -1
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount = man.jumpCount -1
                
        else:
            man.isJump = False
            man.jumpCount = 10
    
            
    redrawgameWindow()
    
pygame.quit()           
            
            
                           
        
        
            
       
            
            
                           
    
    
    
    
            
         
                
               
        
            
        

        
            
        

