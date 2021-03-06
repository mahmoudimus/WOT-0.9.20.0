# 2017.08.29 21:51:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/skeletons/account_helpers/settings_core.py


class ISettingsCache(object):
    onSyncStarted = None
    onSyncCompleted = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    @property
    def waitForSync(self):
        raise NotImplementedError

    @property
    def settings(self):
        raise NotImplementedError

    def update(self, callback = None):
        raise NotImplementedError

    def getSectionSettings(self, section, defaultValue = 0):
        raise NotImplementedError

    def setSectionSettings(self, section, value):
        raise NotImplementedError

    def setSettings(self, settings):
        raise NotImplementedError

    def getSetting(self, key, defaultValue = 0):
        raise NotImplementedError

    def getVersion(self, defaultValue = 0):
        raise NotImplementedError

    def setVersion(self, value):
        raise NotImplementedError


class ISettingsCore(object):
    onSettingsChanged = None
    onSettingsApplied = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    @property
    def options(self):
        raise NotImplementedError

    @property
    def storages(self):
        raise NotImplementedError

    @property
    def interfaceScale(self):
        raise NotImplementedError

    @property
    def serverSettings(self):
        raise NotImplementedError

    def packSettings(self, names):
        raise NotImplementedError

    def getSetting(self, name):
        raise NotImplementedError

    def getApplyMethod(self, diff):
        raise NotImplementedError

    def applySetting(self, key, value):
        raise NotImplementedError

    def previewSetting(self, name, value):
        raise NotImplementedError

    def applySettings(self, diff):
        raise NotImplementedError

    def revertSettings(self):
        raise NotImplementedError

    def isSettingChanged(self, name, value):
        raise NotImplementedError

    def applyStorages(self, restartApproved):
        raise NotImplementedError

    def confirmChanges(self, confirmators):
        raise NotImplementedError

    def clearStorages(self):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\account_helpers\settings_core.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:37 St�edn� Evropa (letn� �as)
