import pygame
import sys
class gameController:
    def __init__(self,model,food,view,size):
        self.snake = model
        self.food = food
        self.view = view
        self.size = size
        self.clock = pygame.time.Clock()
    def handle_input(self):
     
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.snake.change_dir((0, -1))
        elif keys[pygame.K_DOWN]:
            self.snake.change_dir((0, 1))
        elif keys[pygame.K_LEFT]:
            self.snake.change_dir((-1, 0))
        elif keys[pygame.K_RIGHT]:
            self.snake.change_dir((1, 0))
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.handle_input()
            self.snake.move()
            # snake touched food
            if self.snake.body[0] == self.food.pos:
                self.snake.grow()
                self.food.relocate(self.snake.body)
            if self.snake.collide_self() or self.snake.collide_wall(self.size):
                pygame.quit()
                sys.exit()
            self.view.draw(self.snake, self.food)
            self.clock.tick(10)
