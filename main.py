import os
import sys

from window import *
from window import Window
from backend import LoaderAlgorithms, ExceptionExit


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        win = Window()

        algos = LoaderAlgorithms(os.getcwd() + "/algorithms/")
        algos.load(win.console)

        win.show(with_algos=algos.solutions)

        code = app.exec()

        print("[App] cleanup and exit...")

        #TODO stuff after exit

        exit(code)
    except ExceptionExit as e:
        print("[App -> ExceptionError] exit app...")

    exit(-1)
