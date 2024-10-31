from typing import *
from abc import abstractmethod

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

from FastZKI.ui.Widgets import ShellWindow, ConsoleTextEdit, ParamElement


class Attribute:
    def __init__(self, name: str, type_: Any, value: Any = None, filter: Callable[[Any], bool] = None):
        self.name: str = name
        self.Type = type_
        self._v = value

    @property
    def value(self) -> Any:
        if self._v is None or self._v == "":
            return ""
        return self.Type(self._v)

    @value.setter
    def value(self, value):
        self._v = value


class ArgField:

    def __init__(self, args: List[Attribute]):
        self.args = args

    def get(self, name: str):
        for arg in self.args:
            if arg.name == name:
                return arg.value
        return None


class Console:
    _ui: ShellWindow = None
    _is_console_open = True
    _TEConsoleOut: ConsoleTextEdit = None

    def __init__(self, ui: ShellWindow):
        self._ui = ui
        ui.VLConsoleOut.removeWidget(ui.TEConsoleOutExample)
        ui.TEConsoleOutExample.hide()
        ui.TEConsoleOutExample.destroy()  # TODO как эту заразу уничтожить полностью?

        self._TEConsoleOut = ConsoleTextEdit(ui.centralwidget)
        ui.VLConsoleOut.addWidget(self._TEConsoleOut)

        ui.PBConsoleVisibDescide.clicked.connect(self._click_btn_console_visible)
        ui.key_filter.tab_pressed.connect(lambda: self._click_btn_console_visible(tab=True))
        self._click_btn_console_visible()  # by default console have to hidden

        ui.PBClear.clicked.connect(self.clear)

    def print(self, smg: str, _from: str = "unmarked"):
        print(f"[UI.Console -> Print()] print smg {smg} from {_from}")
        self._TEConsoleOut.append_message(smg)

    def clear(self):
        print(f"[UI.Console -> PBClear] clear console...")
        self._TEConsoleOut.clear()

    def _click_btn_console_visible(self, tab: bool = False):
        self._is_console_open = not self._is_console_open
        print(f"[UI -> PBConsoleVisible] clicked to state {self._is_console_open} {'(TAB)' if tab else ''}")
        self._TEConsoleOut.setVisible(self._is_console_open)
        if self._is_console_open:
            self._ui.PBConsoleVisibDescide.setText("спрятать")
        else:
            self._ui.PBConsoleVisibDescide.setText("показать")

class PrototypeSolutionAlgorythm:
    def __init__(self, console: Console): self.console = console
    @abstractmethod
    def generate_attributes_in(self) -> List[Attribute]: ...
    @abstractmethod
    def user_call_calculate(self, attrs: ArgField): ...
    @abstractmethod
    def generate_attributes_in_out(self) -> (Union[List[Attribute], None], List[Attribute]): ...


class AttributeSpace:
    def __init__(self, ui: ShellWindow, layout: QVBoxLayout):
        self._layout = layout
        self._ui = ui
        self._attributes_ui: Dict[str, ParamElement] = {}
        self._attributes: Dict[str, Attribute] = {}


    _layout: QVBoxLayout = None
    _ui: ShellWindow = None

    def add_attributes(self, attrs: List[Attribute]):
        for attr in attrs:
            if attr.name in self._attributes_ui:
                param_element = self._attributes_ui[attr.name]
                param_element.update_value(str(attr.value))
                self._attributes[attr.name].value = attr.value
            else:
                self._attributes[attr.name] = attr
                param_element = ParamElement(attr.name, attr.value, self._ui.centralwidget)
                self._attributes_ui[attr.name] = param_element
                self._layout.insertWidget(0, param_element)

    def set_attributes(self, attrs: List[Attribute]):
        self.clear()
        self.add_attributes(attrs)

    def get_attrs(self) -> List[Attribute]:
        return list(self._attributes.values())

    def get_ui_attrs(self) -> List[ParamElement]:
        return list(self._attributes_ui.values())

    def clear(self):
        for param_element in self.get_ui_attrs():
            self._layout.removeWidget(param_element)
            param_element.deleteLater()
        self._attributes_ui.clear()
