# pip3 install pygame
import pygame
import math
from queue import PriorityQueue

# displaying the window with an 800x800 resolution and a caption
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# colors
RED = (220, 20, 60)
GREEN = (154, 205, 50)
BLUE = (100, 149, 237)
YELLOW = (255, 255, 51)
WHITE = (255, 250, 250)
BLACK = (0, 0, 0)
PURPLE = (138, 43, 226)
ORANGE = (255, 127, 80)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 209)


# this keeps track of where it is (row, col position in the grid), it needs to know the width of itself,
# to be able to draw itself, and keep track of all of its neighbors and a few other things as-well
class Spot:
    # constructor
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # getting the current position of the spot
    def get_pos(self):
        return self.row, self.row

    # what is considered as closed, or where we already passed and failed
    def is_closed(self):
        return self.col == RED

    # checks if the block is still in the open set
    def is_open(self):
        return self.color == GREEN

    # checks if it is an obstacle
    def is_obstacle(self):
        return self.color == BLACK

    # checking the beginning
    def is_start(self):
        return self.color == ORANGE

    # final block
    def is_end(self):
        return self.color == PURPLE

    # resets all the blocks to white
    def reset(self):
        return self.color == WHITE
