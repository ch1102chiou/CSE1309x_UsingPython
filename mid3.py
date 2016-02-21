def find_integer_with_most_divisors(input_list):
    def getDivCount(n):
        div = 1
        cnt = 0
        while div <= n:
            if n % div == 0:
                cnt = cnt + 1
            div = div + 1
        return cnt
    MaxDivCount = -1
    MostDivisors = None
    for i in input_list:
        itemDivCount = getDivCount(i)
        if itemDivCount > MaxDivCount:
            MostDivisors = i
            MaxDivCount = itemDivCount
    return MostDivisors




print (find_integer_with_most_divisors([8,12,18,6]))