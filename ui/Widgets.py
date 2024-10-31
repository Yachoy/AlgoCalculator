from typing import *

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

from PySide6.QtCore import Qt, Signal, Slot, QObject, QEvent
from PySide6.QtGui import QKeyEvent

from FastZKI.ui.ui_DesignMain import Ui_MainWindow as MainWindow
from FastZKI.ui.ui_DesignParameterElement import Ui_Form as ElementParam


class ParamElement(QWidget, ElementParam):

    def __init__(self, name: str, value: Any, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.name = name
        self.value = value
        self.TEEnteredText.setText(str(value))
        self.LNameParameter.setText(name)

    def update_value(self, text: str):
        self.TEEnteredText.setText(text)

    def read_value(self): return self.TEEnteredText.text()


class ConsoleTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setReadOnly(True)  # Делаем поле только для чтения
        self.autoscroll = True  # Флаг автоскролла

    def append_message(self, message):
        """Добавляет сообщение в консоль."""
        self.append(message)
        if self.autoscroll:
            self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def scrollContentsBy(self, dx, dy):
        """Отслеживаем скролл пользователя."""
        super().scrollContentsBy(dx, dy)
        # Если пользователь прокрутил не до конца, отключаем автоскролл
        if self.verticalScrollBar().value() != self.verticalScrollBar().maximum():
            self.autoscroll = False
        # Если пользователь вернулся в конец, включаем автоскролл
        else:
            self.autoscroll = True


class ShellWindow(QMainWindow, MainWindow):
    class KeyFilter(QObject):
        tab_pressed = Signal()

        def eventFilter(self, obj, event):
            if event.type() == QEvent.Type.KeyRelease:
                if event.key() == Qt.Key.Key_Tab:
                    self.tab_pressed.emit()
                    return True
            return super().eventFilter(obj, event)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.key_filter = ShellWindow.KeyFilter()
        self.installEventFilter(self.key_filter)

