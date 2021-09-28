
##external moduls imported
import sys
import pygame

#internal modules imported
from settings import Settings
from ship import Ship



def run_game():
    # Initialize game and create a screen object.
    pygame.init()


    #created the instance of the class ""Settings()"" to use it.
    ai_settings = Settings()



    ##sys.flags gives us the ability to resize the windows. 
    ##sys.flags = RESIZABLE
    sys.screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion - by Sandeep Kumar")

    #set veriable for background color.
    bg_color = (ai_settings.bg_color)

    #draw a ship by making an instance for Ship class.
    #to make an instance of ship, we need to provide screen attrribute 
    #which has the info of screen size and other info.
    ship = Ship(sys.screen)



    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #this will fill the screen with given
        #color on every while loop.
        sys.screen.fill(bg_color)
        
        #putting the ship on top of backgroud.
        ship.blitme()

        # Make the most recently drawn screen visible.
        # it hide the old screen and draw the new one.
        pygame.display.flip()




run_game()

