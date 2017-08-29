# 2017.08.29 21:51:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/skeletons/gui/system_messages.py


class ISystemMessages(object):

    def init(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def pushMessage(self, text, type, priority = None, messageData = None):
        """
        Push system message
        
        :param text: message's body text
        :param type: message's type
        :param priority: message's priority
        :param messageData: dict, contains data for keywords replacement in notification's templates
        """
        raise NotImplementedError

    def pushI18nMessage(self, key, *args, **kwargs):
        """
        Push localized system message using i18n-key
        
        :param key: i18n-key
        :param args: contains data for keywords replacement in localized text
        :param kwargs: contains different data such as notification type, priority and
                       data for keywords replacement in localized text and
                       data for keywords replacement in notification's templates (messageData)
        """
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\gui\system_messages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:39 Støední Evropa (letní èas)
