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
		alight.setColor(VBase4(0.1, 0.1, 0.1, 1))
		alnp = render.attachNewNode(alight)
		render.setLight(alnp)
		
		#cube = loader.loadModel("models/cube.gltf")
		dlight = DirectionalLight('dlight')
		dlight.setColor(VBase4(0.9, 0.9, 0.8, 1))
		dlnp = render.attachNewNode(dlight)
		dlnp.setHpr(0, -60, 0)
		render.setLight(dlnp)

		# Point light
		plight = PointLight('plight')
		plight.setColor(VBase4(0.5, 0.7, 0.5, 1))
		#plight.setShadowCaster(True, 512, 512)
		#plight.setAttenuation(Point3(0, 0, 0.5))
		plnp = render.attachNewNode(plight)
		plnp.setPos(10, 10, 15)
		#plnp.showBounds()
		render.setLight(plnp)
		#cube.reparentTo(plnp)

		plight2 = PointLight('plight2')
		plight2.setColor(VBase4(0.8, 0.5, 0.5, 1))
		#plight2.setShadowCaster(True, 512, 512)
		#plight.setAttenuation(Point3(0, 0, 0.5))
		plnp2 = render.attachNewNode(plight2)
		plnp2.setPos(10, 10, 25)
		render.setLight(plnp2)

		self.jumpFrom = []

		#self.load_level("test")
		self.load_cube()
		self.create_floor()

		#base.wireframeOn()

	def load_cube(self):
		cube = loader.loadModel("models/cube.gltf")
		cube.setPos(0, 0, 0)
		cubes = NodePath('Cubes')

		coin = loader.loadModel("models/coin.gltf")
		# Physics Mesh
		
		#print(noise.noise(1, 1, 1))

		for x in range(10):
			for y in range(10):
				for z in range(45):
					prop = randrange(0, 50) / 40
					#noise = PerlinNoise3(0.3, 0.3, 0.3)
					if prop <= 0.1:#noise.noise(x, y, z) >= 0.35:
						randomOffset = randrange(0, 4)

						placeholder = render.attachNewNode("cube"+str(x))
						placeholder.setPos(x+x+randomOffset, y+y+randomOffset, z+z)

						coin_chance = randrange(0, 100) / 100
						if coin_chance <= 0.1:
							coinholder = render.attachNewNode("coin"+str(y))
							coinholder.setPos(x+x+randomOffset, y+y+randomOffset, z+z+1)
							coinholder.setR(90)
							coinholder.setScale(0.5)
							coin.instanceTo(coinholder)

						cube.instanceTo(placeholder)

						shape = BulletBoxShape(Vec3(1, 1, 1))

						body = BulletRigidBodyNode('cube_body')
						body.addShape(shape)
						body.setMass(0)
						body.setStatic(True)

						np = render.attachNewNode(body)
						np.setCollideMask(BitMask32.allOn())
						np.setPos(x+x+randomOffset, y+y+randomOffset, z+z-1)
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