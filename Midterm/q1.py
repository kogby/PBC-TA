nums = [int(i) for i in input().split(",")]
a, b, c = nums

if a * b == c:
    print(a * b)
elif a * c == b:
    print(a * c)
elif b * c == a:
    print(b * c)
else:
    print(a * b * c)
