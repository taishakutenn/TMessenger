from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messenger(object):
    def setupUi(self, Messenger):
        super().__init__()

        Messenger.setObjectName("Messenger")
        Messenger.resize(950, 600)
        self.widget = QtWidgets.QWidget(Messenger)
        self.widget.setGeometry(QtCore.QRect(0, 0, 950, 600))
        self.widget.setObjectName("widget")
        self.back = QtWidgets.QLabel(self.widget)
        self.back.setGeometry(QtCore.QRect(0, 0, 950, 600))
        self.back.setStyleSheet("border-image: url(:/imagies/wallpapersden.com_windows-11-black_3840x2400.jpg);\n"
                                "border -radius: 20px;")
        self.back.setText("")
        self.back.setObjectName("back")
        self.chatsbar = QtWidgets.QWidget(self.widget)
        self.chatsbar.setGeometry(QtCore.QRect(0, 59, 260, 540))
        self.chatsbar.setObjectName("chatsbar")
        self.Chats = QtWidgets.QScrollArea(self.chatsbar)
        self.Chats.setGeometry(QtCore.QRect(-10, 0, 271, 551))
        self.Chats.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
                                 "border-style: solid; \n"
                                 "border-width: 1px;")
        self.Chats.setWidgetResizable(True)
        self.Chats.setObjectName("Chats")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.Chats.setWidget(self.scrollAreaWidgetContents)
        self.main_zone = QtWidgets.QWidget(self.widget)
        self.main_zone.setGeometry(QtCore.QRect(260, 0, 691, 601))
        self.main_zone.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
                                     "border-style: solid; \n"
                                     "border-width: 1px;")
        self.main_zone.setObjectName("main_zone")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(-1, 0, 261, 60))
        self.widget_2.setObjectName("widget_2")
        self.menubar = QtWidgets.QLabel(self.widget_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 61))
        self.menubar.setStyleSheet("background-color: rgba(0, 0, 0, 150);\n"
                                   "border-style: solid; \n"
                                   "border-width: 1px;")
        self.menubar.setText("")
        self.menubar.setObjectName("menubar")
        self.bt_zone = QtWidgets.QFrame(self.widget_2)
        self.bt_zone.setGeometry(QtCore.QRect(0, 0, 131, 61))
        self.bt_zone.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bt_zone.setStyleSheet("QPushButton {\n"
                                   "background-color: rgba(0, 0, 0, 0);\n"
                                   "border: 2px solid rgba(0, 0, 0, 250);\n"
                                   "padding: 20px;\n"
                                   "font-size: 25px;\n"
                                   "color: rgba(255, 255, 255, 255);\n"
                                   "}")
        self.bt_zone.setObjectName("bt_zone")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bt_zone)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QPushButton(self.bt_zone)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setStyleSheet("border-image: url(:/imagies/free-icon-main-menu-7711100.png);")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.horizontalLayout.addWidget(self.menu)
        self.chat_add = QtWidgets.QPushButton(self.bt_zone)
        self.chat_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chat_add.setStyleSheet("border-image: url(:/imagies/chat.png);")
        self.chat_add.setText("")
        self.chat_add.setObjectName("chat_add")
        self.horizontalLayout.addWidget(self.chat_add)

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

        self.addFunctions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Messenger"))

    def addFunctions(self):
        self.chat_add.clicked.connect(lambda: self.addChat())

    # Попытка добавить окошко чата в список
    def addChat(self):
        # widget_chat = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        # widget_chat.setGeometry(QtCore.QRect(10, 0, 261, 51))
        # widget_chat.setStyleSheet("border: 2px solid rgba(0, 0, 0, 100);\n"
        #                                "border-radius: 10px;\n"
        #                                "")
        # widget_chat.setObjectName("widget_chat")
        # chat_name = QtWidgets.QLabel(self.widget_chat)
        # chat_name.setGeometry(QtCore.QRect(0, 0, 141, 21))
        # chat_name.setStyleSheet("color: rgba(255, 255, 255, 255)")
        # chat_name.setObjectName("chat_name")
        #
        # self.Chats.setWidget(widget_chat)

        print(0)

import rec

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Messenger = QtWidgets.QWidget()
    ui = Ui_Messenger()
    ui.setupUi(Messenger)
    Messenger.show()
    sys.exit(app.exec_())
