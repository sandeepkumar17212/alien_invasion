import sys
import pygame
from pygame.constants import RESIZABLE



def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    ##sys.flags gives us the ability to resize the windows. 
    ##sys.flags = RESIZABLE
    sys.screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Alien Invasion - by Sandeep Kumar")

    #set veriable for background color.
    bg_color = (230,230,230)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #this will fill the screen with given
        #color on every while loop.
        sys.screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        # it hide the old screen and draw the new one.
        pygame.display.flip()




run_game()

