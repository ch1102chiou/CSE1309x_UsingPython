def crazy_list(some_list):
    def updateIndex(index, revIndex):
        index = index + 1
        revIndex = revIndex - 1
        return index , revIndex
    index = 0
    revIndex = -1
    isCrazy = True
    while index < len(some_list):
        if some_list[index] != some_list[revIndex]:
            return False
        index, revIndex =  updateIndex(index, revIndex)
    return True


a = [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] 
b = [4, 5, 6, 7, 8, 4, 5, 2]
print (crazy_list(a))
print (crazy_list(b))