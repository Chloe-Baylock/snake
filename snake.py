# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


class Player:
  def __init__(self, color, x, y, direction, tick, maxTick):
    self.color = color
    self.x = x
    self.y = y
    self.direction = direction
    self.tick = tick
    self.maxTick = maxTick
    self.availableDict = {"Left": True, "Right": True, "Up": True, "Down": True}

  def move(self):
    if (p.direction == 'Left'):
      self.x -= 16
    elif (p.direction == 'Right'):
      self.x += 16
    elif (p.direction == 'Up'):
      self.y -= 16
    elif (p.direction == 'Down'):
      self.y += 16

  def setDirection(self, direction):
    self.direction = direction
    self.lockDirection(direction)

  def moreTime(self):
    if (self.tick == self.maxTick):
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


class Apple:
  def __init__(self, color,x,y):
    self.color = color
    self.x = x
    self.y = y

  def reposition(self):
    self.x = random.randrange(0,256,16)
    self.y = random.randrange(0,256,16)
  
p = Player('Lime', 32, 32, 'Right', 0, 7)
a = Apple('Red',random.randrange(0,256,16),random.randrange(0,256,16))
aX = 128
aY = 128

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if (p.isAvailable("Left") and (event.key == pygame.K_LEFT or event.key == pygame.K_a)):
        p.setDirection("Left")
        print("Left")
      elif (p.isAvailable("Right") and (event.key == pygame.K_RIGHT or event.key == pygame.K_d)):
        p.setDirection("Right")
        print("Right")
      elif (p.isAvailable("Up") and (event.key == pygame.K_UP or event.key == pygame.K_w)):
        p.setDirection("Up")
        print("Up")
      elif (p.isAvailable("Down") and (event.key == pygame.K_DOWN or event.key == pygame.K_s)):
        p.setDirection("Down")
        print("Down")

    if event.type == pygame.KEYUP:
      if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
        p.unlockDirection("Left")
      if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
        p.unlockDirection("Right")
      if(event.key == pygame.K_UP or event.key == pygame.K_w):
        p.unlockDirection("Up")
      if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
        p.unlockDirection("Down")



  # if (p.isAvailable("Left") and (downKeys[pygame.K_a] or downKeys[pygame.K_LEFT])):
  #   p.setDirection("Left")
  # elif (p.isAvailable("Right") and (downKeys[pygame.K_d] or downKeys[pygame.K_RIGHT])):
  #   p.setDirection("Right")
  # elif (p.isAvailable("Up") and (downKeys[pygame.K_w] or downKeys[pygame.K_UP])):
  #   p.setDirection("Up")
  # elif (p.isAvailable("Down") and (downKeys[pygame.K_s] or downKeys[pygame.K_DOWN])):
  #   p.setDirection("Down")

  
  

  if (p.x == a.x and p.y == a.y):
    a.reposition()
    # reposition apple when eaten

  # fill the screen with a color to wipe away anything from last frame
  screen.fill("black")

  # RENDER YOUR GAME HERE
  pygame.draw.rect(screen, p.color, (p.x,p.y,16,16))
  pygame.draw.rect(screen, "red", (a.x,a.y,16,16))



  # flip() the display to put your work on screen
  pygame.display.flip()

  p.moreTime()
  dt = clock.tick(60) / 1000
  #setting slower clock to slow movement

pygame.quit()