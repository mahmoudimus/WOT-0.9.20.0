# 2017.08.29 21:46:24 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/component_override.py
from helpers import dependency
from skeletons.gui.game_control import IBootcampController

class BootcampComponentOverride(object):
    bootcampController = dependency.descriptor(IBootcampController)

    def __init__(self, usualObject, bootcampObject):
        super(BootcampComponentOverride, self).__init__()
        self.__usualObject = usualObject
        self.__bootcampObject = bootcampObject

    def __call__(self):
        if self.bootcampController.isInBootcamp():
            return self.__bootcampObject
        return self.__usualObject
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\component_override.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:24 Støední Evropa (letní èas)
