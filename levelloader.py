#!/usr/bin/python

# System Imports
from random import randrange
# Panda3d Imports
import gltf
from panda3d.bullet import *
from panda3d.core import *

# Game Imports

class LevelLoader():
	def __init__(self, _game):
		self.game = _game

		# Physics World
		self.physicsWorld = self.game.physics.physicsWorld

		# Load Level
		alight = AmbientLight('alight')
		alight.setColor(VBase4(0.5, 0.5, 0.5, 1))
		alnp = render.attachNewNode(alight)
		render.setLight(alnp)
		# Point light
		plight = PointLight('plight')
		plight.setColor(VBase4(0.6, 0.6, 0.6, 1))
		#plight.setAttenuation(Point3(0, 0, 0.5))
		plnp = render.attachNewNode(plight)
		plnp.setPos(0, 0, 30)
		render.setLight(plnp)

		self.jumpFrom = []

		#self.load_level("test")
		self.load_cube()
		self.create_floor()

		#base.wireframeOn()

	def load_cube(self):
		cube = loader.loadModel("models/cube.gltf")
		cube.setPos(0, 0, 0)
		cubes = NodePath('Cubes')

		# Physics Mesh
		

		for x in range(10):
			for y in range(10):
				for z in range(30):
					if x == randrange(0, 10):
						placeholder = render.attachNewNode("cube"+str(x))
						placeholder.setPos(x+x, y+y, z+z)
						cube.instanceTo(placeholder)

						shape = BulletBoxShape(Vec3(1, 1, 1))

						body = BulletRigidBodyNode('cube_body')
						body.addShape(shape)
						body.setMass(0)

						np = render.attachNewNode(body)
						np.setCollideMask(BitMask32.allOn())
						np.setPos(x+x, y+y, z+z-1)
						self.physicsWorld.attachRigidBody(body)
						self.jumpFrom.append(body)

	def create_floor(self):
		shape = BulletPlaneShape(Vec3(0, 0, 0.1), 1)
		node = BulletRigidBodyNode('floor')
		node.addShape(shape)
		np = render.attachNewNode(node)
		np.setPos(0, 0, -3)
		np.setCollideMask(BitMask32.allOn())
		self.physicsWorld.attachRigidBody(node)
		#Give it some visual object
		self.jumpFrom.append(node)






















	# def load_level(self, _level_name):
	# 	self.objectTypes = ["light"]
	# 	self.root = loader.loadModel("models/test_level.gltf")
	# 	self.objects = self.root.findAllMatches('**')

	# 	# Find all objects
	# 	for object in self.objects:
	# 		for type in self.objectTypes:
	# 			if type == "light":
	# 				plight = PointLight('plight')
	# 				plight.setColor(VBase4(0.3, 0.3, 0.5, 1))
	# 				plight.setAttenuation(Point3(0, 0, 0.1))
	# 				plnp = render.attachNewNode(plight)
	# 				plnp.setPos(object.getPos())
	# 				render.setLight(plnp)

	# 	self.root.reparentTo(render)
	# 	self.root.setPos(0, 0, 0)
	# 	print(self.root.find('**/=prop').getTag('prop'))

	# 	