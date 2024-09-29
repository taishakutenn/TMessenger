# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_intarface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messenger(object):
    def setupUi(self, messenger):
        messenger.setObjectName("messenger")
        messenger.resize(900, 575)
        messenger.setStyleSheet("background-color: rgb(139, 139, 139);")
        self.centralwidget = QtWidgets.QWidget(messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chat_menu = QtWidgets.QFrame(self.centralwidget)
        self.chat_menu.setEnabled(True)
        self.chat_menu.setMinimumSize(QtCore.QSize(300, 400))
        self.chat_menu.setMaximumSize(QtCore.QSize(300, 16777215))
        self.chat_menu.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.chat_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chat_menu.setObjectName("chat_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.chat_menu)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_zone_2 = QtWidgets.QFrame(self.chat_menu)
        self.button_zone_2.setMinimumSize(QtCore.QSize(0, 60))
        self.button_zone_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.button_zone_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_zone_2.setStyleSheet("QFrame {\n"
                                         "    background-color: rgb(211, 211, 211);\n"
                                         "    border-radius: 10;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton { \n"
                                         "    border: 1px solid black;\n"
                                         "    border-radius: 10px;\n"
                                         "    padding: 100;\n"
                                         "    background-color: rgba(255, 255, 255,0);\n"
                                         "}\n"
                                         "")
        self.button_zone_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_zone_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_zone_2.setObjectName("button_zone_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.button_zone_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.menu_button = QtWidgets.QPushButton(self.button_zone_2)
        self.menu_button.setMaximumSize(QtCore.QSize(60, 60))
        self.menu_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.menu_button.setBaseSize(QtCore.QSize(0, 0))
        self.menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_button.setStyleSheet("")
        self.menu_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-menu-button-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setObjectName("menu_button")
        self.horizontalLayout_7.addWidget(self.menu_button)
        self.add_chat_button = QtWidgets.QPushButton(self.button_zone_2)
        self.add_chat_button.setMaximumSize(QtCore.QSize(60, 60))
        self.add_chat_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_chat_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons8-chat-room-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_chat_button.setIcon(icon1)
        self.add_chat_button.setObjectName("add_chat_button")
        self.horizontalLayout_7.addWidget(self.add_chat_button)
        self.search_zone_open_button = QtWidgets.QPushButton(self.button_zone_2)
        self.search_zone_open_button.setMaximumSize(QtCore.QSize(60, 60))
        self.search_zone_open_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_zone_open_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_zone_open_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_zone_open_button.setIcon(icon2)
        self.search_zone_open_button.setObjectName("search_zone_open_button")
        self.horizontalLayout_7.addWidget(self.search_zone_open_button)
        self.verticalLayout.addWidget(self.button_zone_2)
        self.search_zone = QtWidgets.QFrame(self.chat_menu)
        self.search_zone.setMaximumSize(QtCore.QSize(16777215, 0))
        self.search_zone.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                       "border-radius: 10;")
        self.search_zone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_zone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_zone.setObjectName("search_zone")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.search_zone)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.search_text = QtWidgets.QLineEdit(self.search_zone)
        self.search_text.setMinimumSize(QtCore.QSize(0, 30))
        self.search_text.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_text.setFont(font)
        self.search_text.setStyleSheet("color: black;")
        self.search_text.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.search_text.setObjectName("search_text")
        self.horizontalLayout_8.addWidget(self.search_text)
        self.search_button = QtWidgets.QPushButton(self.search_zone)
        self.search_button.setMinimumSize(QtCore.QSize(50, 40))
        self.search_button.setMaximumSize(QtCore.QSize(40, 50))
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setStyleSheet("border: 1px solid black;\n"
                                         "border-radius: 10px;\n"
                                         "padding: 10;")
        self.search_button.setText("")
        self.search_button.setIcon(icon2)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_8.addWidget(self.search_button)
        self.verticalLayout.addWidget(self.search_zone)
        self.list_of_chats_zone = QtWidgets.QFrame(self.chat_menu)
        self.list_of_chats_zone.setAutoFillBackground(False)
        self.list_of_chats_zone.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                              "")
        self.list_of_chats_zone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_of_chats_zone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_of_chats_zone.setObjectName("list_of_chats_zone")
        self.none_layout = QtWidgets.QVBoxLayout(self.list_of_chats_zone)
        self.none_layout.setContentsMargins(0, 0, 0, 0)
        self.none_layout.setSpacing(0)
        self.none_layout.setObjectName("none_layout")
        self.scroll_list_of_chats = QtWidgets.QScrollArea(self.list_of_chats_zone)
        self.scroll_list_of_chats.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_list_of_chats.sizePolicy().hasHeightForWidth())
        self.scroll_list_of_chats.setSizePolicy(sizePolicy)
        self.scroll_list_of_chats.setAutoFillBackground(False)
        self.scroll_list_of_chats.setStyleSheet("QScrollBar:vertical {\n"
                                                "    background-color: rgb(76, 76, 76);\n"
                                                "}\n"
                                                "\n"
                                                "QScrollBar::sub-line:vertival {\n"
                                                "    border: none;\n"
                                                "    background-color: rgb(211, 211, 211);\n"
                                                "    border-top-left-radius: 5px;\n"
                                                "    border-top-right-radius: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QScrollBar::handle:vertical {\n"
                                                "    background-color: rgb(131, 131, 131);\n"
                                                "}\n"
                                                "\n"
                                                "")
        self.scroll_list_of_chats.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_list_of_chats.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_list_of_chats.setWidgetResizable(True)
        self.scroll_list_of_chats.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scroll_list_of_chats.setObjectName("scroll_list_of_chats")
        self.scroll_area_list_of_chats = QtWidgets.QWidget()
        self.scroll_area_list_of_chats.setEnabled(True)
        self.scroll_area_list_of_chats.setGeometry(QtCore.QRect(0, 0, 284, 489))
        self.scroll_area_list_of_chats.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                                     "border-radius: 10;")
        self.scroll_area_list_of_chats.setObjectName("scroll_area_list_of_chats")
        self.scroll_list_of_chats.setWidget(self.scroll_area_list_of_chats)
        self.none_layout.addWidget(self.scroll_list_of_chats)
        self.verticalLayout.addWidget(self.list_of_chats_zone)
        self.horizontalLayout.addWidget(self.chat_menu)
        self.click_chat = QtWidgets.QLabel(self.centralwidget)
        self.click_chat.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.click_chat.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.click_chat.setObjectName("click_chat")
        self.horizontalLayout.addWidget(self.click_chat)

        self.chats = QtWidgets.QFrame(self.centralwidget)
        self.chats.setMaximumSize(QtCore.QSize(0, 16777215))
        self.chats.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.chats.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chats.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chats.setObjectName("chats")

        self.gridLayout = QtWidgets.QGridLayout(self.chats)
        self.gridLayout.setObjectName("gridLayout")
        self.messages_zones = QtWidgets.QFrame(self.chats)
        self.messages_zones.setMinimumSize(QtCore.QSize(400, 150))
        self.messages_zones.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                          "border-radius: 10;")
        self.messages_zones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.messages_zones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.messages_zones.setObjectName("messages_zones")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.messages_zones)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.messages_zones)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 150))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scroll_message = QtWidgets.QWidget()
        self.scroll_message.setGeometry(QtCore.QRect(0, 0, 400, 489))
        self.scroll_message.setObjectName("scroll_message")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scroll_message)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.interlocutor_messages = QtWidgets.QFrame(self.scroll_message)
        self.interlocutor_messages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.interlocutor_messages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.interlocutor_messages.setObjectName("interlocutor_messages")
        self.horizontalLayout_6.addWidget(self.interlocutor_messages)
        self.owner_messages = QtWidgets.QFrame(self.scroll_message)
        self.owner_messages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.owner_messages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.owner_messages.setObjectName("owner_messages")
        self.horizontalLayout_6.addWidget(self.owner_messages)
        self.scrollArea.setWidget(self.scroll_message)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.messages_zones, 0, 0, 1, 1)
        self.send_zone = QtWidgets.QFrame(self.chats)
        self.send_zone.setMinimumSize(QtCore.QSize(0, 60))
        self.send_zone.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.send_zone.setFont(font)
        self.send_zone.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                     "border-radius: 10;")
        self.send_zone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.send_zone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.send_zone.setObjectName("send_zone")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.send_zone)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.message = QtWidgets.QTextEdit(self.send_zone)
        self.message.setMinimumSize(QtCore.QSize(0, 25))
        self.message.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message.setFont(font)
        self.message.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.message.setStyleSheet("border: none;")
        self.message.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.message.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.message.setUndoRedoEnabled(True)
        self.message.setObjectName("message")
        self.horizontalLayout_3.addWidget(self.message)
        self.button_zone = QtWidgets.QFrame(self.send_zone)
        self.button_zone.setMinimumSize(QtCore.QSize(0, 60))
        self.button_zone.setMaximumSize(QtCore.QSize(150, 60))
        self.button_zone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_zone.setStyleSheet("QPushButton { \n"
                                       "    border: 1px solid black;\n"
                                       "    border-radius: 10px;\n"
                                       "    padding: 10;\n"
                                       "}    ")
        self.button_zone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_zone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_zone.setObjectName("button_zone")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.button_zone)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.attachments_send = QtWidgets.QPushButton(self.button_zone)
        self.attachments_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.attachments_send.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/attach-clipboard-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attachments_send.setIcon(icon3)
        self.attachments_send.setObjectName("attachments_send")
        self.horizontalLayout_5.addWidget(self.attachments_send)
        self.pushButton = QtWidgets.QPushButton(self.button_zone)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.button_zone)
        self.gridLayout.addWidget(self.send_zone, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.chats)
        messenger.setCentralWidget(self.centralwidget)

        self.retranslateUi(messenger)
        QtCore.QMetaObject.connectSlotsByName(messenger)

    def retranslateUi(self, messenger):
        _translate = QtCore.QCoreApplication.translate
        messenger.setWindowTitle(_translate("messenger", "MainWindow"))
        self.search_text.setPlaceholderText(_translate("messenger", "Поиск"))
        self.click_chat.setText(_translate("messenger",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#dadada;\">выберите чат</span></p></body></html>"))
        self.message.setHtml(_translate("messenger",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.message.setPlaceholderText(_translate("messenger", "Введите текст:"))


import icons_rc
