#!/usr/bin/env python2
# PyTCS.py | 2016
# GUI for sending commands to multiple consoles/terminals
# inspired by windows putty command sender

import sys
import subprocess
from PyQt4 import QtGui, QtCore

class Handling():
    def __init__(self):
        "self"
    def f_exec(cmd):
            # execute cmd
            print cmd
            p = subprocess.Popen(cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
            out=p.communicate()

    def f_listWindows():
        wlist_cmd="xwininfo -root -tree |grep -i xterm |grep -v \"@wrk\" |awk -F\( '{print $1}' |awk -F: '{print $1}'"
        window_list = subprocess.Popen(wlist_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell = True)
        win_details = window_list.communicate()
        return win_details

    def f_submit(self,payload):
        print payload

    def f_showtext(self):        
        print "show input: %s" % Window().inputbox.toPlainText()
        print "tst"
 
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # self.setGeometry(50, 50, 500, 250)
        self.setFixedSize(500, 260)
        self.setWindowTitle("PytCS.py | Python Terminal Command Sender")
        self.f_home()

    def showtext(self):
        print Window().inputbox.toPlainText()

    def f_home(self):
        self.inputbox = QtGui.QTextEdit(self)
        self.inputbox.setGeometry(QtCore.QRect(0,40,500,200))

        btn_send = QtGui.QPushButton("Send", self)
        # btn_send.setStyleSheet("border: solid 5px")
        btn_send.setShortcut("Ctrl+S")
        btn_send.clicked.connect(self.showtext)
        btn_send.resize(80,30)
        btn_send.move(15,4)

        btn_pwd = QtGui.QPushButton("Pwd", self)
        btn_pwd.clicked.connect(sys.exit)
        btn_pwd.resize(80,30)
        btn_pwd.move(97,4)

        btn_list = QtGui.QPushButton("List terms", self)
        btn_list.clicked.connect(sys.exit)
        btn_list.resize(80,30)
        btn_list.move(179,4)

        btn_quit = QtGui.QPushButton("Quit", self)
        btn_quit.clicked.connect(sys.exit)
        btn_quit.resize(80,30)
        btn_quit.move(401,4)

        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
