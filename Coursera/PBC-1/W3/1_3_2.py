pay = int(input())
to_give = 1000 - pay

five_hund = to_give // 500
remain = to_give % 500
one_hund = remain // 100
remain = remain % 100
fifty = remain // 50
remain = remain % 50
ten = remain // 10
remain = remain % 10
five = remain // 5
remain = remain % 5

first = True

if five_hund > 0:
    if first:
        first = False
    print("500,",five_hund,end='')
else:
    print("",end='')
if one_hund > 0 :
    if first:
        first = False
    else:
        print('; ',end='')
    print("100,",one_hund,end='')
else:
    print("",end='')

if fifty > 0 :
    if first:
        first = False
    else:
        print('; ',end='')
    print("50,", fifty, end='')
else:
    print("",end='')

if ten > 0 :
    if first:
        first = False
    else:
        print('; ',end='')
    print("10,", ten, end='')
else:
    print("", end='')

if five > 0 :
    if first:
        first = False
    else:
        print('; ',end='')
    print("5,",five,end='')
else:
    print("",end='')

if remain > 0 :
    if first:
        first = False
    else:
        print('; ',end='')
    print("1,",remain,end='')
else:
    print("",end='')
