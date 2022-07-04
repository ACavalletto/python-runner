import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score:  {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()

#Creates a display window for the game.
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Runner') 
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0


# import sky.png as a surface object
sky_surf = pygame.image.load('graphics/sky.png').convert() 
ground_surf = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center= (400, 50))

snail_surf = pygame.image.load('graphics//snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))


player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# adds a rectangle around player surface that allows you to position image easier
player_rect = player_surf.get_rect(midbottom=(80,300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400,80))


instructions_surf = test_font.render(f'Press Space To Start.', False, (111,196,169))
instructions_rect = instructions_surf.get_rect(center = (400, 330))


while True:
    # gets all events and loops through them
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks for exit button for window
            pygame.quit()
            exit() # exits while loop
            
        # if statements that check for button press or mouse click to jump character and character is on the floor
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time =  int(pygame.time.get_ticks() / 1000)
                
    if game_active:       #active game code
        #display sky surface on display surface
        screen.blit(sky_surf, (0,0)) 
        screen.blit(ground_surf, (0,300))
        
        # pygame.draw.rect(screen, '#c0e8ec',score_rect)
        # pygame.draw.rect(screen, '#c0e8ec',score_rect,10)
        # screen.blit(score_surf, score_rect)
        score = display_score()
        
        snail_rect.x -= 4
        if snail_rect.right <= 0:snail_rect.left = 800   
        screen.blit(snail_surf, snail_rect)
        
        player_gravity += 1
        player_rect.y += player_gravity
        # keeps player on the "floor" and if not jumping
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        
        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        score_surf = test_font.render(f'Score: {score}', False, (111,196,169))
        score_rect = score_surf.get_rect(center = (400, 330))
        if score == 0:
            screen.blit(instructions_surf, instructions_rect)
        else: screen.blit(score_surf, score_rect)
    # Updates the display window
    pygame.display.update()
    clock.tick(60) #caps framerate to 60 fps