def isAnagram(in1, in2):
    list1 = []
    list2 = []

    list1.extend(in1)
    list2.extend(in2)

    print(list1)

    if in1 is None or in2 is None or len(in1) != len(in2):
        return False
    
    if len(in1) == len(in2):
        for a in list1:
            if a not in list2:
                return False

    return True

print(isAnagram('amor', 'roma'))  