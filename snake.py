import pygame
import random

# pygame setup
pygame.init()



score = 0
my_font = pygame.font.SysFont("Comic Sans MS", 30)
text_surface = my_font.render("Score: " + str(score), False, (155, 155, 155))

# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True

border = []
size = 64
# size = 22
height = 10
width = 10

class Player:
  def __init__(self, color, x, y, tick, maxTick):
    self.color = color
    self.x = x
    self.y = y
    self.startX = x
    self.startY = y
    self.tick = tick
    self.maxTick = maxTick
    self.availableDict = {"Left": True, "Right": True, "Up": True, "Down": True}
    self.buffer = {0: "Right", 1: None}
    self.direction = None
    self.body = [(self.x, self.y)]
    self.gamin = True
    self.bc = "gray"

  def setColor(self, color):
    self.color = color

  def restart(self):
    p.color = "Gray20"
    p.bc = "Gray"
    a.reposition()
    self.x = self.startX
    self.y = self.startY
    global size
    size = 64
    self.availableDict = {"Left": True, "Right": True, "Up": True, "Down": True}
    self.buffer = {0: "Right", 1: None}
    self.direction = None
    self.body = [(1, 1)]
    self.gamin = True
    global score
    score = 0
    global text_surface
    text_surface = my_font.render("Score: " + str(score), False, (155, 155, 155))

  def move(self):

    self.body.pop(0)

    if (self.buffer[0]):
      self.direction = self.buffer[0]
      self.buffer[0] = self.buffer[1]
      self.buffer[1] = None

    if (self.direction == 'Left'):
      n = self.x - 1

      #looping border
      if (n, self.y) in border:
        self.x = n + width - 1
      else:
        self.x -= 1

    elif (self.direction == 'Right'):
      n = self.x + 1
      if (n, self.y) in border:
        self.x = n - width + 1
      else:
        self.x += 1

    elif (self.direction == 'Up'):
      m = self.y - 1
      if (self.x, m) in border:
        self.y = m + height - 1
      else:
        self.y -= 1

    elif (self.direction == 'Down'):
      m = self.y + 1
      if (self.x, m) in border:
        self.y = m - height + 1
      else:
        self.y += 1

    if ((self.x, self.y) in self.body):
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
    
class Apple:
  def __init__(self, color,x,y):
    self.color = color
    self.x = x
    self.y = y

  def reposition(self):
    if score < 10:
      self.x = random.randrange(1, width, 1)
      self.y = random.randrange(1, height, 1)
    elif score < 21:
      nx = random.randrange(1, width, 1)
      ny = random.randrange(1, height, 1)
      rx = random.randrange(0, 2, 1)
      ry = random.randrange(0, 2, 1)
      self.x = nx + rx * width
      self.y = ny + ry * height
    else:
      nx = random.randrange(1, width, 1)
      ny = random.randrange(1, height, 1)
      rx = random.randrange(0, 3, 1)
      ry = random.randrange(0, 3, 1)
      self.x = nx + rx * width
      self.y = ny + ry * height

def opposites(d1, d2):
  if (d1 == "Right" and d2 == "Left") or (d1 == "Left" and d2 == "Right") or (d1 == "Up" and d2 == "Down") or (d1 == "Down" and d2 == "Up"):
    return True
  else:
    return False

playerList = []

a = Apple('Red',random.randrange(1,width,1),random.randrange(1,height,1))

p = Player('Gray20', 1, 1, 0, 4)
p2 = Player('Yellow', 11, 1, 0, 4)
p3 = Player('Pink', 1, 11, 0, 4)
adder = Player('Purple', 11, 11, 0, 4)
p5 = Player('Orange', 1, 21, 0, 4)
p6 = Player('Seagreen', 11, 21, 0, 4)
p7 = Player('Blue', 21, 1, 0, 4)
p8 = Player('Indigo', 21, 11, 0, 4)
flak = Player('Gray20', 21, 21, 0, 4)

playerList.append(p)
playerList.append(p2)
playerList.append(p3)
playerList.append(adder)
playerList.append(p5)
playerList.append(p6)
playerList.append(p7)
playerList.append(p8)
playerList.append(flak)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        for s in playerList:
          s.restart()
      if (p.isAvailable("Left") and (event.key == pygame.K_LEFT or event.key == pygame.K_a)):
        for s in playerList:
          s.setBuffer("Left")
          s.lockDirection("Left")
      elif (p.isAvailable("Right") and (event.key == pygame.K_RIGHT or event.key == pygame.K_d)):
        for s in playerList:
          s.setBuffer("Right")
          s.lockDirection("Right")
      elif (p.isAvailable("Up") and (event.key == pygame.K_UP or event.key == pygame.K_w)):
        for s in playerList:
          s.setBuffer("Up")
          s.lockDirection("Up")
      elif (p.isAvailable("Down") and (event.key == pygame.K_DOWN or event.key == pygame.K_s)):
        for s in playerList:
          s.setBuffer("Down")
          s.lockDirection("Down")

    if event.type == pygame.KEYUP:
      if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
        for s in playerList:
          s.unlockDirection("Left")
      if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
        for s in playerList:
          s.unlockDirection("Right")
      if(event.key == pygame.K_UP or event.key == pygame.K_w):
        for s in playerList:
          s.unlockDirection("Up")
      if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
        for s in playerList:
          s.unlockDirection("Down")

  if any((a.x,a.y) in s.body for s in playerList):
    for s in playerList:
      s.grow()
    score += 1
    a.reposition()
    text_surface = my_font.render("Score: " + str(score), False, (155, 155, 155))
    if score > 29:
      # p.bc = "Black"
      size -= 1
    elif score > 21:
      size -= 0
    elif score > 15:
      size -= 2
    elif score > 10:
      size -= 0
    elif score > 5:
      size -= 6
    elif score > 4:
      p.setColor("Lime")
    elif score > 2:
      p.setColor("White")

  if p.gamin:
    #this checks for gameover

    screen.fill("black")
  # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    border = []
    

    for x in range(0, 3 * width + 1, 1):
      border.append((x,0))
      border.append((x,height))
      border.append((x, 2 * height))
      border.append((x, 3 * height))

    # y will not contain the corners an additional time
    for y in range(1, 3 * width + 1, 1):
      border.append((0,y))
      border.append((width,y))
      border.append((2 * width, y))
      border.append((3 * width, y))

    pygame.draw.rect(screen, "red", (a.x * size,a.y * size,size,size))

    for n in playerList:
      for (x, y) in n.body:
        pygame.draw.rect(screen, n.color, (x*size, y*size, size, size))

    for (x,y) in border:
      pygame.draw.rect(screen, p.bc, (x * size,y * size,size,size))


    screen.blit(text_surface, (160,160))

    # flip() the display to put your work on screen
    pygame.display.flip()

    for s in playerList:
      s.moreTime()

    dt = clock.tick(60) / 1000

pygame.quit()