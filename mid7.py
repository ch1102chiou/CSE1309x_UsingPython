def pattern_sum(a, b):
    pat = ''
    pat_sum = 0
    for i in range(b):
        pat = pat + str(a)
        pat_sum = pat_sum + int(pat)
    return pat_sum
print (pattern_sum(4, 5))
print (pattern_sum(5, 3))