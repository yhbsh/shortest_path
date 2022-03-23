import pygame
import math
from constants import *
from queue import PriorityQueue


SIZE = 800
WIN = pygame.display.set_mode((SIZE, SIZE))

pygame.display.set_caption('A* Path Finding Algorithm')

# this is a spot in the grid
