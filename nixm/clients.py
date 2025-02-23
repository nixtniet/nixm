# This file is placed in the Public Domain.


"clients"


import os


from nixt.objects import Default
from nixt.reactor import Fleet, Reactor


from nixm.command import command


class Config(Default):

    init    = ""
    name    = __file__.rsplit(os.sep, maxsplit=2)[-2]
    opts    = Default()


class Client(Reactor):

    def __init__(self):
        Reactor.__init__(self)
        Fleet.add(self)
        self.register("command", command)

    def announce(self, txt):
        pass

    def raw(self, txt) -> None:
        raise NotImplementedError("raw")

    def say(self, channel, txt) -> None:
        self.raw(txt)


def __dir__():
    return (
        'Client',
        'Config'
    )
