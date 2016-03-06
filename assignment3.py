# Type your code here 
def find_word_horizontal(crosswords,word):
    rowIndex = 0
    for row in crosswords:
        string = ""
        # transfer to each row to string
        for c in row:
            string = string + c
        # if string contains a word
        # return the colume and row index
        colIndex = string.find(word)
        if  colIndex != -1:
            return [rowIndex, colIndex]
        rowIndex = rowIndex + 1
    # No match return None
    return None



""" part 1 test case
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print (find_word_horizontal(crosswords,word))
"""


# Type your code here 
def find_word_vertical(crosswords,word):
    # Type your code here 
    # Insert from part 1
    def find_word_horizontal(crosswords,word):
        rowIndex = 0
        for row in crosswords:
            string = ""
            # transfer to each row to string
            for c in row:
                string = string + c
            # if string contains a word
            # return the colume and row index
            colIndex = string.find(word)
            if  colIndex != -1:
                return [rowIndex, colIndex]
            rowIndex = rowIndex + 1
        # No match return None
        return None

    # function to caculate matrix transpose
    def transMatrix(matrix):
        if len(matrix) <= 0:
            return None
        rowSize = len(matrix)
        colSize = len(matrix[0])
        # init the matrix_T
        matrix_T = [[] for i in range(len(matrix[0]))]
        for i in range (rowSize):
            for j in range (colSize):
                matrix_T[j].append(matrix[i][j])
        return matrix_T

    a = find_word_horizontal(transMatrix(crosswords), word)
    if a is None:
        return None
    else:
        return [a[1], a[0]]


""" part2 test case
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print (find_word_vertical(crosswords,word)) 
"""


def capitalize_word_in_crossword(crosswords,word):
    wordLen = len(word)
    hori_match = find_word_horizontal(crosswords,word)
    if hori_match != None:
        row = hori_match[0]
        col = hori_match[1]
        for index in range(wordLen):
            crosswords[row][col + index] = crosswords[row][col + index].upper()
    else:
        verti_match = find_word_vertical(crosswords,word)
        if verti_match != None:
            row = verti_match[0]
            col = verti_match[1]
            for index in range(wordLen):
                crosswords[row + index][col] = crosswords[row + index][col].upper()
    return crosswords

crosswords=[['s','d','o'],['c','u','c'],['a','x','a'],['t','e','t']]
word='cat'
print (capitalize_word_in_crossword(crosswords,word))

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print (capitalize_word_in_crossword(crosswords,word))