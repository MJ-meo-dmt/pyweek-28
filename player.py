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
        inputState.watchWithModifiers('esc', 'escape')

        shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
        body = BulletCharacterControllerNode(shape, 0.5, 'player') #BulletRigidBodyNode('player')

        #body.addShape(shape)
        #body.setMass(1)
        #body.setKinematic(True)

        
        self.body = render.attachNewNode(body)
        self.body.setPos(0, 0, 1)
        self.body.setCollideMask(BitMask32.allOn())
        
        # Add player customize
        self.playerModel = loader.loadModel("models/player_cube.gltf")
        self.playerModel.setScale(0.5)
        self.playerModel.setPos(0, 0, 0.5)
        self.playerModel.reparentTo(self.body)
      
        self.game.physics.physicsWorld.attachCharacter(body)
        
        playerRayNode = self.body.attachNewNode("ray-dummy")
        playerRayNode.setCompass()
        self.playerRayNode = playerRayNode

        # mouse
        self.winXhalf = base.win.getXSize()//2
        self.winYhalf = base.win.getYSize()//2
        
        # Should move the camera stuff to the baseCamera.py
        base.camera.reparentTo(self.body)
        #base.camera.setPos(0, 5, 0)
        base.camLens.setFov(90)
        base.camLens.setNear(0.1)
        
        
        self.mouseSpeedX = 3
        self.mouseSpeedY = 0.1
        self.camP = 5
        
        
    def getMouse(self, dt):
        
        # Handle mouse
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        
        if base.win.movePointer(0, self.winXhalf, self.winYhalf):
            omega = (x - self.winXhalf)*-self.mouseSpeedX
            #print(omega)
            self.body.node().setAngularMovement(omega)
            #self.body.setH(self.body.getH() - 0.3* x)
            cam = base.cam.getP() - (y - self.winYhalf) * self.mouseSpeedY / 2
            if cam <-80:
                cam = -80
            elif cam > 90:
                cam = 90
            base.cam.setP(cam)
            #base.camera.setY(base.camera, 8.0)

        #base.camera.lookAt(self.body)

    def update(self, dt):
        self.getMouse(dt)