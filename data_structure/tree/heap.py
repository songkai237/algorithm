class MinHeap:
    def __init__(self):
        self._heapList = []
        self._size = 0

    def buildHeap(self, alist):
        i = len(alist) // 2
        self._size = len(alist)
        self._heapList = alist[:]
        while i > 0:
            self.doDown(i)
            i -= 1

    def doUp(self, i):
        while i // 2 > 0:
            if self._heapList[i - 1] < self._heapList[i // 2 - 1]:
                self._heapList[i - 1], self._heapList[i // 2 - 1] = self._heapList[i // 2 - 1], self._heapList[i - 1]
            else:
                break
            i = i // 2

    def doDown(self, i):
        while i * 2 <= self._size:
            minIndex = self._getMInChildIndex(i)
            if self._heapList[i - 1] > self._heapList[minIndex]:
                self._heapList[i - 1], self._heapList[minIndex] = self._heapList[minIndex], self._heapList[i - 1]
                i = minIndex
            else:
                break

    def insert(self, value):
        self._heapList.append(value)
        self._size += 1
        self.doUp(self._size)

    def delMin(self):
        minValue = self._heapList[0]
        self._heapList[0] = self._heapList.pop()
        self._size -= 1
        self.doDown(1)
        return minValue

    def getList(self):
        return self._heapList

    def getSize(self):
        return self._size

    def _getMInChildIndex(self, i):
        if i * 2 + 1 > self._size:
            return i * 2
        else:
            if self._heapList[i * 2 - 1] < self._heapList[i * 2]:
                return i * 2 - 1
            else:
                return i * 2

# 测试
if __name__ == '__main__':
    # h = MinHeap()
    # h.insert(5)
    # h.insert(1)
    # h.insert(4)
    # h.insert(2)
    # h.insert(8)
    # h.insert(0)
    # print(h.getList())
    # print(h.delMin())
    # print(h.getList())
    h = MinHeap()
    alist = [3,4,1,5,45,24,77,57,15]
    h.buildHeap(alist=alist)
    print(h.getList())