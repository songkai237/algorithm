def mergeSort(alist):
    print(alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        leftlist = alist[:mid]
        rightlist = alist[mid:]

        mergeSort(leftlist)
        mergeSort(rightlist)

        i, j, k = 0, 0, 0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k] = leftlist[i]
                i = i + 1
                k = k + 1
            else:
                alist[k] = rightlist[j]
                j = j + 1
                k = k + 1

        while i < len(leftlist):
            alist[k] = leftlist[i]
            i = i + 1
            k = k + 1

        while j < len(rightlist):
            alist[k] = rightlist[j]
            j = j + 1
            k = k + 1
    print(alist)


list = [1, 5, 6, 2, 8, 9, 3, 7, 4]
mergeSort(list)
