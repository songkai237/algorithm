def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if item == alist[mid]:
            found = True
        elif item > alist[mid]:
            first = mid + 1
        else:
            last = mid - 1

    return found


alist = [1, 2, 3, 4, 5, 6, 7]
print(binarySearch(alist,1))
print(binarySearch(alist,7))
print(binarySearch(alist,4))
print(binarySearch(alist,3))
print(binarySearch(alist,0))
print(binarySearch(alist,8))
