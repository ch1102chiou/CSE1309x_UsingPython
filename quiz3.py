## 1-1
count = 0
for x in range(2,5):
    count = count + x
print(count)

## 1-2
k = 10
while k > 2:
    x = k / 2
    k = k - 1
print(x)

## 1-3
count = 10
for x in range(0,7):
    count = count + 2
    if x == 4:
        break
print(count)


## 1-4
k = 1
count = 0
while count < 10:
    if k % 4 == 0:
        break
    count = count + k
    k = k + 1
print(count)

## 1-5
my_list = ["pet" ,"dog", 35, "cat", 23]
count = 0
for item in my_list:
    if type(item)== str:
        continue
    count = count + 1
print(count)

## 1-6
m = 0
my_str= "mississipi"
for char in my_str:
    if char == "s":
        continue
    if char == "p":
        break
    m = m +1
print(m)

## 1-7
m = 0
for x in range (4,6):
   for y in range (2,4):
      m = m + x + y
print (m)

## 1- 8
m = 0
x = 1
while x < 5:
    y = 1
    while y < 4:
        m = m + y
        y = y + 3
    x = x + 2
print(m)

## 1-9
m = 0
my_list_1 = [1, 2, 5]
my_list_2 = [1, 3, 2, 6, 5]
for x in my_list_1:
    for y in my_list_2:
        if x == y :
            m = m + 1
print (m)

## 1-10
m = 0
my_str_1 = "cat"
my_str_2 = "pet"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 != char_2:
            m = m + 1
print(m)

##################################################################################################################
print ("########################################################################################################")
##################################################################################################################

## 2-1
def say_hello():
    print('Hello World!') 
say_hello()

# 2-2
def func2(x):
    x = 2
    print('x is', x)
func2(50)

# 2-3
def even3(x):
    if x % 2 == 0:
        return x
    else:
        return x+1
print(even3(3))

# 2-4
def cube4(x):
    return x * x * x   
y = cube4(3)    
print(y)

# 2-5
"""
def fun5(x, y, z): 
    z = x * y
    return x + y + z
print(fun5(2, 30)) <- Error because of invalid parameter.
"""
print ("Error")


# 2-6
def find_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
find_max(3, 4)

# 2-7
def my_fun7(x):
    count = 0
    for str in x:
        if str == "cat":
            count = count + 1
        elif str == "dog":
            count = count - 1
    return count
z = ['cat', 2, 'cat', 'dog', 34, 'cat'] 
print(my_fun7(z))


# 2-8
def myFun():
    count = 0
    for x in range (0,3): 
        count = count + x
    return 
print(myFun())

# 2-9
def fun1(x,y):
   z = multiply(x,y)
   m = x + z
   return m
  
def multiply(a,b):
   n = a * b
   return n
  
x = 2
y = 4
z = fun1(x,y)
print (x,y,z)

# 2-10
def my_fun(x):
    for m in range(0,3):
        n = 2
        while n <= 4:
            if m == n:
                x = x + 1
            n = n + 1
    return x
print(my_fun(5))

##################################################################################################################
print ("########################################################################################################")
##################################################################################################################

## 3
l = int(input())
index = 1
## Compute the total height, it should be 2*l - 1
totalHeight = 2*l - 1
while index <= totalHeight:
    if index <= l:
        numberOfStar = index
    else:
        numberOfStar = l - (index - l)
    for i in range(numberOfStar):
        print("*", end="")
    index = index + 1
    ## If it is NOT the final iteration, print the newline.
    if index <= totalHeight:
        print()

##################################################################################################################
print ()
print ("########################################################################################################")
##################################################################################################################


## 4
def sumlist(p):
    oddsum = 0
    for i in p:
        if i % 2 != 0:
            oddsum = oddsum + i
    return oddsum


## 5
def checkPerfectNumber(num):
    ## Search from 1 ~ num
    divsum = 0
    for i in range(1, num):
        if num % i == 0:
            divsum = divsum + i
    if divsum == num:
        return True
    else:
        return False

##################################################################################################################
print ("########################################################################################################")
##################################################################################################################

## 6
def checkPrime(num):
    # return false if number is equal to 1 or 1
    if num == 0 or num == 1:
        return False
    ## Search from 1 ~ num
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

##################################################################################################################
print ("########################################################################################################")
##################################################################################################################


## 7
def caculateLCM(a,b):
    def caculateGCD(a,b):
        if a == b:
            return a
        elif a > b:
            return caculateGCD(a - b, b)
        else:
            return caculateGCD(a , b - a)
    return int(a * b / caculateGCD(a , b))
print (caculateLCM(4,6))


##################################################################################################################
print ("########################################################################################################")
##################################################################################################################

## 8


def chickensAndDogs(heads,legs):
    # let x = checkins, y = dogs
    # x + y = heads
    #     2x + 4y = legs
    #  -) 2x + 2y = 2*heads
    #---------------------------
    #          2y = legs - 2 * heads
    #          y  = legs/2 - heads
    #          x  = heads - y
    # if x or y is negative, return None

    # Bad data check, heads, legs < 0 or legs is odd is invalid
    if heads < 0 or legs < 0 or legs % 2 !=0:
        return None
    dogs = legs/2 - heads
    checkins = heads - dogs
    if dogs < 0 or checkins < 0:
        return None
    else:
        return [int(checkins), int(dogs)]
print (chickensAndDogs(5,12))
print (chickensAndDogs(7,12))