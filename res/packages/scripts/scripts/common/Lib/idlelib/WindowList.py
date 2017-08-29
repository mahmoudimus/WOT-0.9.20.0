# 2017.08.29 21:57:10 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/idlelib/WindowList.py
from Tkinter import *

class WindowList:

    def __init__(self):
        self.dict = {}
        self.callbacks = []

    def add(self, window):
        window.after_idle(self.call_callbacks)
        self.dict[str(window)] = window

    def delete(self, window):
        try:
            del self.dict[str(window)]
        except KeyError:
            pass

        self.call_callbacks()

    def add_windows_to_menu(self, menu):
        list = []
        for key in self.dict.keys():
            window = self.dict[key]
            try:
                title = window.get_title()
            except TclError:
                continue

            list.append((title, window))

        list.sort()
        for title, window in list:
            menu.add_command(label=title, command=window.wakeup)

    def register_callback(self, callback):
        self.callbacks.append(callback)

    def unregister_callback(self, callback):
        try:
            self.callbacks.remove(callback)
        except ValueError:
            pass

    def call_callbacks(self):
        for callback in self.callbacks:
            try:
                callback()
            except:
                print 'warning: callback failed in WindowList',
                print sys.exc_type, ':', sys.exc_value


registry = WindowList()
add_windows_to_menu = registry.add_windows_to_menu
register_callback = registry.register_callback
unregister_callback = registry.unregister_callback

class ListedToplevel(Toplevel):

    def __init__(self, master, **kw):
        Toplevel.__init__(self, master, kw)
        registry.add(self)
        self.focused_widget = self

    def destroy(self):
        registry.delete(self)
        Toplevel.destroy(self)
        if not registry.dict:
            self.quit()

    def update_windowlist_registry(self, window):
        registry.call_callbacks()

    def get_title(self):
        return self.wm_title()

    def wakeup(self):
        try:
            if self.wm_state() == 'iconic':
                self.wm_withdraw()
                self.wm_deiconify()
            self.tkraise()
            self.focused_widget.focus_set()
        except TclError:
            pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\WindowList.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:57:10 St�edn� Evropa (letn� �as)
