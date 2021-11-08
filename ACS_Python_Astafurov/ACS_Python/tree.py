from plant import *


class Tree(Plant):
    def __init__(self):
        self.age = 0
        self.name = ""

    def Write(self, outStream):
        outStream.write("Tree: {} of age {}\n".format(self.name, self.age))
        pass

