def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        leftlist = l[:mid]
        rightlist = l[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i, j, k = 0, 0, 0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                l[k] = leftlist[i]
                i = i + 1
                k = k + 1
            else:
                l[k] = rightlist[j]
                j = j + 1
                k = k + 1

        while i < len(leftlist):
            l[k] = leftlist[i]
            i = i + 1
            k = k + 1

        while j < len(rightlist):
            l[k] = rightlist[j]
            j = j + 1
            k = k + 1
    print(l)


l = [1, 5, 6, 2, 8, 9, 3, 7, 4]
merge_sort(l)
print(l)
