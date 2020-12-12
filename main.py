# pip3 install pygame
import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))  # square display window
pygame.display.set_caption("A* Path Finding Algorithm")  # just the caption for the window

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
