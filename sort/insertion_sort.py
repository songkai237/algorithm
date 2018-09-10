def sort_fun(list):
    for i in range(1, len(list)):
        j = i
        for j in range(j, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
    print(list)

l = [2, 56, 7, 36, 75, 23, 17, 8]
sort_fun(l)