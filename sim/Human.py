#!/usr/bin/env python3

import random
from World import World

class Human:
	def __init__(self, name):
		self.name = name
		self.age = 22
		self.hunger = 77
		self.sleep = 88
		self.pos_x = 2
		self.pos_y = 2

	def set_position(self, x, y):
		if x < 0:
			self.pos_x = 0
		elif x >= World.width:
			self.pos_x = World.width - 1
		else:
			self.pos_x = x
		if y < 0:
			self.pos_y = 0
		elif y >= World.height:
			self.pos_y = World.height - 1
		else:
			self.pos_y = y

	def move_around(self):
		# start, end (not including), skip first x results
		direction = random.randrange(0, 4)
		if direction == 0:
			self.set_position(self.pos_x, self.pos_y - 1)
		elif direction == 1:
			self.set_position(self.pos_x - 1, self.pos_y)
		elif direction == 2:
			self.set_position(self.pos_x, self.pos_y + 1)
		elif direction == 3:
			self.set_position(self.pos_x + 1, self.pos_y)
