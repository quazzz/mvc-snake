import pygame
from model import Snake, Food
from view import gameView
from controller import gameController

def main():
    pygame.init()
    grid_size = 20
    cell_size = 20
    screen = pygame.display.set_mode((grid_size * cell_size, grid_size * cell_size))
    pygame.display.set_caption("snake game")
    snake = Snake()
    food = Food(grid_size)
    view = gameView(screen, cell_size)
    controller = gameController(snake, food, view, grid_size)
    controller.run()

if __name__ == '__main__':
    main()
    