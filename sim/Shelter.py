#!/usr/bin/env python3

import random
from World import World

class Shelter:
	def __init__(self):
		self.pos_x = random.randrange(0, World.width)
		self.pos_y = random.randrange(0, World.height)

shelter_number = 1
shelter_tiles = []
for i in range(shelter_number):
	shelter_tiles.append(Shelter())
