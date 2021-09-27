import pygame

class Ship():
    def __init__(self,screen):
        self.screen=screen


        #load the ship image.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()


        #start the new ship at the bottom center of the screen.
        self.rect.centerx= self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
    
        ##drwaing the ship at the current location
        self.screen.blit(self.image,self.rect)





