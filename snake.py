# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


class Player:
  def __init__(self, color, x, y):
    self.color = color
    self.x = x
    self.y = y

  def changeX(self, x):
    self.x += x
  def changeY(self, y):
    self.y += y


  
p = Player('Lime', 32, 32)
aX = 128
aY = 128

def move(direction):
  if (direction == 'A'):
    p.changeX(-16)
  elif (direction == 'D'):
    p.changeX(+16)
  elif (direction == 'W'):
    p.changeY(-16)
  elif (direction == 'S'):
    p.changeY(+16)

while running:


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      move("A")
    elif keys[pygame.K_d]:
      move("D")
    elif keys[pygame.K_w]:
      move("W")
    elif keys[pygame.K_s]:
      move("S")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, p.color, (p.x,p.y,16,16))
    pygame.draw.rect(screen, "red", (aX,aY,16,16))



    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(5) / 1000
    #setting slower clock to slow movement

pygame.quit()