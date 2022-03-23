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

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()



def algorithm(draw, grid, start, end):
    cnt = 0
    open_set = PriorityQueue()
    open_set.put((0, cnt, start))
    came_from = {}

    g_score = {node: float('inf') for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float('inf') for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    cnt += 1
                    open_set.put((f_score[neighbor], cnt, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
                
        draw()


        if (current != start):
            current.make_closed()

    return False



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


def main(win, size):
    ROWS = 30

    grid = make_grid(ROWS, size)


    run = True
    started = False
    start = None
    end = None

    while run:        
        draw(win, grid, ROWS, size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            pos = pygame.mouse.get_pos()
            row, col = get_clicked_position(pos, ROWS, size)
            node = grid[row][col]

            if not started and pygame.mouse.get_pressed()[0]: #LEFT
                if node.color != BLACK and node != end and not start:
                    start = node
                    node.make_start()
                elif node.color != BLACK and node != start and not end:
                    end = node
                    node.make_end()

                elif node != start and node != end:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #RIGHT
                if node == start:
                    start = None
                elif node == end:
                    end = None
                node.reset()

            if event.type == pygame.KEYDOWN:
                if not started and event.key == pygame.K_SPACE and start and end:
                    started = True
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, size), grid, start, end)
                else:
                    start = None
                    end = None
                    started = False
                    grid = make_grid(ROWS, size)
                



        draw(win, grid, ROWS, size)
                

    pygame.quit()


main(WIN, SIZE)
