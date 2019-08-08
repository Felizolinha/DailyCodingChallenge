values = [3, 4, -1, 1]
integerList = dict()

for v in values:
    integerList[v] = 1


for i in range(1, max(values)+2):
    if(i not in integerList):
        print(i)
        break