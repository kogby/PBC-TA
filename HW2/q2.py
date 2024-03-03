'''
This is a Ｍathematical Programming problem, and it may be solved with KKT condition.
In this problem, we are only required to do greed search.
'''

price_red = int(input())
price_white = int(input())
budget = int(input())

best_obj = 0
for white_num in range(0, 76):
    for red_num in range(white_num * 2, 101):
        if (red_num * price_red + white_num * price_white) > budget:
            break
        obj = (200 - red_num) * red_num + (300 - 2 * white_num) * white_num
        best_obj = obj if obj > best_obj else best_obj

print(best_obj)
