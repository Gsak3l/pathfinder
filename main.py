# pip3 install pygame
# import os  # hide the message from pygame
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
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
    def is_barrier(self):
        return self.color == BLACK

    # checking the beginning
    def is_start(self):
        return self.color == ORANGE

    # final block
    def is_end(self):
        return self.color == TURQUOISE

    # resets all the blocks to white
    def reset(self):
        return self.color == WHITE

    # --- M A K E --- #
    # make changes the color instead of giving back colors, it changes them
    def make_closed(self):
        self.col = RED

    def make_open(self):
        self.color = GREEN

    def make_start(self):
        self.color = ORANGE

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    # what we call when we want to draw the method on the screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    # this compares two Spots together, and in this case, it always says that the other spot is greater than this spot
    def __lt__(self, other):
        return False


# p1 p2 should be like x and y or row and col
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# creating the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows  # integer division
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


# drawing the grid to the white cubes
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # drawing horizontal lines, starting with the 0, gap and ending at 800, gap in this specific case
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            # flipping the first draw
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# this draws everything
def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


# gets where the position of the block clicked is, on the grid
# this helps us understand what color the block should be
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col


# this is the manager for everything that is happening
def main(win, width):
    rows = 50
    grid = make_grid(rows, width)

    start = None
    end = None

    run = True
    started = False

    # checking all the events that happened, when the algorithm started (timers, keyboard things etc)
    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # x button
                run = False

            # this blocks the user from doing stuff when the algorithm has already started
            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # left
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                # if start hasn't been defined yet
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # right
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()

                # resetting start and end if they press on either of these
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

    pygame.quit()


main(WIN, WIDTH)
