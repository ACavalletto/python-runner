import pygame

pygame.init()

#Creates a display window for the game.
screen = pygame.display.set_mode((800, 400)) 

while True:
    # gets all events and loops through them
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks for exit button for window
            pygame.quit()
    # draw all our elements
    # Updates the display window
    pygame.display.update()