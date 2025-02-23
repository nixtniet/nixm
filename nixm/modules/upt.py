# This file is placed in the Public Domain.


"uptime"


import time


from nixt.locater import elapsed
from nixm.package import STARTTIME


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
