import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        """the constructor for the Enemy class, takes name, x, y, img_file as parameters and stores than as instance variables 
      self: (str)  represent an instance (object) of the given class
      name = (str) name sets the name of the surface object
      x = (int) x value of the position of the enemy 
      y = (int) y value of the position of the enemy
      img_file: (str) name of the image file name for the enemy
      return: None """
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
        """updates the movement of the enemy to be random 
      self: (str)  represent an instance (object) of the given class
      return: None"""
        self.rect.x = self.rect.x + random.randint(-1,1)
        self.rect.y = self.rect.y + random.randint(-1,1)