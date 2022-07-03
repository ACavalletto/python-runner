import pygame
from sys import exit

pygame.init()

#Creates a display window for the game.
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Runner') 
clock = pygame.time.Clock()

# import sky.png as a surface object
sky_surface = pygame.image.load('graphics/sky.png') 

ground_surface = pygame.image.load('graphics/ground.png')


while True:
    # gets all events and loops through them
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks for exit button for window
            pygame.quit()
            exit() # exits while loop
    
    #display sky surface on display surface
    screen.blit(sky_surface, (0,0)) 
    screen.blit(ground_surface, (0,300))
    
    # Updates the display window
    pygame.display.update()
    clock.tick(60) #caps framerate to 60 fps