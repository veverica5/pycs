# PyCS - Python Command Sender
A Python/Qt4 GUI tool for sending data { mostly commands & short strings } to multiple terminal windows at once

![vid](https://u.pomf.is/fiugzr.webm)


<b> :: keyboard shortcuts</b>
```
Ctrl + s	Send commands
Ctrl + c	Clear textbox
Ctrl + q	Quit
```
<b> :: requirements </b>
```
xdotool  ( debian: # aptitude install xdotool )
xwininfo ( debian: # aptitude install x11-utils )
pyqt4	 ( debian: # aptitude install python-qt4 )
```
<b> :: gotchas </b>

you cannot send simple quotes ' ' for now. use double quotes " " instead
