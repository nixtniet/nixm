# This file is placed in the Public Domain.


"uptime"


import time


from ..command import elapsed
from ..timer   import STARTTIME


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
