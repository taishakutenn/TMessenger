import sys
from interface import *  # GUI file
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPropertyAnimation


class MainWindow(QtWidgets.QMainWindow):  # Унаследуем от QMainWindow
    def __init__(self):
        super(MainWindow, self).__init__()  # Инициализация родительского класса
        self.ui = Ui_messenger()  # Создание экземпляра вашего UI
        self.ui.setupUi(self)  # Настройка интерфейса
        self.ui.message.setFixedHeight(60)
        self.ui.send_zone.setFixedHeight(60)

        # Нажатие кнопок
        self.ui.search_zone_open_button.clicked.connect(lambda: self.open_search_zone())
        self.ui.add_chat_button.clicked.connect(lambda: self.add_chat_to_list())
        self.ui.menu_button.clicked.connect(lambda: self.toggle_menu())

        # Создаем меню
        self.menu_widget = MenuWidget(self)
        self.menu_widget.setGeometry(0, 0, 280, 590)  # Задаем размеры и положение меню
        self.menu_widget.hide()  # Скрываем меню по умолчанию

        # Изменение размера поля для ввода сообщения
        self.ui.message.textChanged.connect(self.adjust_height)

        self.ui.scroll_list_layout = QtWidgets.QVBoxLayout(self.ui.scroll_area_list_of_chats)
        self.ui.scroll_list_of_chats.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ui.scroll_list_layout.setContentsMargins(5, 5, 0, 0)

        self.show()  # Показываем окно

    def open_search_zone(self):
        height = self.ui.search_zone.height()

        #  Условия считывающие, открыто ли окно поиска
        if height == 0:
            newHeight = 60
        else:
            newHeight = 0

        # Проигрывание анимации
        self.animation = QtCore.QPropertyAnimation(self.ui.search_zone, b"maximumHeight")
        self.animation.setDuration(150)
        self.animation.setStartValue(height)
        self.animation.setEndValue(newHeight)
        self.animation.start()

    def adjust_height(self):
        try:
            # Получаем необходимую высоту для текста
            height = self.ui.message.document().size().height()
            newHeight = 0
            # Добавляем небольшой отступ
            if height < 168:
                if height >= 56:
                    self.ui.message.setFixedHeight(int(height) + 16)
                    self.ui.send_zone.setFixedHeight(int(height) + 16)
                    newHeight = 56
                elif height >= 88:
                    self.ui.message.setFixedHeight(int(height) + 16)
                    self.ui.send_zone.setFixedHeight(int(height) + 16)
                    newHeight = 88
                elif height >= 120:
                    self.ui.message.setFixedHeight(int(height) + 16)
                    self.ui.send_zone.setFixedHeight(int(height) + 16)
                    newHeight = 120
                elif height >= 152:
                    self.ui.message.setFixedHeight(int(height) + 16)
                    self.ui.send_zone.setFixedHeight(int(height) + 16)
                    newHeight = 152
                if height > 24:
                    if height < newHeight:
                        self.ui.message.setFixedHeight(int(height) - 16)
                        self.ui.send_zone.setFixedHeight(int(height) - 16)
                else:
                    self.ui.message.setFixedHeight(60)
                    self.ui.send_zone.setFixedHeight(60)

            else:
                self.ui.message.setFixedHeight(168)
                self.ui.send_zone.setFixedHeight(168)

        except Exception as e:
            print(f"Ошибка при изменении высоты: {e}")  # Выводим ошибку в консоль

    def open_chat_zone(self):
        width = self.ui.chats.width()

        #  Условия считывающие, открыто ли окно поиска
        if width == 0:
            newWidth = 16777215
            # Скрытие заглушки
            self.ui.click_chat.setMaximumSize(0, 16777215)
            # Показ окна чата
            self.ui.chats.setMaximumSize(16777215, 16777215)
        else:
            newWidth = 0
            # Показ заглушки
            self.ui.click_chat.setMaximumSize(16777215, 16777215)
            # Скрытие окна чата
            self.ui.chats.setMaximumSize(0, 16777215)

    def add_chat_to_list(self):
        try:
            # Создаем экземпляр ChatFrame
            chat_frame = ChatFrame("Имя чата", "Последнее сообщение", self)
            # Добавляем chat_frame в layout
            self.ui.scroll_list_layout.addWidget(chat_frame, 0, QtCore.Qt.AlignTop)

        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def toggle_menu(self):
        if self.menu_widget.isVisible():
            self.close_menu()
        else:
            self.open_menu()

    def open_menu(self):
        self.menu_widget.setVisible(True)

    def close_menu(self):
        self.menu_widget.setVisible(False)

    def mousePressEvent(self, event):
        if self.menu_widget.isVisible():
            self.close_menu()


