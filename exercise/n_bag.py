# 广义背包问题的描述如下：给定载重量为M的背包和n种物品，每种物品有一定的重量和价值，现在需要设计算法，在不超过背包载重量的前提下，巧妙选择物品，使得装入背包的物品的总价值最大化。规则是，每种物品均可装入背包多次或不装入（但不能仅装入物品的一部分）。请用数学语言对上述背包问题加以抽象，在此基础上给出动态规划求解该问题的递归公式。要求对所给公式中的符号意义加以详细说明，并简述算法的求解步骤。用一种你熟悉的程序设计语言加以实现。

# 最大收益递推式：M[i][j]=max(M[i-1][j-k*weight[i]]+k*value[i])(0 <= k <= j/weight[i])
# M为前i件物品放在容量j的背包的最大收益集合
# weight[i]为第i件物品的重量
# value[i]为第i件物品的价值
# k为当前物品放入的个数

def complet_bag(num, capacity, weight, value):
    """
    :param num:物品数量
    :param capacity:背包容量
    :param weight:物品占用容量列表
    :param value:物品价值列表
    :return:最大收益集合
    """
    M = [[0 for col in range(capacity + 1)] for row in range(num + 1)]
    sign = [0 for i in range(num)]
    for i in range(1, num + 1):
        for j in range(1, capacity + 1):
            M[i][j] = M[i - 1][j]
            for k in range(j // weight[i - 1] + 1):
                if M[i][j] < M[i - 1][j - k * weight[i - 1]] + k * value[i - 1]:
                    M[i][j] = M[i - 1][j - k * weight[i - 1]] + k * value[i - 1]
                    sign[i - 1] = k
                    # if i - 1 >= 1:
                    #     sign[i - 2] =sign[i-2] -
    return M, sign


# weight = [2, 6, 7, 4, 1]
# value = [10, 4, 3, 7, 4]
weight = [7, 4, 6, 1, 2]
value = [3, 7, 4, 4, 10]
M, sign = complet_bag(5, 7, weight, value)
print(M)

print("最大收益为", M[5][7])
print("物品选择集合为", sign)
