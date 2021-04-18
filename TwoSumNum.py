def TwoSumNum(arr, a=0):
    TwoNum = []
    for i in arr:
        if (a - i) in arr:
            if not any(i in sublist for sublist in TwoNum):
                TwoNum.append([a - i, i])
    return TwoNum


c = TwoSumNum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 11)
print(c)
