from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.vision import WebcamVideo, ARToolKit
from direct.showbase.InputStateGlobal import inputState
from direct.task import Task
import sys

class Artoolkit(ShowBase):
    def __init__(self, webCamFeed=-1):
        ShowBase.__init__(self)
        base.accept("q", base.oobe)
        webcam = WebcamVideo.getOption(0)
        self.tex = MovieTexture(webcam)

        self.tex.setTexturesPower2(ATSNone)
        self.b : NodePath = loader.loadModel("./gfx/3d/marker.glb")
        self.b.reparentTo(self.render)
        self.ar : ARToolKit = ARToolKit.make(base.cam, "./data/camera_para.dat", 1)

        self.ar.attachPattern("./data/patt.kanji", self.b)
        
        #self.bgCamImageObj.setImage(self.tex)
        self.bgCamImageObj = OnscreenImage(parent=render2dp, image=self.tex)
        base.cam2dp.node().getDisplayRegion(0).setSort(-20) 
        self.updateTask = taskMgr.add(self.setupAR, 'setupAR')

    def setupAR(self, task):
        self.bgCamImageObj.setImage(self.tex)
        self.ar.analyze(self.tex, True)
        print(self.b.getPos(), self.b.getHpr())
        return Task.cont

app = Artoolkit()

app.run()