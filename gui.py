#!/usr/bin/python

# Panda Engine imports
from direct.gui.DirectGui import *
from panda3d.core import TextNode
from panda3d.core import *

# Game Imports

class GUI():
    def __init__(self, _main):
        self.makeButton("start game", Vec3(0.0, 0.0))
        self.makeButton("settings", Vec3(0.0, -0.12))
        self.makeButton("exit", Vec3(0.0, -0.25))

    def createMenu(self):
        pass

    def makeButton(self, text, pos):
        button = DirectButton(text=text, scale=0.07, pos=pos, frameColor=(0.2, 0.2, 0.2, 1), text_fg=(0, 0.862, 0.921, 1), borderWidth=(0.2, 0.2))
        return button