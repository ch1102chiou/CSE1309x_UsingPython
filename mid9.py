def find_gcd(some_list):
    # Quiz fucntion
    def caculateGCD(a,b):
        if a == b:
            return a
        elif a > b:
            return caculateGCD(a - b, b)
        else:
            return caculateGCD(a , b - a)

    gcd = some_list[0]

    for index in range(1, len(some_list)):
        gcd = caculateGCD (gcd, some_list[index])

    return gcd

print (find_gcd([12, 24, 6, 18]))
print (find_gcd([3, 5, 9, 11, 13]))