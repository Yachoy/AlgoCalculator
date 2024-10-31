from abc import ABC
from typing import *

from FastZKI.Components import Attribute, PrototypeSolutionAlgorythm, Console, ArgField


class Solution(PrototypeSolutionAlgorythm):

    def __init__(self, console: Console):
        super().__init__(console)

    p = 0
    q = 0
    m = 0

    n = 0
    e = 0
    d = 0

    def generate_attributes_in(self) -> List[Attribute]:
        return [
            Attribute("p", int),
            Attribute("q", int),
            Attribute("Message", str)
        ]

    def generate_attributes_in_out(self) -> (Union[List[Attribute], None], List[Attribute]):
        return [
            [
                Attribute("p", int, self.p),
                Attribute("q", int, self.q)
            ],
            [
                Attribute("m", int, self.m),
                Attribute("n", int, self.n),
                Attribute("e", int, self.e),
                Attribute("d", int, self.d)
            ]
        ]

    def user_call_calculate(self, attrs: ArgField):
        data = {}
        print(f"rsa {t if (t:=attrs.get("p")) else "_"} {t if (t:=attrs.get("q")) else "_"} {attrs.get("Message")}")
        self.p = attrs.get("p")
        self.q = attrs.get("q")

