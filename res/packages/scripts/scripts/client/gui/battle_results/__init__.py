# 2017.08.29 21:44:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/battle_results/__init__.py
from gui.battle_results.service import BattleResultsService
from gui.battle_results.context import RequestResultsContext
from gui.battle_results.context import RequestEmblemContext
from gui.battle_results.settings import EMBLEM_TYPE
from skeletons.gui.battle_results import IBattleResultsService
__all__ = ('getBattleResultsServiceConfig', 'RequestResultsContext', 'RequestEmblemContext', 'EMBLEM_TYPE')

def getBattleResultsServiceConfig(manager):
    """Configures services for package battle_results.
    :param manager: helpers.dependency.DependencyManager
    """
    instance = BattleResultsService()
    instance.init()
    manager.addInstance(IBattleResultsService, instance, finalizer='fini')
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_results\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:40 Støední Evropa (letní èas)
