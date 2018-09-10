import numpy as np


def PrintSnakeMatrix(n):
    # 输入正整数n，如果n=4，输出
    # 10 11 12 1
    # 9  16 13 2
    # 8  15 14 3
    # 7  6  5  4
    n = int(n)
    myArray = np.zeros((n, n), dtype=np.int16)

    i, j, num = 0, n - 1, 1
    myArray[i][j] = num
    while num < n * n:
        # 向下
        while i + 1 < n and myArray[i + 1][j] == 0:
            i = i + 1
            num = num + 1
            myArray[i][j] = num
        while j > 0 and myArray[i][j - 1] == 0:
            j = j - 1
            num = num + 1
            myArray[i][j] = num
        while i > 0 and myArray[i - 1][j] == 0:
            i = i - 1
            num = num + 1
            myArray[i][j] = num
        while j + 1 < n and myArray[i][j + 1] == 0:
            j = j + 1
            num = num + 1
            myArray[i][j] = num

    print(myArray)


n = input("请输入n的值：")
PrintSnakeMatrix(n)
