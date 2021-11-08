from plant import *
from enum import Enum


class Months(Enum):
    NOMONTH = 0
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    @staticmethod
    def GetMonth(i):
        if i == 1:
            return Months.JANUARY
        if i == 2:
            return Months.FEBRUARY
        if i == 3:
            return Months.MARCH
        if i == 4:
            return Months.APRIL
        if i == 5:
            return Months.MAY
        if i == 6:
            return Months.JUNE
        if i == 7:
            return Months.JULY
        if i == 8:
            return Months.AUGUST
        if i == 9:
            return Months.SEPTEMBER
        if i == 10:
            return Months.OCTOBER
        if i == 11:
            return Months.NOVEMBER
        if i == 12:
            return Months.DECEMBER
        return Months.NOMONTH


class Bush(Plant):
    def __init__(self):
        self.month = Months.NOMONTH
        self.name = ""

    def Write(self, outStream):
        outStream.write("Bush: {} that blossoms in {}\n".format(self.name, self.month.name.capitalize()))
        pass
