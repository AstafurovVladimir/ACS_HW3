import random

from extender import *


class Container:
    def __init__(self):
        self.contents = []

    def FillLines(self, lines):
        for i in range(len(lines) // 3):
            try:
                type = int(lines[i * 3])
                name = lines[i * 3 + 1]
                param = int(lines[i * 3 + 2])
            except:
                print('Incorrect input')
                self.contents = []
                return
            if type < 0 | type > 3:
                print('Incorrect input')
                self.contents = []
                return
            if type == 1:
                plant = Tree()
                plant.name = name
                plant.age = param
            if type == 2:
                plant = Bush()
                plant.name = name
                plant.month = Months.GetMonth(param)
            if type == 3:
                plant = Flower()
                plant.name = name
                plant.type = Type.GetType(param)
            self.contents.append(plant)

    def FillRandom(self, number):
        for i in range(number):
            type = random.randint(1, 3)
            name = ""
            nameLenght = random.randint(1, 50)
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(nameLenght):
                name += alphabet[random.randint(0, 25)]
            if type == 1:
                plant = Tree()
                plant.name = name
                plant.age = random.randint(1, 2000)
            if type == 2:
                plant = Bush()
                plant.name = name
                plant.month = Months.GetMonth(random.randint(1, 12))
            if type == 3:
                plant = Flower()
                plant.name = name
                plant.type = Type.GetType(random.randint(1, 3))
            self.contents.append(plant)

    def Write(self, outputPath):
        file = open(outputPath, 'w')
        if len(self.contents) == 0:
            file.write("Container was empty")
            file.close()
            return
        file.write("Container contains {} plants:\n".format(len(self.contents)))
        for plant in self.contents:
            plant.Write(file)
        file.close()

    def HeapSort(self):
        length = len(self.contents)
        for i in range(length, -1, -1):
            self.Heapify(i, length)
        for i in range(length - 1, 0, -1):
            self.contents[0], self.contents[i] = self.contents[i], self.contents[0]
            self.Heapify(0, i)

    def Heapify(self, i, size):
        ma = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size and self.contents[l].NameFunction() > self.contents[ma].NameFunction():
            ma = l
        if r < size and self.contents[r].NameFunction() > self.contents[ma].NameFunction():
            ma = r
        if ma != i:
            self.contents[ma], self.contents[i] = self.contents[i], self.contents[ma]
            self.Heapify(ma, size)
