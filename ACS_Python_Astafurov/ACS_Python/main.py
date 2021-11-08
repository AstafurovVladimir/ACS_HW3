import sys

from container import *


def ReadFile(inputPath):
    lines = []
    file = open(inputPath, 'r')
    amount = file.readline()
    try:
        amount = int(amount)
    except:
        print('Incorrect input')
        return []
    for i in range(3 * amount):
        lines.append(file.readline().rstrip())
    file.close()
    return lines


if __name__ == '__main__':
    container = Container()
    if len(sys.argv) != 5:
        print('Incorrect console parameters')
        sys.exit()
    if sys.argv[1] == 'file':
        try:
            file = open(sys.argv[2], 'r')
            file.close()
            file = open(sys.argv[3], 'w')
            file.close()
            file = open(sys.argv[4], 'w')
            file.close()
        except:
            print('Incorrect console parameters')
            sys.exit()
        container.FillLines(ReadFile(sys.argv[2]))
    elif sys.argv[1] == 'random':
        try:
            number = int(sys.argv[2])
            file = open(sys.argv[3], 'w')
            file.close()
            file = open(sys.argv[4], 'w')
            file.close()
        except:
            print('Incorrect console parameters')
            sys.exit()
        container.FillRandom(int(sys.argv[2]))
    else:
        print('Incorrect console parameters')
        sys.exit()
    container.Write(sys.argv[3])
    container.HeapSort()
    container.Write(sys.argv[4])
