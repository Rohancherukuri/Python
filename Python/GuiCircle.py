# Creating a circle in python
import pygame
# Initialising the circle
pygame.init()
# Creating RGB colors 
COLOR1 = [0,0,0]# Background color
COLOR2 = [255,255,255]# Circle color
# Setting the screen/window size
SIZE=[250,250]
screen=pygame.display.set_mode(SIZE)
# Setting the window /screen caption
pygame.display.set_caption("Gui Circle")
screen.fill(COLOR1) # screen/Background color
# Drawing the circle on the screen/window
pygame.draw.circle(screen,COLOR2,(130,100),30)
# Duration to display the screen/window
c=pygame.time.Clock()
# Updating the screen/window
pygame.display.flip()
c.tick(1)
pygame.quit()
