class Button():
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.screen = screen
    
    def draw(self): 
        #draw button on the screen 
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def isClicked(self, mouseposition):
        #checking if the mouse position collides with the button when it was clicked
        if self.rect.collidepoint(mouseposition):
            return True 
        return False