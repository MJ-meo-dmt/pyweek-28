#!/usr/bin/python

# Panda Engine imports
from direct.gui.DirectGui import *
from panda3d.core import TextNode

# Game Imports

class GUI():
    def __init__(self, _main):
        self.makeButton("Start Game")
        self.makeButton("Options")

    def createMenu(self):
        pass

    def makeButton(self, text):
        button = DirectButton(text=text, scale=0.08)
        return button