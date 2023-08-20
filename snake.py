# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


class Player:
  def __init__(self, color, x, y, direction):
    self.color = color
    self.x = x
    self.y = y
    self.direction = direction

  def move(self):
    if (p.direction == 'A'):
      self.x -= 16
    elif (p.direction == 'D'):
      self.x += 16
    elif (p.direction == 'W'):
      self.y -= 16
    elif (p.direction == 'S'):
      self.y += 16

class Apple:
  def __init__(self, color,x,y):
    self.color = color
    self.x = x
    self.y = y

  def reposition(self):
    self.x = random.randrange(0,256,16)
    self.y = random.randrange(0,256,16)
  
p = Player('Lime', 32, 32, 'D')
a = Apple('Red',random.randrange(0,256,16),random.randrange(0,256,16))
aX = 128
aY = 128

while running:
  p.move()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

  keys = pygame.key.get_pressed()
  if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
    p.direction = "A"
  elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
    p.direction = "D"
  elif (keys[pygame.K_w] or keys[pygame.K_UP]):
    p.direction = "W"
  elif (keys[pygame.K_s] or keys[pygame.K_DOWN]):
    p.direction = "S"

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

  dt = clock.tick(60) / 1000
  #setting slower clock to slow movement

pygame.quit()