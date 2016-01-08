# PyCS - Python Command Sender
A Python/Qt4 GUI tool for sending data { mostly commands & short strings } to multiple terminal windows at once

![pcs](http://i.imgur.com/zCvXyK1.gif)


<b> Ø keyboard shortcuts</b>
```
Ctrl + s	Send commands
Ctrl + c	Clear textbox
Ctrl + q	Quit
```
<b> Ø requirements </b>
```
xdotool  ( debian: # aptitude install xdotool )
xwininfo ( debian: # aptitude install x11-utils )
pyqt4	 ( debian: # aptitude install python-qt4 )
```
<b> Ø gotchas </b>

you cannot send simple quotes ' ' for now. use double quotes " " instead

<b> Ø todo </b>
* get rid of xdotool/xwinfo and use xlib
* history of sent data


