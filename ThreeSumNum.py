def TwoSumNum(arr, a=0):
    ThreeNum = []
    for i in arr:
        for j in arr:
            if (i - j) and (a - (i + j)) in arr:
                if not any(i in sublist for sublist in ThreeNum):
                    if not any(j in sublist for sublist in ThreeNum):
                        ThreeNum.append([a - (i +j), i, j])
    return ThreeNum


c = TwoSumNum([2, 8, 6, 1, 0, 10, 16, 3, 4, 11, 5], 11)
print(c)
