# test List = [2,4,1,5,6,3,9,7,8]

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    """

    快速排序的辅助方法，递归调用进行排序
    """
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    """

    默认参考值为数组的第一个数
    左右指针分别向中间移动
    """
    pivotvalue = first

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= alist[pivotvalue]:
            leftmark = leftmark + 1

        while alist[rightmark] >= alist[pivotvalue] and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[pivotvalue], alist[rightmark] = alist[rightmark], alist[pivotvalue]

    return rightmark


alist = [54, 26, 93, 17, 77, 100, 44, 55, 20]
# l1 = [54,26,-93,17,77,100,44,55,-20]
# l2 = [54,26,20,17,77,100,44,55,93]
# l3 = [54,26,20,17,-77,100,-44,55,93]
# l4 = [54,26,20,17,l_44,100,r_77,55,93]
quickSort(alist)
print(alist)
