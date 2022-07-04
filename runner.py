import pygame
from sys import exit

pygame.init()

#Creates a display window for the game.
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Runner') 
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# import sky.png as a surface object
sky_surface = pygame.image.load('graphics/sky.png').convert() 
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics//snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))


player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# adds a rectangle around player surface that allows you to position image easier
player_rect = player_surf.get_rect(midbottom=(80,300))

while True:
    # gets all events and loops through them
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks for exit button for window
            pygame.quit()
            exit() # exits while loop
        # if event.type == pygame.MOUSEMOTION:
        #    if  player_rect.collidepoint(event.pos): print('collision')
    #display sky surface on display surface
    screen.blit(sky_surface, (0,0)) 
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800   
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)
    
    #checks if there is a collision between two rects
    # if player_rect.colliderect(snail_rect):
    #     print('collision')
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #    print(pygame.mouse.get_pressed())
    
    # Updates the display window
    pygame.display.update()
    clock.tick(60) #caps framerate to 60 fps