# 2017.08.29 21:43:06 Støední Evropa (letní èas)
# Embedded file name: scripts/client/services_config.py
__all__ = ('getClientServicesConfig',)

def getClientServicesConfig(manager):
    """ Configures services on client.
    :param manager: helpers.dependency.DependencyManager
    """
    import account_helpers
    import connection_mgr
    import gui
    import helpers
    from skeletons.connection_mgr import IConnectionManager
    manager.addInstance(IConnectionManager, connection_mgr.ConnectionManager(), finalizer='fini')
    manager.addConfig(gui.getGuiServicesConfig)
    manager.addConfig(account_helpers.getAccountHelpersConfig)
    manager.addConfig(helpers.getHelperServicesConfig)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\services_config.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:06 Støední Evropa (letní èas)
