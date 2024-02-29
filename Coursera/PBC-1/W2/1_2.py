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
print(five_hund,one_hund,fifty,ten,five,remain,sep=' ')
