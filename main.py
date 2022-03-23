import sys
sys.path.append('../')
import pygame
from src.constants import *
from models.node import *
from lib.A_Start_Algorithm import *
from lib.grid import *

pygame.display.set_caption('A* Path Finding Algorithm')


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
