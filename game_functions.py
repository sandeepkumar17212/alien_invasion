import pygame
import sys




def check_events(ship):

    # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship to right from centerx by one position.
                    ship.rect.centerx += 5


def update_screen(ai_settings,screen,ship):
    #this will fill the screen with given
        #color on every while loop.
        sys.screen.fill(ai_settings.bg_color)
        
        #putting the ship on top of backgroud.
        ship.blitme()

        # Make the most recently drawn screen visible.
        # it hide the old screen and draw the new one.
        pygame.display.flip()