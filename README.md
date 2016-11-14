# PyCS - Python Command Sender
A Python3/Qt4 GUI tool for sending commands/strings to multiple windows at once. You are not limited to terminals, although this is undeniably primary focus of PyCS. Use `xwininfo -root -tree -all` to find the name of your app & edit `termapp` variable at top of the script to your liking.

![pcs](http://i.imgur.com/zCvXyK1.gif)

##### Ø keyboard shortcuts

* Ctrl + s  | Send commands
* Ctrl + r  | Clear textbox
* Ctrl + q  | Quit

##### Ø requirements 
* pyqt4	 { debian: # aptitude install python-qt4 }
* pyautogui { # pip3 install pyautogui}
* ewmh { # pip3 install ewmh}

#####  Ø todo
* history of sent data dropdown menu
* ctrl-c, ctrl-d buttons

##### Ø download packages

[debian](http://ra.0x.no/pycs/pycs-0.9.deb)
