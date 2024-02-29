account_1 = int(input())
account_2 = int(input())
num = int(input())

account_2 += num if account_1 >= num else account_1
account_1 -= num if account_1 >= num else account_1
print(account_1, account_2)