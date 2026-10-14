import pygame
import random
import time
import sys

lenght = 2
points = 0
clock = pygame.time.Clock()
go = True

linkeWand = pygame.Rect(-5,0,6,750)
rechteWand = pygame.Rect(1505,0,6,750)
untereWand = pygame.Rect(0,755,1500,6)
obereWand = pygame.Rect(0,-5,1500,6)

#Register
class Felder:
    def __init__(self, x,y):
        self.feld = pygame.draw.rect(screen,(255,255,255),(x,(y),50,50),width=1)
        self.x = x
        self.y = y

class RichtungsBlock:
    def __init__(self,x,y,count):
        self.block = pygame.Rect(x,y,50,50)
        self.count = count+1

class SnakeBlock:
    def __init__(self,x,y,color,next=None):
        self.next = next
        self.x = x
        self.y = y
        self.color = color
        self.block = pygame.draw.rect(screen,self.color,(self.x,(self.y),50,50))
        self.rect = pygame.Rect(self.x+2.5,self.y+2.5,45,45)
        self.north = False
        self.south = False
        self.east = True
        self.west = False
    def check(self):
        if any(self.rect.colliderect( i.block) for i in snake.NorthRectList):
            self.west = False
            self.north = True 
            self.south = False
            self.east = False 
        elif any(self.rect.colliderect(i.block) for i in snake.SouthRectList):
            self.west = False
            self.north = False 
            self.south = True
            self.east = False 
        elif any(self.rect.colliderect( i.block) for i in snake.WestRectList):
            self.west = True
            self.north = False 
            self.south = False
            self.east = False 
        elif any(self.rect.colliderect( i.block) for i in snake.EastRectList):
            self.west = False
            self.north = False 
            self.south = False
            self.east = True 
        


#Snake body
class Snake:
    def __init__(self,head):
        self.head = head
        self.northcount = 0
        self.southcount = 0
        self.eastcount = 0
        self.westcount = 0
        self.northx = 0
        self.northy = 0
        self.southx = 0
        self.southy = 0
        self.eastx = 0
        self.easty = 0
        self.westx = 0
        self.westy = 0
        self.NorthRectList = []
        self.SouthRectList = []
        self.EastRectList = []
        self.WestRectList = []
        self.lenght = 2
    #Movement (when the snake can and cannot move)
    def turn(self):
        if gedrückt[pygame.K_w] and not (head.north or head.south):
            self.NorthRectList.append(RichtungsBlock(self.head.x,self.head.y,self.lenght+1))
        if gedrückt[pygame.K_s] and not (head.north or head.south) :
            self.SouthRectList.append(RichtungsBlock(self.head.x,self.head.y,self.lenght+1))
        if gedrückt[pygame.K_a] and not (head.east or head.west):
            self.WestRectList.append(RichtungsBlock(self.head.x,self.head.y,self.lenght+1))
        if gedrückt[pygame.K_d] and not (head.east or head.west) :
            self.EastRectList.append(RichtungsBlock(self.head.x,self.head.y,self.lenght+1))




    def moveForward(self,go):
        last = self.head
        time.sleep(0.2)
        screen.fill((0,0,0))
        for i in range(0,750,50):
            for j in range(0,1500,50):
                Felder(j,i)
        self.turn()
        for i in self.NorthRectList:
         if i.count ==0:
            self.NorthRectList.remove(i)
         else:
            i.count -= 1
        for i in self.SouthRectList:
         if i.count ==0:
            self.SouthRectList.remove(i)
         else:
            i.count -= 1
        for i in self.EastRectList:
         if i.count ==0:
            self.EastRectList.remove(i)
         else:
            i.count -= 1
        for i in self.WestRectList:
         if i.count ==0:
            self.WestRectList.remove(i)
         else:
            i.count -= 1
       
        time.sleep(0.2)
        while last:
            last.check()
            if last.east:
              last.x += 50
            if last.north:
                last.y -= 50
            if last.south:
                last.y += 50
            if last.west:
                last.x -= 50
            last.block = pygame.draw.rect(screen,last.color,(last.x,(last.y),50,50))
            last.rect = pygame.Rect(last.x+2.5,last.y+2.5,45,45)
            last = last.next
        
    #Snake tail (to spawn new body part)

    def newBodyPart(self):
        last = self.head
        while last.next:
            last = last.next
        if last.east:
         last.next = SnakeBlock(last.x-50,last.y,(0,255,0))
        if last.north:
            last.next = SnakeBlock(last.x,last.y+50,(0,255,0))
        if last.west:
         last.next = SnakeBlock(last.x+50,last.y,(0,255,0))
        if last.south:
            last.next = SnakeBlock(last.x,last.y-50,(0,255,0))
        last.next.north = last.north
        last.next.east = last.east
        last.next.west = last.west
        last.next.south = last.south
        self.lenght += 1
     
        

  
#Register
screen = pygame.display.set_mode([1500,750])
snakeX = random.choice(range(0,1500,50))
snakeY = random.choice(range(0,750,50))
#Snake head (for movement and collision)
head = SnakeBlock(750,350,(255,0,0))
#Snake tail (to spawn new body part)
tail = SnakeBlock(700,350,(0,255,0))
snake = Snake(head)
deactivate = False
head.next = tail
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
#Spawn food (Apple)
    apple = pygame.draw.rect(screen,(255,0,0),(snakeX,snakeY,25,25))
    appleRect = pygame.Rect(snakeX,snakeY,25,25)

    gedrückt = pygame.key.get_pressed()
    snake.moveForward(go)
    apple = pygame.draw.rect(screen,(255,0,0),(snakeX,snakeY,25,25))
    appleRect = pygame.Rect(snakeX,snakeY,25,25)
    #Recognise collision
    if head.rect.colliderect(rechteWand) or head.rect.colliderect(linkeWand) or head.rect.colliderect(obereWand) or head.rect.colliderect(untereWand):
       deactivate = True
    last = head.next
    while last:
       if last.rect.colliderect(head.rect):
          deactivate = True
       last = last.next
    if deactivate:
       print(points)
       break
    if head.block.colliderect(appleRect):
        points += 1
        snake.newBodyPart()
        snakeX = random.choice(range(0,1500,50))
        snakeY = random.choice(range(0,750,50))


    pygame.display.flip()
        
#Count points

pygame.display.flip()

