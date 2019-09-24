#!/usr/bin/python

# System Imports
# Panda3d Imports

# Game Imports
from physics import Physics
from levelloader import LevelLoader
from player import Player

class Game():
	def __init__(self, _main):

		self.main = _main

		# Physics
		self.physics = Physics(self)
		# Level 
		self.levelloader = LevelLoader(self)
		# Input
		# Player
		self.player = Player(self)
		# GUI

		# STATE
		self.isFloating = False

	def start_game(self):
		self.physics.start()

	def stop_game(self):
		self.physics.stop()