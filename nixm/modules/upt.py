# This file is placed in the Public Domain.


"uptime"


import time


from ..cmnd  import STARTTIME
from ..utils import elapsed


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
