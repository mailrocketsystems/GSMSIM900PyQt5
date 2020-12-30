import sys
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.app_ui import Ui_MainWindow
from pyembedded.gsm_module.gsm import GSM


curr_path = os.path.dirname(os.path.abspath(__file__))


class APP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        make_call_icon_path = os.path.join(curr_path, 'ui', 'make_call.PNG')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(make_call_icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.make_call_btn.setIcon(icon)

        end_call_icon_path = os.path.join(curr_path, 'ui', 'end_call.PNG')
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(end_call_icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.end_call_btn.setIcon(icon2)

        self.phone_number = ""
        self.phone = GSM(port='COM4', baud_rate=9600)

        self.ui.pushButton_0.clicked.connect(self.btn0)
        self.ui.pushButton_1.clicked.connect(self.btn1)
        self.ui.pushButton_2.clicked.connect(self.btn2)
        self.ui.pushButton_3.clicked.connect(self.btn3)
        self.ui.pushButton_4.clicked.connect(self.btn4)
        self.ui.pushButton_5.clicked.connect(self.btn5)
        self.ui.pushButton_6.clicked.connect(self.btn6)
        self.ui.pushButton_7.clicked.connect(self.btn7)
        self.ui.pushButton_8.clicked.connect(self.btn8)
        self.ui.pushButton_9.clicked.connect(self.btn9)

        self.ui.make_call_btn.clicked.connect(self.make_call)
        self.ui.end_call_btn.clicked.connect(self.end_call)

        self.ui.send_sms_btn.clicked.connect(self.send_sms)
        self.ui.clear_sms.clicked.connect(self.clear_sms_event)

    def send_sms(self):
        sms_number = self.phone_number
        sms_number = "+91" + sms_number
        sms_number = sms_number.replace(" ", "")
        msg_content = self.ui.textEdit.toPlainText()
        sms_res = self.phone.send_sms(number=sms_number, message=str(msg_content))
        print(sms_res)
        self.ui.sms_status_label.setText(sms_res[1])

    def clear_sms_event(self):
        self.ui.textEdit.setText(" ")

    def make_call(self):
        number_to_dial = self.phone_number
        call_res = self.phone.make_call(number=number_to_dial)
        print(call_res)
        self.ui.call_status_label.setText("Calling....")

    def end_call(self):
        res = self.phone.end_ongoing_call()
        self.ui.call_status_label.setText("Call Cancelled")
        print(res)

    def btn0(self):
        self.phone_number = self.phone_number + "0"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn1(self):
        self.phone_number = self.phone_number + "1"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn2(self):
        self.phone_number = self.phone_number + "2"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn3(self):
        self.phone_number = self.phone_number + "3"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn4(self):
        self.phone_number = self.phone_number + "4"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn5(self):
        self.phone_number = self.phone_number + "5"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn6(self):
        self.phone_number = self.phone_number + "6"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn7(self):
        self.phone_number = self.phone_number + "7"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn8(self):
        self.phone_number = self.phone_number + "8"
        self.ui.lineEdit.setText(str(self.phone_number))

    def btn9(self):
        self.phone_number = self.phone_number + "9"
        self.ui.lineEdit.setText(str(self.phone_number))


app = QApplication(sys.argv)
main_window = APP()
main_window.show()
sys.exit(app.exec_())