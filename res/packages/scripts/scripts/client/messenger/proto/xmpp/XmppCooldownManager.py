# 2017.08.29 21:51:19 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/xmpp/XmppCooldownManager.py
from gui.shared.rq_cooldown import RequestCooldownManager, REQUEST_SCOPE
from messenger.proto.shared_errors import I18nActionID

class XmppCooldownManager(RequestCooldownManager):

    def __init__(self, default = 1.0):
        super(XmppCooldownManager, self).__init__(REQUEST_SCOPE.XMPP)
        self.__default = default

    def lookupName(self, rqTypeID):
        return I18nActionID(rqTypeID).getI18nName()

    def getDefaultCoolDown(self):
        return self.__default
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\xmpp\XmppCooldownManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:19 Støední Evropa (letní èas)
