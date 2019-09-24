#!/usr/bin/python

# Panda Engine imports
from panda3d.core import loadPrcFileData
loadPrcFileData("",
"""
    window-title Tower Runner
    load-display pandagl
    fullscreen 0
    win-size 1024 768
    cursor-hidden 0
    sync-video 0
    show-frame-rate-meter 1
"""
)

from direct.showbase.ShowBase import ShowBase

# Game Imports
from game import Game


class TowerRunner(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		render.setShaderAuto()

		self.game = Game(self)
		print(render.ls())


app = TowerRunner()
app.run()