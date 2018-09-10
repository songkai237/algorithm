# 组合数：
#     从n个不同元素中任意选取m个数为一组，称为一个组合数
#     求n个元素选取m个数的组合数的个数
# 公式：C(n,m)=n!/((n-m)!*m!)（m≤n）
# 性质1：C(n,m)= C(n,n-m)
# 性质2：C(n,m)=C(n-1,m-1)+C(n-1,m)
# 通过性质2可以看出求组合数个数的方法可以使用递归来解决

def combinatiorial(n, m):
    if m == 0 or n == m:
        return 1
    return combinatiorial(n - 1, m - 1) + combinatiorial(n - 1, m)


print(combinatiorial(5, 5))
