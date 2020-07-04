#!/usr/bin/env python3

import random
from World import World

class Food:
	def __init__(self):
		self.pos_x = random.randrange(0, World.width)
		self.pos_y = random.randrange(0, World.height)

food_supply = 1
food_tiles = []
for i in range(food_supply):
	food_tiles.append(Food())
