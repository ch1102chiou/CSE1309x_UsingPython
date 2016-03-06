# 1-1
my_list = [[3,4],[6,7],[10,12]]
print(my_list[0:2])

# 1-2
my_list = [[3,5,6], [6,4,2], [9,4,8]]
for k in range (len(my_list)):
    my_list[k][0] = 1
print(my_list)

# 1-3
my_list = [[6,2],[3,9,5]]
x = 0
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        x = x + my_list[m][k] 
print(x)

# 1-4
my_list = []
for m in range(0,2):
    new_list = []
    for k in range(4,6):
        new_list.append(k)
    my_list.append(new_list)
print(my_list)

# 1-5
my_list = [[3,5],[2,9],[4,7]]
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        my_list[m][k] = my_list[m][k] * 2
print(my_list)

# 1-6
numbers={1: "uno", 3:"two", "tres":3}
print(numbers.pop(3))


# 1-7
numbers={"one": [1,"uno"], "two": [2,"dos"]}
print (numbers["two"][1][2])

print ("Error")
""" Key Error
# 1-8
d={1:"one", "two": 2 , 3: "tres"}
print (d[2])
"""

# 1-9
d={1:"one", "two": 2 , 3: "tres"}
print (d.get(2))

print ("Error")
""" unhashable type as a key
# 1-10
numbers = {["one","two"]: 1, "two": 2}
print(numbers)
"""


def row_maximums(some_multi_dimensional_list):
    max_dict = {}
    for i in range(len(some_multi_dimensional_list)):
        # minimum value for 32-bit integer
        max_num = -2147483648
        for j in range(len(some_multi_dimensional_list[i])):
            if some_multi_dimensional_list[i][j] > max_num:
                max_num = some_multi_dimensional_list[i][j]
        key = "row %d max" %(i)
        val = max_num
        max_dict[key] = val
    return max_dict


"""
matrix = [[5, 0, 0, 0, 13],
 [0, 12, 0, 0],
 [20, 0, 11, 0],
  [6, 0, 0, 8]]


print (row_maximums(matrix))
"""


def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    score_dict = {}
    def checkScore(score):
        if score >= 60:
            return 'pass'
        else:
            return 'fail'

    for name, age, score in zip(names_list, ages_list, scores_list):
        score_dict[name] = [age, score, checkScore(score)]
    return score_dict


"""
test =  (["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60])
print (construct_dictionary_from_lists(test[0], test[1], test[2]))
"""

# Type your code here
def one_to_2D(some_list, r, c):    
    # initialize matrix create
    twoD = [[] for i in range(r)]
    for index in range(r*c):
        if index < len(some_list):
            twoD[index//c].append(some_list[index])
        else:
            twoD[index//c].append(None)
    return twoD

print (one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3))

# Type your code here
# Review functional language!!
def multiplication_table(n):
    return [[i*j for i in range(1,n+1)] for j in range(1,n+1)] 

"""
print (multiplication_table(4))
"""