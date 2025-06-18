import pygame

class gameView:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        
    def draw(self, snake, food):
        # filling with black
        self.screen.fill((0, 0, 0))
        # drawing snake
        for segment in snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (*self.to_pixels(segment), self.size, self.size))
        # drawing fruit
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.to_pixels(food.pos), self.size, self.size))
        # updating the screen
        pygame.display.flip()
        
    def to_pixels(self, pos):
        # multiplying positions with size ratio (20) to get it pos in pixels
        return (pos[0] * self.size, pos[1] * self.size)
