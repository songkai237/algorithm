# 所谓TSP问题是指旅行商要去n个城市推销商品，其中每个城市到达且仅到达一次，并且要求所走的路程最短（该问题又称货郎担问题、邮递员问题、售货员问题等）。TSP问题最容易想到、也肯定能得到最优解的算法是穷举法，即考察所有可能的行走线路，从中选出最佳的一条。但是用穷举法求解TSP问题的时间复杂性为O(n!)，属于NP问题。请用数学语言对该TSP问题加以抽象，在此基础上给出动态规划求解该问题的递推公式。要求对所给公式中的符号意义加以详细说明，并简述算法求解步骤。用一种你熟悉的程序设计语言加以实现。

# 分析:假设最短路径为s0->s1->s2->s3->s4->s0,则可以知道s1->s2->s3->s4->s0必然是这五个点钟从s1到s0的最短路径

# 最短路径递推式:d(i,V)=min(Cik+d(k,V-{k}))

C = [[0, 3, 6, 7],
     [5, 0, 2, 3],
     [6, 4, 0, 2],
     [3, 7, 5, 0]]


def i_in_j(i, j):
    # print("i=", i, "j=", j)
    str1 = bin(j).replace('0b', '')
    # print("str1=", str1)
    l = list(str1)
    # print("list=", l)
    l.reverse()
    # print("listr=", l)
    if i > len(l):
        return False
    return int(l[i - 1]) == 1


def get_vector(j):
    str1 = bin(j).replace('0b', '')
    l = list(str1)
    l.reverse()
    for i in range(0, len(l)):
        l[i] = int(l[i])
    return l


def get_j(j, k):
    str1 = bin(j).replace('0b', '')
    l = list(str1)
    l.reverse()
    l[k] = 0
    str2 = ''.join('%s' % s for s in l)
    result = 0
    for i in range(0, len(str2)):
        result += int(str2[i]) * (2 ** i)
    return result


def best_path(C, n):
    """
    :param C: 城市距离矩阵
    :param n: 矩阵长度
    :return: 最短路径
    """
    d = [[None for col in range(0, 2 ** (n - 1))] for row in range(0, n)]

    for i in range(1, n):
        d[i][0] = C[i][0]
    for j in range(1, 2 ** (n - 1)):
        v = get_vector(j)
        for i in range(1, n):
            if i_in_j(i, j) is not True:
                for k in range(0, len(v)):
                    if v[k] == 1:
                        m = get_j(j, k)
                        if d[i][j] is None:
                            d[i][j] = C[i][k + 1] + d[k + 1][m]
                        else:
                            if d[i][j] > C[i][k + 1] + d[k + 1][m]:
                                d[i][j] = C[i][k + 1] + d[k + 1][m]
    for i in range(1, n):
        j = get_j(2 ** (n - 1) - 1, i - 1)

        if d[0][2 ** (n - 1) - 1] is None:
            d[0][2 ** (n - 1) - 1] = C[0][i] + d[i][j]
        else:
            if d[0][2 ** (n - 1) - 1] > C[0][i] + d[i][j]:
                d[0][2 ** (n - 1) - 1] = C[0][i] + d[i][j]
    print(d)
    return d[0][2 ** (n - 1) - 1]


a = best_path(C, 4)
print("最短路径为", a)
