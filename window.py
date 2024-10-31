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

from FastZKI.backend import ExceptionExit
from FastZKI.ui.Widgets import ShellWindow
from FastZKI.Components import PrototypeSolutionAlgorythm, AttributeSpace, Console, ArgField


class Window:

    _mv: ShellWindow = None
    _algos: Dict[str, PrototypeSolutionAlgorythm] = None
    console: Console = None

    attrs_in: AttributeSpace = None
    attrs_out: AttributeSpace = None

    def __init__(self):
        super().__init__()
        self._mv = ShellWindow()
        self.console = Console(self._mv)
        self._algos = {}

        self.attrs_in = AttributeSpace(self._mv, self._mv.VLAttrIn)
        self.attrs_out  = AttributeSpace(self._mv, self._mv.VLAttrOut)

        self._mv.comboBox.currentIndexChanged.connect(self.change_algo)
        self._mv.PBCalculate.clicked.connect(self.calculate_call)
        print("Done loading")

    def change_algo(self, index: int, name: str = None):
        if name is not None: raise NotImplementedError #TODO in future realise this may be

        name_algo = self._mv.comboBox.itemText(index)
        print(f"[UI -> CBAlgorithmList] loading algorithm {name_algo}")
        attrs = self._algos[name_algo].generate_attributes_in()
        self.attrs_in.set_attributes(attrs)
        self.attrs_out.clear()

    def calculate_call(self):
        name_algo = self._mv.comboBox.itemText(self._mv.comboBox.currentIndex())
        algo: PrototypeSolutionAlgorythm = self._algos[name_algo]
        attrs_in = self.attrs_in.get_attrs()
        attrs_in_ui = self.attrs_in.get_ui_attrs()

        for attr, attr_ui in zip(attrs_in, attrs_in_ui):
            attr.value = attr_ui.read_value()

        print(f"[UI -> PBCalculate] start calculate algo {name_algo} with {[f"{i.name}:{i.value}" for i in attrs_in]}")


        algo.user_call_calculate(ArgField(attrs_in))
        print("[UI -> PBCalculate] done. Read output")
        attrs_in, attrs_out = algo.generate_attributes_in_out()
        self.attrs_in.add_attributes(attrs_in)
        self.attrs_out.set_attributes(attrs_out)

    def get_mv(self): return self._mv

    def show(self, with_algos: Dict[str, PrototypeSolutionAlgorythm]):
        self._mv.show()
        self._algos = with_algos
        self._mv.comboBox.addItems(list(with_algos.keys()))
