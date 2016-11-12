#!/usr/bin/env python3
# PyCS.py | Richard Nedbalek 2016
# pyqt gui for sending commands to multiple consoles/terminals
# requirements: pyqt4 pyautogui ewmh

import time
import sys
from PyQt4 import QtGui, QtCore
import ewmh
from pyautogui import typewrite as pya
from pyautogui import hotkey as hotkey

##  what terminals/windows will we look for?
#   we can output to any window that accepts text input
#   most common terminals are listed below, just uncomment the one that you use
#   if your terminal is not listed below, use xwininfo -root -tree -all to determine the app name 

termapp = "Gnome-terminal"
# termapp = "Mate-terminal"
# termapp = "XTerm"

class Tools(object):
    """Helper functions definition"""
	
    def __init__(self):
        pass

    def getTermWindows():
        """Returns window objects which satisfy criterion defined in _termapp_ variable"""
        wlist = []
        windows = ew.getClientList()
        for window in windows:
            if termapp in window.get_wm_class():
                wlist.append(window)
        return(wlist)

    def submitPayload(self, payload, window):
        """fn sends qt textbox defined _payload_ to a target _window_"""
		
        print(window, payload)
        if not payload or not window:
            print("err: payload or window empty")
        else:
            ew.setActiveWindow(window)
            ew.display.flush()
            time.sleep(0.1)
            pya(payload)

class Window(QtGui.QMainWindow):
    """qt window parameters definition"""

    def __init__(self):
        super(Window, self).__init__()
        # self.setGeometry(50, 50, 500, 250)
        self.setFixedSize(500, 260)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("PyCS.py | Python [terminal] Command Sender")
        self.home()

    def f_prgBarInc(self, current_prgbar_value):
        """progressbar step fn """
        self.progress.setValue(current_prgbar_value)

    def f_preSend(self):
        windows = Tools.getTermWindows()
        current_prgbar_value = 0
        if len(windows) > 0:
            prgmax = len(windows)
        else:
            prgmax = 1
        self.progress.setMaximum(prgmax)
        for window in windows:
            current_prgbar_value += 1
            self.f_prgBarInc(current_prgbar_value)
            # h = Tools()
            Tools().submitPayload(self.inputbox.toPlainText(), window)
        self.inputbox.clear()
        self.progress.setValue(100)

    def home(self):
        """fn defines homescreen buttons & progressbar size/position/text/shortcut"""
        # editable textbox
        self.inputbox = QtGui.QTextEdit(self)
        self.inputbox.setGeometry(QtCore.QRect(0, 40, 500, 205))

        # button: send
        btn_send = QtGui.QPushButton("Send", self)
        btn_send.setShortcut("Ctrl+S")
        btn_send.clicked.connect(self.f_preSend)
        btn_send.resize(80, 30)
        btn_send.move(15, 4)

        # button: clear
        btn_clr = QtGui.QPushButton("Clear", self)
        btn_clr.setShortcut("Ctrl+R")
        btn_clr.clicked.connect(self.inputbox.clear)
        btn_clr.resize(80, 30)
        btn_clr.move(97, 4)

        # button: quit
        btn_quit = QtGui.QPushButton("Quit", self)
        btn_quit.setShortcut("Ctrl+Q")
        btn_quit.clicked.connect(sys.exit)
        btn_quit.resize(80, 30)
        btn_quit.move(401, 4)

        # draw progressbar
        self.progress = QtGui.QProgressBar(self)
        
        # self.progress.setGeometry(2, 244, 493, 15)
        self.progress.setTextVisible(0)
        self.progress.setGeometry(2, 248, 493, 10)
        self.progress.setMinimum(0)

        # show all
        self.show()

def run():
    global ew
    ew = ewmh.EWMH()
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

    
        

