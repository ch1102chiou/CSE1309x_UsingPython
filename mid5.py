def items_price(a, b):
    totalprice = 0
    itemlist = zip(a,b)
    for quantities , eachprice in itemlist:
        totalprice = totalprice + quantities * eachprice
    return totalprice

a = [2, 3, 5, 7, 9]
b = [5, 8, 4, 1, 11]
print (items_price(a, b))