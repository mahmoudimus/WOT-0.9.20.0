# 2017.08.29 21:43:44 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/BootCampEvents.py
import BigWorld
import Event

class _BootCampEvents(object):

    def __init__(self):
        self.__manager = Event.EventManager()
        self.onBootcampBecomePlayer = self._createEvent()
        self.onBootcampBecomeNonPlayer = self._createEvent()
        self.onBootcampStarted = self._createEvent()
        self.onBootcampFinished = self._createEvent()
        self.onIntroVideoStop = self._createEvent()
        self.onOutroVideoStop = self._createEvent()
        self.onIntroVideoLoaded = self._createEvent()
        self.onIntroVideoGoNext = self._createEvent()
        self.onUIStateChanged = self._createEvent()
        self.onBattleAction = self._createEvent()
        self.onArenaLoadCompleted = self._createEvent()
        self.onGarageLessonFinished = self._createEvent()
        self.onBattleLessonFinished = self._createEvent()
        self.onRequestBootcampFinish = self._createEvent()
        self.onBattleLoaded = self._createEvent()
        self.onBattleNotReady = self._createEvent()
        self.onBattleReady = self._createEvent()
        self.onResultScreenFinished = self._createEvent()
        self.onComponentAppear = self._createEvent()
        self.onBCGUIComponentLifetime = self._createEvent()
        self.onBattleComponentVisibility = self._createEvent()
        self.onRequestChangeResearchButtonState = self._createEvent()
        self.onRequestChangeVehiclePreviewBuyButtonState = self._createEvent()
        self.onRequestBootcampMessageWindowClose = self._createEvent()
        self.onHangarDispose = self._createEvent()

    def destroy(self):
        self.__manager.clear()

    def _createEvent(self):
        return Event.Event(self.__manager)


g_bootcampEvents = _BootCampEvents()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\BootCampEvents.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:44 Støední Evropa (letní èas)
