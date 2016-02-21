# part 1.1
x = ["dog", 2, "cat", 34, 5.8]
m = 0
for i in range(len(x)):
    m = m + i
print ("part 1.1")
print(m)


# part 1.2
def my_fun2(x,y):
    m = x ** y  
y = my_fun2(2, 3)    
print ("part 1.2")
print(y)

# part 1.3
i = 1
while False:
    if i % 5 == 0:
        break
    i = i + 2
print ("part 1.3")
print(i)

# part 1.4
count = 0
list_1 = []
for i in range(1,4):
    list_1.append(i**2)
for x in list_1:
    count = count + x
print ("part 1.4")
print(count)


# part 1.5
def my_fun5(a):
    a[0] = 'new value:'     
    a[1] = a[1] + 1      

x = ['old value:', 99]
my_fun5(x)
print ("part 1.5")
print (x[0], x[1])


# part 1.6
x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
count = 0
for item in x:
    m = 0
    if item == "pet" or item == 3:
        m = x.index(item)
        count = count + m
print ("part 1.6")
print(count)


# part 1.7
count = 0
my_list = [2, 4, 1, 5, 7, 3, 9, 4]
new_list = my_list[1:7:2]
for item in new_list:
    count = count + 1
print ("part 1.7")
print(count)

# part 1.8
x = 0
my_list = []
while x < 10:
    if x % 2 == 0:
        my_list.append("dog")
    elif x % 3 == 0:
        my_list.remove("dog")
    x = x + 1
print ("part 1.8")
print(my_list.count("dog"))

# part 1.9
list_1 = ["dog", 3, "cat" , 25, 2.4]
list_2 = ["car", 25, "dog" , 43]
count = 0
for item in list_1:
    if item in list_2:
        count = count + 1
print ("part 1.9")
print (count)


# part 1.10
def my_fun10(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print ("part 1.10")
print (my_fun10(y))





