#!/usr/bin/env python3

import random
import math
import os
import string

from World import World
from Food import food_tiles
from Shelter import shelter_tiles

class Human:
	def __init__(self):
		self.pos_x = random.randrange(0, World.width)
		self.pos_y = random.randrange(0, World.height)

		self.name = 'error'
		self.surname = list(string.ascii_uppercase)[random.randrange(0, len(list(string.ascii_uppercase)))]
		self.age = random.randrange(20, 41)
		self.gender = random.choice(['female', 'male'])
		self.gender_glyph = '♀' if self.gender == 'female' else '♂'
		self.set_name()

		self.need_hunger = random.randrange(40, 101)
		self.need_sleep = random.randrange(50, 101)
		
		self.is_eating = False
		self.is_sleeping = False
		self.target = None
		self.set_status('Wandering.')
		self.is_dead = False

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
		if self.is_dead or self.is_eating or self.is_sleeping:
			pass
		elif self.target:
			if(self.pos_x != self.target.pos_x or self.pos_y != self.target.pos_y):
				if self.pos_x == self.target.pos_x or self.pos_y == self.target.pos_y:
					direction = 2
				else:
					direction = random.randrange(0, 2)
				# or direction == 2 to let it pass without randoming so it moves regardless
				if direction == 0 or direction == 2:
					if self.pos_x > self.target.pos_x:
						self.pos_x -= 1
					elif self.pos_x < self.target.pos_x:
						self.pos_x += 1
				if direction == 1 or direction == 2:
					if self.pos_y > self.target.pos_y:
						self.pos_y -= 1
					elif self.pos_y < self.target.pos_y:
						self.pos_y += 1
			else:
				reason = ''
				if self.target_reason == 'food':
					reason = 'food'
				elif self.target_reason == 'shelter':
					reason == 'shelter'
				self.target_reason = ''
				self.target = None
				if reason == 'food':
					self.eat()
				elif reason == 'shelter':
					self.sleep()
		else:
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

	def decrease_needs(self):
		if not self.is_eating:
			self.need_hunger -= random.randrange(2, 6)
		if not self.is_sleeping:
			self.need_sleep -= random.randrange(1, 4)

	def check_needs(self):
		if self.need_sleep < -15 or self.need_hunger < -25:
			self.die()
		elif self.is_sleeping:
			self.is_eating = False
			self.set_status('Sleeping.')
			self.sleep()
		elif self.need_sleep <= 10 and not self.is_sleeping:
			self.is_eating = False
			self.set_status('Passed out!')
			self.is_sleeping = True
			self.sleep()
		elif self.need_hunger <= 50 and not self.is_eating:
			self.is_sleeping = False
			self.set_status('Looking for food.')
			self.get_closest_object('food')
		elif self.is_eating:
			self.is_sleeping = False
			self.set_status('Eating.')
			self.eat()
		elif self.need_sleep <= 30 and not self.is_sleeping:
			self.set_status('Looking for shelter.')
			self.get_closest_object('shelter')
		else:
			self.set_status('Wandering.')

	def eat(self):
		self.is_eating = True
		self.set_status('Eating.')
		if self.need_hunger < 100:
			self.need_hunger = self.need_hunger + 20 if self.need_hunger + 20 <= 100 else 100
		else:
			self.is_eating = False
			self.set_status('Wandering.')

	def sleep(self):
		self.is_sleeping = True
		if self.need_sleep < 100:
			self.need_sleep = self.need_sleep + 8 if self.need_sleep + 8 <= 100 else 100
		else:
			self.is_sleeping = False
			self.set_status('Wandering.')
	
	def get_closest_object(self, reason):
		# formula: v/ (x2 - x1)^2 + (y2 - y1)^2
		best_target = None
		closest_distance = float('inf')

		if reason == 'food':
			tiles = food_tiles
		elif reason == 'shelter':
			tiles = shelter_tiles

		for obj in tiles:
			distance_to_obj = math.sqrt((obj.pos_x - self.pos_x) ** 2 + (obj.pos_y - self.pos_y) ** 2)
			if distance_to_obj < closest_distance:
				closest_distance = distance_to_obj
				best_target = obj

		self.target = best_target
		self.target_reason = reason

	def die(self):
		self.is_dead = True
		self.set_status('Died!!!')

	def set_status(self, status):
		'''Set status.'''
		# TODO: maybe limit width here to have a good looking UI^tm
		self.status = status

	def set_name(self):
		name_list = list(filter(None, open(os.path.join('names', '%s_names.txt' % self.gender)).read().split('\n')))
		self.name = name_list[random.randrange(0, len(name_list))]
