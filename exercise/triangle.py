# 打印出三角形：
#    1
#   121
#  12321
# 1234321

n = int(input("请输入一个数："))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for m in range(1, 2 * i):
        if m <= i:
            print(m, end='')
        else:
            print(2 * i - m, end='')
    print('\n', end='')
