# 2017.08.29 21:54:14 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/md5.py
import warnings
warnings.warn('the md5 module is deprecated; use hashlib instead', DeprecationWarning, 2)
from hashlib import md5
new = md5
blocksize = 1
digest_size = 16
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\md5.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:54:14 Støední Evropa (letní èas)
