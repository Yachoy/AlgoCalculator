from typing import *
import os
import importlib.util

from FastZKI.Components import PrototypeSolutionAlgorythm, Console


class ExceptionExit(Exception): pass

class LoaderAlgorithms:
    place_algo: str
    solutions: dict[str, PrototypeSolutionAlgorythm]

    def __init__(self, path_folder_algos: str):
        self.path_algo = path_folder_algos
        self.solutions = {}

    def load(self, console: Console):
        for k, v in self.solutions.items():
            del v #TODO its good idea?
        self.solutions.clear()
        if not os.path.exists(self.path_algo):
            print(f"[Backend.LoaderAlgorithms -> load()] Fail to find path for algorithms {self.path_algo}!")
            raise ExceptionExit
        if not os.path.isdir(self.path_algo):
            print(f"[Backend.LoaderAlgorithms -> load()] The path {self.path_algo} for algorithms is not folder!")
            raise ExceptionExit
        for filename in os.listdir(self.path_algo):
            if filename.endswith('.py'):
                module_name = filename[:-3]  # Убираем '.py' из имени файла
                module_path = os.path.join(self.path_algo, filename)

                # Загрузка модуля
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Проверка, есть ли класс Solution в модуле
                if hasattr(module, 'Solution'):
                    self.solutions[module_name] = module.Solution(console)
                    print(f"[Backend.LoaderAlgorithms -> load()] find algorithm {module_name}")
                else:
                    print(f"[Backend.LoaderAlgorithms -> load()] find file {module_path} but hi didn't have class Solution to import. Watch documentation")


class CppRuntimeImplementation:
    pass #TODO future for fast execute.

