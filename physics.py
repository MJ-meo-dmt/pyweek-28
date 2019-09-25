#!/usr/bin/python

# System Imports
# Panda3d Imports
from panda3d.bullet import *
from panda3d.core import *
from direct.task.Task import Task
from direct.showbase.InputStateGlobal import inputState

# Game Imports

class Physics():
	def __init__(self, _game):
		self.game = _game

		# Physics World
		self.physicsWorld = BulletWorld()
		self.physicsWorld.setGravity(0, 0, -9.81)
		#self.enableDebug()
		self.start()
		self.move_speed = 5.0
		self.jump_speed = 8.0
		self.jump_height = 2.0

	def enableDebug(self):
		debugNode = BulletDebugNode('Debug')
		debugNode.showWireframe(True)
		debugNode.showConstraints(True)
		debugNode.showBoundingBoxes(False)
		debugNode.showNormals(False)
		debugNP = render.attachNewNode(debugNode)
		debugNP.show()
		self.physicsWorld.setDebugNode(debugNP.node())

	def movement(self):
		## GET PLAYER BODY ##
		self.playerBody = self.game.player.body
		speed = Vec3(0, 0, 0)
		jump = Vec3(0, 0, 0)
		if inputState.isSet('left'):
			#self.checkFloorCollide()
			speed.setX(-self.move_speed)

		if inputState.isSet('right'):
			speed.setX(self.move_speed)

		if inputState.isSet('up'):
			speed.setY(self.move_speed)

		if inputState.isSet('down'):
			speed.setY(-self.move_speed)

		if inputState.isSet('space'):
			self.doJump()
			#if self.game.isFloating != True:
			#	jump.setZ(self.jump_speed)
			#	self.game.isFloating = True
			#elif self.game.isFloating == True:
			#	jump.setZ(0.0)
				#self.game.isFloating = False
		#self.playerBody.node().setActive(True)
		self.playerBody.node().setLinearMovement(speed, True)#applyCentralForce(speed)
		#self.playerBody.node().#applyCentralImpulse(jump)

	def doJump(self):
		self.game.player.body.node().setMaxJumpHeight(self.jump_height)
		self.game.player.body.node().setJumpSpeed(self.jump_speed)
		self.game.player.body.node().doJump()

	def checkFloorCollide(self):
		pos = Point3(self.game.player.playerRayNode.getPos(render))
		pFrom = Point3(pos)
		pTo = Point3(float(pos.getX()), float(pos.getY()),float(pos.getZ()-1))
		result = self.physicsWorld.rayTestClosest(pFrom, pTo)
		contactNode = result.getNode()

		if contactNode == None:
			self.game.isFloating = True
		elif contactNode in self.game.levelloader.jumpFrom:
			self.game.isFloating = False

	def update(self, task):
		dt = globalClock.getDt()
		self.physicsWorld.doPhysics(dt)#, 5, 1.0/240.0)
		self.movement()
		self.game.player.update(dt)

		return task.cont

	def start(self):
		taskMgr.add(self.update, "update-physics", priority=1)

	def stop(self):
		taskMgr.remove("update-physics")