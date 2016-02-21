
digitalDic = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
}

digitalTensDic = {
 2:"twenty",
 3:"thirty",
 4:"forty",
 5:"fifty",
 6:"sixty",
 7:"seventy",
 8:"eighty",
 9:"ninety",
}

digitalEleven2NinteenDic = {
 11:"eleven",
 12:"twelve",
 13:"thirteen",
 14:"fourteen",
 15:"fifteen",
 16:"sixteen",
 17:"seventeen",
 18:"eighteen",
 19:"nineteen"
}

n=int(input('please enter an integer between 1 and 9999: '))
remind = n
needSpace = False

def getEnd (a):
    # two thousand_one
    if a > 0:
        return " "
    # two thousand
    else:
        return ""

## Compute thousand
thousand = remind // 1000
if thousand:
    remind = remind - thousand * 1000
    print ("%s thousand" %(digitalDic[thousand]), end = getEnd(remind) )

## Compute hundred
hundred =  remind // 100
if hundred:
    remind = remind - hundred * 100
    print ("%s hundred" %(digitalDic[hundred]), end = getEnd(remind) )

## Compute tens and remind
tens = remind // 10
if tens >= 2:
    remind = remind - tens * 10
    print ("%s" %(digitalTensDic[tens]), end = getEnd(remind)  )
    print ("%s" %(digitalDic[remind]), end = getEnd(0))
elif tens == 1:
    print ("%s" %(digitalEleven2NinteenDic[remind]), end = getEnd(0))
else:
    print ("%s" %(digitalDic[remind]), end = getEnd(0))


## Final End of Line
print("")



