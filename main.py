#!/usr/bin/python

# Panda Engine imports
from panda3d.core import loadPrcFileData
loadPrcFileData("",
"""
    window-title Tower Runner
    load-display pandagl
    fullscreen 0
    win-size 1024 768
    cursor-hidden 1
    sync-video 0
    show-frame-rate-meter 1
"""
)

from direct.showbase.ShowBase import ShowBase
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import *

# Game Imports
from game import Game


class TowerRunner(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        render.setShaderAuto()
        self.game = Game(self)
        filters = CommonFilters(base.win, base.cam)
        filters.setBloom()
        filters.setCartoonInk()
        #render.setAttrib(LightRampAttrib.makeSingleThreshold(0.5, 0.8))
        print(render.ls())


app = TowerRunner()
app.run()