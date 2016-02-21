def unique_common(a, b):
    # Allocate an empty list CommonList
    commonList = []

    # unique list a
    a = list(set(a))

    # foreach i in a
    # if i in b ->  append i to res
    # else continue
    for i in a:
        if i in b:
            commonList.append(i)

    # if there is no common element return None
    if len(commonList) == 0:
        return None

    # sort the list
    commonList.sort()

    return commonList




print (unique_common([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7]))
print (unique_common([5, 6, 7, 0], [3, 2, 3, 2]))