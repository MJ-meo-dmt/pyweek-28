#!/usr/bin/python

# System imports

# Panda Engine imports
import gltf
from panda3d.bullet import *
from panda3d.core import *
from direct.showbase.InputStateGlobal import inputState
# Game imports

#----------------------------------------------------------------------#

class Player():
    def __init__(self, _game):
        self.game = _game


        ## MOVEMENT INPUTS ##
        inputState.watchWithModifiers('up', 'w')
        inputState.watchWithModifiers('down', 's')
        inputState.watchWithModifiers('left', 'a')
        inputState.watchWithModifiers('right', 'd')
        inputState.watchWithModifiers('space', 'space')

        shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
        body = BulletRigidBodyNode('player')
        body.addShape(shape)
        body.setMass(1)
        
        self.body = render.attachNewNode(body)
        self.body.setPos(0, 0, 1)
        self.body.setCollideMask(BitMask32.allOn())
        
        # Add player customize
        self.playerModel = loader.loadModel("models/player_cube.gltf")
        self.playerModel.setScale(0.5)
        self.playerModel.setPos(0, 0, 0.5)
        self.playerModel.reparentTo(self.body)
      
        self.game.physics.physicsWorld.attachRigidBody(body)
        
        playerRayNode = self.body.attachNewNode("ray-dummy")
        playerRayNode.setCompass()
        self.playerRayNode = playerRayNode
