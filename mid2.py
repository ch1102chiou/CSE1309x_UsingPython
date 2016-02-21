# part 2.1
my_list = []
for k in range(1,101,20):
    my_list.append(k)
print ("part 2.1")
print (my_list[: :2] )


# part 2.2
def my_fun2(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [1,5,3]
my_fun2(m)
print ("part 2.2")
print(m)

#part 2.3
def my_fun3(x):
    for k in range (len(x)):
        x.append(x[:k])
m = [1,5,3]
print ("part 2.3")
my_fun3(m)
print(m)

#part 2.4
my_list = [9, 8, 7]
for k in range (3):
    my_list.insert(-k, k+1)
print ("part 2.4")
print(my_list)

#part 2.5
my_list = [12, "cat", 3.4, "dog", 62]
new_list = []
for k in range(5):
    if k % 2:
        m = my_list.pop(k)
        new_list.append(m)
print ("part 2.5")
print(new_list)


# part 2.6
def my_fun6(my_list,s,e):
    del (my_list[s:e])
 
values = [2, 9, 16, 3, 24, 13, 15]
my_fun6(values,-6,-4)
my_fun6(values,2,4)
print ("part 2.6")
print(values)

# part 2.7
def my_fun7(i):
    values = []
    values.append(i)
    return values
my_fun7(5)
print ("part 2.7")
print(my_fun7(3))



#part 2.8
def my_fun8(m):
    x = []
    for k in range(len(m)):
        if m[k] % 3 == 0 and m[k] % 2:
            x.insert(k, m[k])
    return x
 
values = [2, 9, 16, 3, 24, 13, 15]
print ("part 2.8")
print(my_fun8(values))


#part 2.9
def my_fun9(m, increment):
    x = 0
    while x < len(m):
        m[x] = m[x] + increment
        x = x + 1
    return m 

values = [4, 3, 7]
print ("part 2.9")
print(my_fun9(values, 2))


#part 2.10
def my_fun10(m):
    x = m[:]
    for k in x:
        if type(k) == int:
            m.remove(k)

values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
my_fun10(values)
print ("part 2.10")
print(values)














