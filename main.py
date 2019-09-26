#!/usr/bin/python

# Panda Engine imports
from panda3d.core import loadPrcFileData
loadPrcFileData("",
"""
    window-title Tower Runner
    load-display pandagl
    fullscreen 0
    win-size 1920 1080
    cursor-hidden 1
    sync-video 0
    show-frame-rate-meter 1
    threading-model Cull/Draw
"""
)

from direct.showbase.ShowBase import ShowBase
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import *

# Game Imports
from game import Game
from gui import GUI


class TowerRunner(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Gui
        #gui = GUI(self)

        render.setShaderAuto()
        self.game = Game(self)
        filters = CommonFilters(base.win, base.cam)
        filters.setBloom()
        filters.setCartoonInk()
        #render.setAttrib(CullFaceAttrib.make(CullFaceAttrib.MCullClockwise))
        #render.setAntialias(AntialiasAttrib.MMultisample)
        #render.setAttrib(LightRampAttrib.makeSingleThreshold(0.5, 0.8))
        #print(render.ls())


app = TowerRunner()
app.run()