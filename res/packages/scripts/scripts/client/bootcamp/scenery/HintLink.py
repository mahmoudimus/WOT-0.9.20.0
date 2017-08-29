# 2017.08.29 21:43:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/scenery/HintLink.py


class HintLink(object):

    def __init__(self, hintTypeId, timeCompleted, cooldownAfter, message, startDelay, duration, innerCooldown, completeDuration, voiceover):
        self.hintTypeId = hintTypeId
        self.timeCompleted = timeCompleted
        self.cooldownAfter = cooldownAfter
        self.message = message
        self.voiceover = voiceover
        self.timeStartDelay = startDelay
        self.timeDuration = duration
        self.timeInnerCooldown = innerCooldown
        self.timeCompleteDuration = completeDuration
        self.hintObject = None
        return

    def show(self):
        if self.hintObject is not None:
            self.hintObject.show()
        return

    def hide(self):
        if self.hintObject is not None:
            self.hintObject.hide()
        return

    def complete(self):
        if self.hintObject is not None:
            self.hintObject.complete()
        return

    def disable(self):
        if self.hintObject is not None:
            self.hintObject.disable()
        return

    isVisible = property(lambda self: (self.hintObject.isVisible() if self.hintObject is not None else False))
    isActive = property(lambda self: (self.hintObject.isActive() if self.hintObject is not None else False))
    isNotShown = property(lambda self: (self.hintObject.isNotShown() if self.hintObject is not None else False))
    isComplete = property(lambda self: (self.hintObject.isComplete() if self.hintObject is not None else False))
    isDisabled = property(lambda self: (self.hintObject.isDisabled() if self.hintObject is not None else False))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\scenery\HintLink.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:53 Støední Evropa (letní èas)
