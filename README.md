# pycs
Python Command Sender
A Python/Qt4 GUI tool for sending data { mostly commands; short strings } to multiple terminal windows

![alt tag](http://i.imgur.com/5K72pUA.png)


# keyboard shortcuts
```
Ctrl + s	Send commands
Ctrl + c	Clear textbox
Ctrl + q	Quit
```
# requirements
```
xdotool  ( debian: # aptitude install xdotool )
xwininfo ( debian: # aptitude install x11-utils )
pyqt4	 ( debian: # aptitude install python-qt4 )
```
# gotchas
you cannot send simple quotes '' for now. use double quotes "" instead