class ChatFrame(QtWidgets.QFrame):
    def __init__(self, chat_name, last_message, main_window):
        super().__init__()
        self.main_window = main_window
        self.setMaximumSize(QtCore.QSize(261, 51))
        self.setMinimumSize(QtCore.QSize(0, 51))
        self.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)

        # Создаем метку для имени чата
        self.chat_name_label = QtWidgets.QLabel(self)
        self.chat_name_label.setGeometry(QtCore.QRect(10, 0, 235, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chat_name_label.setFont(font)
        self.chat_name_label.setStyleSheet("color: rgb(218, 218, 218)")
        self.chat_name_label.setText(chat_name)  # Устанавливаем текст имени чата

        # Создаем метку для последнего сообщения
        self.last_message_label = QtWidgets.QLabel(self)
        self.last_message_label.setGeometry(QtCore.QRect(10, 20, 241, 31))
        self.last_message_label.setText(last_message)  # Устанавливаем текст последнего сообщения

    def mousePressEvent(self, event):
        # Обработка нажатия на фрейм
        print(f"Нажатие на чат: {self.chat_name_label.text()}")
        self.main_window.open_chat_zone()
        super().mousePressEvent(event)  # Вызов метода родителя

    def open_chat_window(self):
        try:
            width = self.width()
            #  Условия считывающие, открыто ли окно поиска
            if width == 0:
                # Скрытие заглушки
                self.click_chat.setMaximumSize(0, 16777215)
                # Показ окна чата
                self.chats.setMaximumSize(16777215, 16777215)
            else:
                # Показ заглушки
                self.click_chat.setMaximumSize(16777215, 16777215)
                # Скрытие окна чата
                self.chats.setMaximumSize(0, 16777215)
        except Exception as e:
            print(f"Ошибка при опытки показа окна чата {e}")


class MenuWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Создние виджета меню
        self.setStyleSheet("background-color: rgb(76,76,76);\n"
                           "border-radius: 10;\n"
                           "")
        self.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 281, 579))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.menu_zones_frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.menu_zones_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_zones_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_zones_frame.setObjectName("menu_zones_frame")
        self.widget = QtWidgets.QWidget(self.menu_zones_frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 261, 581))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.account_frame = QtWidgets.QFrame(self.widget)
        self.account_frame.setMaximumSize(QtCore.QSize(16777215, 90))
        self.account_frame.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                         "border-radius: 10;")
        self.account_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.account_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.account_frame.setObjectName("account_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.account_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QFrame(self.account_frame)
        self.logo.setMaximumSize(QtCore.QSize(80, 80))
        self.logo.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.name_id = QtWidgets.QFrame(self.account_frame)
        self.name_id.setStyleSheet("background-color: rgb(76, 76, 76);\n"
                                   "border-radius: 40px")
        self.name_id.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_id.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_id.setObjectName("name_id")
        self.horizontalLayout.addWidget(self.name_id)
        self.verticalLayout.addWidget(self.account_frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.menu_zones_frame, 0, 0, 1, 1)

    def mousePressEvent(self, event):
        # Игнорируем события мыши
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()  # Создаем экземпляр MainWindow
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
