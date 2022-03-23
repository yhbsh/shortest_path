import pygame
import math
from constants import *
from queue import PriorityQueue


SIZE = 800
WIN = pygame.display.set_mode((SIZE, SIZE))

pygame.display.set_caption('A* Path Finding Algorithm')


# this is the heuristic function used in the A* pathfinding algorithm
# We will use the manhattan distance
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)
