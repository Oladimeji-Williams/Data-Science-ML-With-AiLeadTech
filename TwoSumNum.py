def TwoSumNum(arr=None, tar=None):
    TwoNum = []  # define an empty list for holding the list of duplet
    for i in arr:  # first number to iterate into the given array
        if (tar - i) in arr:  # if the other number of the target mated pair is present in the given array
            if not any(i in sublist for sublist in TwoNum):  # To avoid, repitition, if one of the target numbers is not already in the target list (i.e in TwoNum)
                TwoNum.append([tar - i, i])  # appends the duplet that hits the target into the target list (i.e into TwoNum)
    return TwoNum
