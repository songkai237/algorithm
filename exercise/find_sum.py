# 给定一个列表如[1,2,3,5,4,7,2,9]和一个目标数tag=10，找出列表中属是否有几个数加起来的和正好是目标数，如果有，返回他们的下标，如果没有，返回False

def findSum(l, target):
    finalResult = []
    currentResult = []
    findSumHelper(l, target, 0, currentResult, finalResult)
    if finalResult:
        return finalResult
    return False


def findSumHelper(l, target, begin, currentResult, finalResult):
    if begin > len(l):
        return

    if target == 0:
        temp = currentResult[:]
        finalResult.append(temp)
    elif target < 0:
        return
    else:
        for i in range(begin, len(l)):
            currentResult.append(i)
            findSumHelper(l, target - l[i], i + 1, currentResult, finalResult)
            currentResult.pop()


if __name__ == '__main__':
    l = [1, 2, 3, 5, 4, 7, 2, 9]
    print(findSum(l, 10))
