N I X M
=======


**NAME**


``nixm`` - NIXM


**SYNOPSIS**


|
| ``nixm <cmd> [key=val] [key==val]``
| ``nixm -cvaw [init=mod1,mod2]``
| ``nixm -d`` 
| ``nixm -s``
|

**DESCRIPTION**


``NIXM`` has all you need to program a unix cli program, such as disk
perisistence for configuration files, event handler to handle the
client/server connection, deferred exception handling to not crash
on an error, etc.

``NIXM`` allows for easy json save//load to/from disk of objects. It
provides an "clean namespace" Object class that only has dunder
methods, so the namespace is not cluttered with method names. This
makes storing and reading to/from json possible.

``NIXM`` is a demo bot, it can connect to IRC, fetch and display RSS
feeds, take todo notes, keep a shopping list and log text. You can
also copy/paste the service file and run it under systemd for 24/7
presence in a IRC channel.

``NIXM`` is Public Domain.


**INSTALL**


installation is done with pipx

|
| ``$ pipx install nixm``
| ``$ pipx ensurepath``
|
| <new terminal>
|
| ``$ nixm srv > nixm.service``
| ``$ sudo mv nixm.service /etc/systemd/system/``
| ``$ sudo systemctl enable nixm --now``
|
| joins ``#nixm`` on localhost
|


**USAGE**


use ``nixm`` to control the program, default it does nothing

|
| ``$ nixm``
| ``$``
|

see list of commands

|
| ``$ nixm cmd``
| ``cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,``
| ``pwd,rem,req,res,rss,srv,syn,tdo,thr,upt``
|

start console

|
| ``$ nixm -c``
|

start console and run irc and rss clients

|
| `` $ nixm -c init=irc,rss``
|

list available modules

|
| `` $ nixm mod``
| ``err,flt,fnd,irc,llm,log,mbx,mdl,mod,req,rss,rst,slg,tdo,thr,tmr,udp,upt``
|

start daemon

|
| ``$ nixm -d``
| ``$``
|

start service

|
| ``$ nixm -s``
| ``<runs until ctrl-c>``
|


**COMMANDS**


here is a list of available commands

|
| ``cfg`` - irc configuration
| ``cmd`` - commands
| ``dpl`` - sets display items
| ``err`` - show errors
| ``exp`` - export opml (stdout)
| ``imp`` - import opml
| ``log`` - log text
| ``mre`` - display cached output
| ``pwd`` - sasl nickserv name/pass
| ``rem`` - removes a rss feed
| ``res`` - restore deleted feeds
| ``req`` - reconsider
| ``rss`` - add a feed
| ``syn`` - sync rss feeds
| ``tdo`` - add todo item
| ``thr`` - show running threads
| ``upt`` - show uptime
|

**CONFIGURATION**


irc

|
| ``$ nixm cfg server=<server>``
| ``$ nixm cfg channel=<channel>``
| ``$ nixm cfg nick=<nick>``
|

sasl

|
| ``$ nixm pwd <nsvnick> <nspass>``
| ``$ nixm cfg password=<frompwd>``
|

rss

|
| ``$ nixm rss <url>``
| ``$ nixm dpl <url> <item1,item2>``
| ``$ nixm rem <url>``
| ``$ nixm nme <url> <name>``
|

opml

|
| ``$ nixm exp``
| ``$ nixm imp <filename>``
|


**PROGRAMMING**


``nixm`` runs it's modules in the package edit a file in nixm/modules/<name>.py
and add the following for ``hello world``

|
|    def hello(event):
|        event.reply("hello world !!")
|

save this and recreate the dispatch table

|
| ``$ nixm tbl > nixm/modules/tbl.py``
|

``nixm`` can execute the ``hello`` command now.

|
| ``$ nixm hello``
| ``hello world !!``
|


Commands run in their own thread and the program borks on exit, output gets
flushed on print so exceptions appear in the systemd logs. Modules can contain
your own written python3 code, see the nixbot/modules directory for examples.


**FILES**

|
| ``~/.nixm``
| ``~/.local/bin/nixm``
| ``~/.local/pipx/venvs/nixm/*``
|

**AUTHOR**

|
| ``Bart Thate`` <``nixtniet@gmail.com``>
|

**COPYRIGHT**

|
| ``NIXM`` is Public Domain.
|
