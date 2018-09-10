# 两个一样的list（顺序可能不同），其中一个list丢失了一个数据，找出那个丢失的数据

def findD(L1, L2):
    if len(L1) > len(L2):
        for val in L1:
            if val not in L2:
                return val
    elif len(L1) < len(L2):
        for val in L2:
            if val not in L1:
                return val
    else:
        return None


L1 = [1, 3, 5, 7, 2, 4, 6, 8]
L2 = [1, 5, 7, 4, 2, 8, 6]
assert (findD(L1, L2) == 3)

L1 = [1, 3, 5, 7, 2, 4, 6, 8]
L2 = [1, 5, 3, 7, 4, 2, 8, 10, 6]
assert (findD(L1, L2) == 10)
