import pygame
from src.constants import *
from models.node import *

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