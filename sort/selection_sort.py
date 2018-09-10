def sort_fun(list):
    for i in range(0, len(list) - 1):
        index = i
        for j in range(index + 1, len(list)):
            if list[index] > list[j]:
                index = j
            list[i], list[index] = list[index], list[i]
    print(list)


l = [2, 56, 7, 36, 75, 23, 17, 8]
sort_fun(l)
