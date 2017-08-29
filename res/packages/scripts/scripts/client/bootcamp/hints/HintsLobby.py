# 2017.08.29 21:43:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bootcamp/hints/HintsLobby.py
import time
import math
import weakref
from constants import HINT_TYPE
from HintsBase import HintBase, HINT_COMMAND
from copy import copy

class HintLobbyRotate(HintBase):

    def __init__(self, params):
        super(HintLobbyRotate, self).__init__(None, HINT_TYPE.HINT_ROTATE_LOBBY, params['timeout'])
        self.__prevCameraDirection = None
        self.__neededAngle = math.radians(params['angle'])
        self.__curAngle = 0.0
        self.__cancelAngle = params.get('cancelAngle', 0.2)
        self.__hangarSpace = None
        return

    def update(self):
        if self._state == HintBase.STATE_INACTIVE or self._state == HintBase.STATE_COMPLETE:
            return
        elif self.__hangarSpace is None:
            return
        else:
            camera = self.__hangarSpace.space.getCamera()
            if camera is None:
                return
            elif self.__prevCameraDirection is None:
                self.__prevCameraDirection = copy(camera.direction)
                self.__prevCameraDirection.normalise()
                return
            curDirection = copy(camera.direction)
            curDirection.normalise()
            cosAngle = self.__prevCameraDirection.dot(curDirection)
            self.__curAngle += abs(math.acos(cosAngle))
            self.__prevCameraDirection = curDirection
            resultCommand = None
            if self._state == HintBase.STATE_HINT:
                if self.__curAngle > self.__neededAngle:
                    self._state = HintBase.STATE_COMPLETE
                    resultCommand = HINT_COMMAND.SHOW_COMPLETED_WITH_HINT
            elif self._state == HintBase.STATE_DEFAULT:
                if time.time() - self._timeStart > self._timeout:
                    self._state = HintBase.STATE_HINT
                    resultCommand = HINT_COMMAND.SHOW
                elif self.__curAngle > self.__cancelAngle:
                    self._state = HintBase.STATE_COMPLETE
                    resultCommand = HINT_COMMAND.SHOW_COMPLETED
            return resultCommand

    def start(self):
        self._state = HintBase.STATE_DEFAULT
        self._timeStart = time.time()
        from gui.shared.utils.HangarSpace import g_hangarSpace
        self.__hangarSpace = weakref.proxy(g_hangarSpace)

    def stop(self):
        self._state = HintBase.STATE_INACTIVE
        self.__hangarSpace = None
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\hints\HintsLobby.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:50 St�edn� Evropa (letn� �as)
