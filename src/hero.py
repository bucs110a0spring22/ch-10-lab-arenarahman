import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        """constructor for the Hero class, takes name, x, y, img_file as parameters and stores than as instance variables.
      self: (str)  represent an instance (object) of the given class
      name = (str) name sets the name of the surface object
      x = (int) x value of the position of the hero 
      y = (int) y value of the position of the hero
      img_file: (str) name of the image file name for the hero
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
        self.name = name
        self.speed = 3
        self.health = 3

    #methods to make moving our hero easier
    def move_up(self):
        """moves the hero easier when it moves up
      self: (str) represent an instance (object) of the given class"""
        self.rect.y -= self.speed
    def move_down(self):
        """moves the hero easier it moves down
     self: (str) represent an instance (object) of the given class
      return: None"""
        self.rect.y += self.speed
    def move_left(self):
        """moves the hero easier when it moves left
      (str)  represent an instance (object) of the given class
      return: None"""
        self.rect.x -= self.speed
    def move_right(self):
        """moves the hero easier when it moves right
      (str)  represent an instance (object) of the given class
      return: None"""
        self.rect.x += self.speed

    def fight(self, opponent):
        """ sets up what happens to hero's health when they either fail or succeeds an attack
       self: (str)  represent an instance (object) of the given class
      opponent: (str) the enemy the hero fights
      return: None """  
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True


     
    def update(self,width=640, height=480):
        """function that makes sure the hero does not           move off the screen
      self: (str) represent an instance (object) of the given class
      width: (int) width of the screen
      height: (int) height of the screen"""
        if self.rect.left < 0:
          self.rect.left = 0
        if self.rect.right > width:
          self.rect.right = width
        if self.rect.top <= 0:
          self.rect.top = 0
        if self.rect.bottom >= height:
          self.rect.bottom = height
