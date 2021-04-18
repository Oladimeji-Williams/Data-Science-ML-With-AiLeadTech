def TwoSumNum(arr, a=0):
    TwoNum = []
    for i in arr:
        if (a - i) in arr:
            if not any(i in sublist for sublist in TwoNum):
                TwoNum.append([a - i, i])
    return TwoNum
