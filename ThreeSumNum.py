def ThreeSumNum(arr=None, tar=None):
    ThreeNum = []  # define an empty list for holding the list of triplets
    for i in arr:  # first number to iterate into the given array
        for j in arr:  # second number to iterate into the given array
            if (i - j) and (tar - (i + j)) in arr:  # if two target numbers are present in the given array
                if not any(i in sublist for sublist in ThreeNum):  # To avoid repitition, if one of the target numbers is not already in the target list (i.e in ThreeNum)
                    if not any(j in sublist for sublist in ThreeNum):  # if another target number is not already in teh target list (i.e in ThreeNum)
                        ThreeNum.append([tar - (i + j), i, j])  # appends the triplet that hits the target into the target list (i.e into ThreeNum)
    for i in ThreeNum:  # sorts each item in the triplet in the ThreeNum
        i.sort()
    ThreeNum.sort()  # sorts each triplet of the ThreeNum
    return ThreeNum


c = ThreeSumNum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 21)
print(c)
