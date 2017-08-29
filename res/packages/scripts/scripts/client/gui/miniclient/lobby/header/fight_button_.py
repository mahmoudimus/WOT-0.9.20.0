# 2017.08.29 21:45:14 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/header/fight_button_.py
from helpers import aop
from CurrentVehicle import g_currentVehicle

class _DisableFightButtonAspect(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config['vehicle_is_available']
        aop.Aspect.__init__(self)

    def atCall(self, cd):
        if g_currentVehicle.isPresent() and not self.__vehicle_is_available(g_currentVehicle.item):
            cd.change()
            original_args = list(cd.args)
            original_args[0] = True
            return (original_args, cd.kwargs)


class DisableFightButtonPointcut(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.LobbyHeader', 'LobbyHeader', 'as_disableFightButtonS', aspects=(_DisableFightButtonAspect(config),))


class DisableTrainingFightButtonPointcut(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.trainings.TrainingRoom', 'TrainingRoom', 'as_disableStartButtonS', aspects=(_DisableFightButtonAspect(config),))


class _DisableBattlesForHiddenVehiclesAspect(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config['vehicle_is_available']
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        if not self.__vehicle_is_available(cd.self):
            cd.change()
            return False


class DisableBattlesForHiddenVehicles(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.shared.gui_items.Vehicle', 'Vehicle', 'isReadyToPrebattle', aspects=(_DisableBattlesForHiddenVehiclesAspect(config),))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\header\fight_button_.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:14 Støední Evropa (letní èas)
