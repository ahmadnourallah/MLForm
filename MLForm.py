#!/usr/bin/python3
from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        # set fix size to gui
        Form.setFixedSize(346, 138)
        # set gui color
        Form.setStyleSheet(_fromUtf8("background-color: #2196F3"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 35))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        # make gui in the middle of screen
        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = Form.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        Form.move(hpos, vpos)
        ##
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        # define username label
        self.label = QtGui.QLabel(self.layoutWidget)
        # set lable text color
        self.label.setStyleSheet(_fromUtf8("color: white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        # define usrline lineedit
        self.usrline = QtGui.QLineEdit(self.layoutWidget)
        # set usrline lineedit background color and border style
        self.usrline.setStyleSheet(_fromUtf8("background-color: white; border: 2px solid #0277BD; border-radius: 12px;"))
        self.usrline.setObjectName(_fromUtf8("usrline"))
        self.horizontalLayout.addWidget(self.usrline)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 52, 311, 35))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        # define password label
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        # set lable text color
        self.label_2.setStyleSheet(_fromUtf8("color: white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        # define Password lineedit
        self.passline = QtGui.QLineEdit(self.layoutWidget1)
        # set Password lineedit background color and border style
        self.passline.setStyleSheet(_fromUtf8("background-color: white; border: 2px solid #0277BD; border-radius: 12px;"))
        self.passline.setObjectName(_fromUtf8("passline"))
        self.passline.setEchoMode(QtGui.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.passline)
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 100, 178, 33))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        # define ok pushbutton
        self.okbtn = QtGui.QPushButton(self.layoutWidget2)
        # set ok pushbutton style
        self.okbtn.setStyleSheet(_fromUtf8("QPushButton {background-color: #263238; color: white; } \n"
"QPushButton:pressed {background-color: #03A9F4}"))
        self.okbtn.setObjectName(_fromUtf8("okbtn"))
        self.horizontalLayout_3.addWidget(self.okbtn)
        # define Cancel pushbutton
        self.canbtn = QtGui.QPushButton(self.layoutWidget2)
        # set ok pushbutton style
        self.canbtn.setStyleSheet(_fromUtf8("QPushButton {background-color: #263238; color: white; } \n"
"QPushButton:pressed {background-color: #03A9F4}"))
        self.canbtn.setObjectName(_fromUtf8("canbtn"))
        self.horizontalLayout_3.addWidget(self.canbtn)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # set clicked signal for object
        self.okbtn.clicked.connect(self.check)
        # set clicked signal for object
        self.canbtn.clicked.connect(self.checkexit)
    # set obejcts texts
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Username", None))
        self.label_2.setText(_translate("Form", "Password", None))
        self.okbtn.setText(_translate("Form", "OK", None))
        self.canbtn.setText(_translate("Form", "Cancel", None))
    ##
    # check password and username function
    def check(self):
        if self.usrline.text() == 'ahmad' and self.passline.text() == 'password':
            self.msg = QtGui.QMessageBox()
            self.msg.setIcon(QtGui.QMessageBox.Information)
            self.msg.setText("Hello "+self.usrline.text())
            self.msg.setWindowTitle("Login Successful")
            self.msg.setStandardButtons(QtGui.QMessageBox.Cancel)
            self.msg.show()
        else:
            self.msg = QtGui.QMessageBox()
            self.msg.setIcon(QtGui.QMessageBox.Warning)
            self.msg.setText("Sorry "+self.usrline.text()+" You didn't sign up")
            self.msg.setWindowTitle("Login Failed")
            self.msg.setStandardButtons(QtGui.QMessageBox.Cancel)
            self.msg.show()
    # exit check function
    def checkexit(self):
            ask = QtGui.QMessageBox.question(None, "Confirm Remove",
                            "Are you sure you want to quit?",
                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if ask == QtGui.QMessageBox.Yes:
                QtGui.QApplication.quit()
            else:
                pass
# handle ctrl+c keys
def sigint_handler(*args):
    """Handler for the SIGINT signal."""
    sys.stderr.write('\r')
    ask = QtGui.QMessageBox.question(None, "Exit Confirm",
                    "Are you sure you want to quit?",
                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    if ask == QtGui.QMessageBox.Yes:
        QtGui.QApplication.quit()
    else:
        pass

if __name__ == "__main__":
    import sys
    import signal
    signal.signal(signal.SIGINT, sigint_handler)
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    timer = QtCore.QTimer()
    timer.start(500)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    timer.timeout.connect(lambda: None)
    sys.exit(app.exec_())
