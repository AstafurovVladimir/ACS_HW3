class Plant:
    def Read(self, array, i):
        pass

    def Print(self):
        pass

    def Write(self, outStream):
        pass

    def NameFunction(self):
        vowels = "aeiyou"
        vCount = 0
        for i in range(len(self.name)):
            if vowels.find(self.name[i]) != -1:
                vCount += 1
        return vCount / len(self.name)
