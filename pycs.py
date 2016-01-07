#!/usr/bin/env python2
# PyCS.py | Richard Nedbalek 2016
# pyqt gui for sending commands to multiple consoles/terminals
# inspired by windows putty command sender

import sys
import subprocess
from PyQt4 import QtGui, QtCore

# TODO regex this!
tinfo="xwininfo -root -tree |grep -i XTerm |grep -vE '@wrk|VIM' |awk '{print $1,$2}'"
terms="xwininfo -root -tree |grep -i XTerm |grep -vE '@wrk|VIM' |awk '{print $1}'"

class handling():
    def __init__(self):
        "self"
    def f_err(self,text):
        print "err: %s" % text
    def f_ok(self,text):
        print "ok: %s" % text
    def f_inf(self,text):
        print "inf: %s" % text
    def f_exec(self,cmd):
            # execute cmd
            print cmd
            p = subprocess.Popen(cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
            out=p.communicate()
            return(out)

    def f_submit(self,payload,window):
        if not payload or not window:
            handling().f_err("payload or window empty")
        else:
            # set_layout = "setxkbmap us"
            win_activate = "xdotool windowactivate %s" % (window)
            self.f_exec(win_activate)
            win_focus = "xdotool windowfocus %s" % (window)
            self.f_exec(win_focus)
            win_payload = "xdotool type '%s'" % (payload)
            self.f_exec(win_payload)
            win_enter = "xdotool key KP_Enter"
            self.f_exec(win_enter)
            print

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # self.setGeometry(50, 50, 500, 250)
        self.setFixedSize(500, 260)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("PyCS.py | Python [terminal] Command Sender")
        self.f_home()

    def f_prgBarInc(self,prgstep):
        self.progress.setValue(prgstep)

    def f_preSend(self):
        prgstep = 0
        term_ids = ' '.join(handling().f_exec(terms)[0].split("\n")).split()
        self.progress.setMaximum(len(term_ids))
        for window in term_ids:
            prgstep += 1
            handling().f_submit(self.inputbox.toPlainText(),window)
            self.f_prgBarInc(prgstep)
        self.inputbox.clear()
        self.progress.setValue(100)

    def f_home(self):
        # editable textbox
        self.inputbox = QtGui.QTextEdit(self)
        self.inputbox.setGeometry(QtCore.QRect(0,40,500,205))

        # button: send 
        btn_send = QtGui.QPushButton("Send", self)
        # btn_send.setStyleSheet("border: solid 5px")
        btn_send.setShortcut("Ctrl+S")
        btn_send.clicked.connect(self.f_preSend)
        btn_send.resize(80,30)
        btn_send.move(15,4)

        # button: clear
        btn_clr = QtGui.QPushButton("Clear", self)
        btn_clr.setShortcut("Ctrl+R")
        btn_clr.clicked.connect(self.inputbox.clear)
        btn_clr.resize(80,30)
        btn_clr.move(97,4)
        
        # button: list terminals TODO maybe?
        # btn_list = QtGui.QPushButton("List terms", self)
        # btn_list.clicked.connect(lambda: handling().f_listWindows())
        # btn_list.resize(80,30)
        # btn_list.move(179,4)

        # button: quit
        btn_quit = QtGui.QPushButton("Quit", self)
        btn_quit.setShortcut("Ctrl+Q")
        btn_quit.clicked.connect(sys.exit)
        btn_quit.resize(80,30)
        btn_quit.move(401,4)

        # progressbar
        # TODO no text
        self.progress = QtGui.QProgressBar(self)
        # self.progress.setGeometry(2, 244, 493, 15)
        self.progress.setTextVisible(0)
        self.progress.setGeometry(2, 248, 493, 10)
        self.progress.setMinimum(0)

        # show all
        self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
