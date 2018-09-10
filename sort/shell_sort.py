def sort_fun(list, trip):
    length = len(list)
    h = length // trip
    while h >= 1:
        for i in range(h, length):
            for j in range(i, h - 1, -h):
                if list[j] < list[j - h]:
                    list[j], list[j - h] = list[j - h], list[j]
        h = h // trip
    print(list)


list = [5, 3, 2, 4, 6, 1]
sort_fun(list, 2)
