from plant import *
from enum import Enum


class Type(Enum):
    NOTYPE = 0
    HOME = 1
    GARDEN = 2
    WILD = 3

    @staticmethod
    def GetType(i):
        if i == 1:
            return Type.HOME
        if i == 2:
            return Type.GARDEN
        if i == 3:
            return Type.WILD
        return Type.NOTYPE


class Flower(Plant):
    def __init__(self):
        self.type = Type.NOTYPE
        self.name = ""

    def Write(self, outStream):
        outStream.write("Flower: {} of {} type\n".format(self.name, self.type.name.lower()))
        pass
