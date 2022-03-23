import re
import pygame
import math
from constants import *
from models.node import *
from queue import PriorityQueue


pygame.display.set_caption('A* Path Finding Algorithm')


# this is the heuristic function used in the A* pathfinding algorithm
# We will use the manhattan distance
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def make_grid(rows, size):
    grid = []
    # size is the total size (height and width) of the grid

    # rect_size is the size (height and width) of each grid item (square)
    rect_size = size // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, rect_size, rows)
            grid[i].append(node)

    return grid


def draw_grid(win, rows, size):
    rect_size = size // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * rect_size), (size, i * rect_size))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * rect_size, 0), (j * rect_size, size))

def draw(win, grid, rows, size):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, size)
    pygame.display.update()

def get_clicked_position(mouse_pos, rows, size):
    rect_size = size // rows
    y, x = mouse_pos
    row = y // rect_size
    col = x // rect_size
    
    return row, col