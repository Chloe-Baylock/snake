import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

border = []
height = 160
width = 160

for x in range(0, height + 16, 16):
  border.append((x,0))
  border.append((x,height))

# y will not contain the corners an additional time
for y in range(16, width, 16):
  border.append((0,y))
  border.append((width,y))



class Player:
  def __init__(self, color, x, y, tick, maxTick):
    self.color = color
    self.x = x
    self.y = y
    self.tick = tick
    self.maxTick = maxTick
    self.availableDict = {"Left": True, "Right": True, "Up": True, "Down": True}
    self.buffer = {0: "Right", 1: None}
    self.direction = None
    self.body = [(self.x, self.y)]
    self.gamin = True

  def restart(self):
    self.x = 16
    self.y = 16
    self.availableDict = {"Left": True, "Right": True, "Up": True, "Down": True}
    self.buffer = {0: "Right", 1: None}
    self.direction = None
    print(self.body)
    self.body = [(16, 16)]
    print(self.body)
    self.gamin = True

  def move(self):
    self.body.pop(0)

    if (self.buffer[0]):
      self.direction = self.buffer[0]
      self.buffer[0] = self.buffer[1]
      self.buffer[1] = None
    if (self.direction == 'Left'):
      self.x -= 16
    elif (self.direction == 'Right'):
      self.x += 16
    elif (self.direction == 'Up'):
      self.y -= 16
    elif (self.direction == 'Down'):
      self.y += 16

    if ((self.x, self.y) in self.body):
      print("game over")
      p.gamin = False
    
    if (self.x, self.y) in border:
      print("game over")
      p.gamin = False

    self.body.append((self.x, self.y))

  def setDirection(self, direction):
    self.direction = direction
    self.lockDirection(direction)

  def moreTime(self):
    if (self.tick >= self.maxTick):
      self.move()
      self.tick = 0
    else:
      self.tick += 1
  
  def isAvailable(self, direction):
    return self.availableDict[direction]

  def lockDirection(self, direction):
    self.availableDict[direction] = False

  def unlockDirection(self, direction):
    self.availableDict[direction] = True

  def setBuffer(self, direction):
    if self.buffer[1]:
      return
      # dont buffer if we are already full

    elif (self.buffer[0] and (opposites(direction, self.buffer[0]))):
      return

    elif ((not self.buffer[0]) and (opposites(direction, self.direction))):
      return

    elif self.buffer[0] and direction == self.direction:
      # do not buffer the current diretion unless it is second buffer
      self.buffer[1] = direction

    elif self.buffer[0] == direction:
      return
      # do not buffer currently buffered direction

    elif self.buffer[0]:
      self.buffer[1] = direction
      #if there is already something buffered buffer this

    else:
      self.buffer[0] = direction 
      #if you get here buffer this

  def grow(self):
    self.body.append((self.x, self.y))
    print("Score: " + str(len(self.body)))

class Apple:
  def __init__(self, color,x,y):
    self.color = color
    self.x = x
    self.y = y

  def reposition(self):
    self.x = random.randrange(16,width,16)
    self.y = random.randrange(16,height,16)

def opposites(d1, d2):
  if (d1 == "Right" and d2 == "Left") or (d1 == "Left" and d2 == "Right") or (d1 == "Up" and d2 == "Down") or (d1 == "Down" and d2 == "Up"):
    return True
  else:
    return False
  
  
p = Player('Lime', 32, 32, 0, 4)
a = Apple('Red',random.randrange(16,width,16),random.randrange(16,height,16))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        p.restart()
      if (p.isAvailable("Left") and (event.key == pygame.K_LEFT or event.key == pygame.K_a)):
        p.setBuffer("Left")
        p.lockDirection("Left")
      elif (p.isAvailable("Right") and (event.key == pygame.K_RIGHT or event.key == pygame.K_d)):
        p.setBuffer("Right")
        p.lockDirection("Right")
      elif (p.isAvailable("Up") and (event.key == pygame.K_UP or event.key == pygame.K_w)):
        p.setBuffer("Up")
        p.lockDirection("Up")
      elif (p.isAvailable("Down") and (event.key == pygame.K_DOWN or event.key == pygame.K_s)):
        p.setBuffer("Down")
        p.lockDirection("Down")

    if event.type == pygame.KEYUP:
      if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
        p.unlockDirection("Left")
      if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
        p.unlockDirection("Right")
      if(event.key == pygame.K_UP or event.key == pygame.K_w):
        p.unlockDirection("Up")
      if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
        p.unlockDirection("Down")

  if (p.x == a.x and p.y == a.y):
    p.grow()
    a.reposition()
    while (a.x,a.y) in (p.body):
      a.reposition()
    # reposition apple when eaten

  if p.gamin:
    #this checks for gameover

    screen.fill("black")
  # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "red", (a.x,a.y,16,16))
    for (x, y) in p.body:
      pygame.draw.rect(screen, p.color, (x,y,16,16))
    for (x,y) in border:
      pygame.draw.rect(screen, "gray", (x,y,16,16))



    # flip() the display to put your work on screen
    pygame.display.flip()

    p.moreTime()
    dt = clock.tick(60) / 1000
  #setting slower clock to slow movement

pygame.quit()