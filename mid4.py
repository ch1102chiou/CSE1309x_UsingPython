def list_of_primes(n):

    ## Quiz 3 Function
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

    primes_list = []
    for i in range(2,n):
        if checkPrime(i) == True:
            primes_list.append(i)

    return primes_list


print (list_of_primes(20))
