# PyCS - Python Command Sender
A Python3/Qt4 GUI tool for sending commands/strings to multiple windows at once. You are not limited to terminals, although this is undeniably primary focus of PyCS. Use `xwininfo -root -tree -all` to find the name of your app & edit `termapp` variable at top of the script to your liking.

download here : [debian/ubuntu](http://ra.0x.no/pycs/pycs-0.9.deb)

![pcs](http://i.imgur.com/zCvXyK1.gif)

##### Ø keyboard shortcuts

* Ctrl + s  | Send commands
* Ctrl + r  | Clear textbox
* Ctrl + q  | Quit

##### Ø requirements 
* python3 pyqt4 pil xlib tkinter	 { debian: # aptitude install python3 python3-qt4 python3-pil python3-xlib python3-tk }
* pyautogui, ewmh { # pip3 install pyautogui ewmh --user}

#####  Ø todo
* history of sent data dropdown menu
* ctrl-c, ctrl-d buttons
