# 第四章 操作列表
# 4.1 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# alice
# david
# carolina

# 4.3 创建数字列表
# range()能轻松生成一系列的数字，注意区间为"[a,b)"
for value in range(1, 5):
    print(value, end="")  # 1234

numbers = list(range(1,6))
print(numbers)  # [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))
print(even_numbers)  # [2, 4, 6, 8, 10]

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

digits = [value for value in range(1, 11)]  # 列表解析
print(digits)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("minimum:" + str(min(digits)) + " maximum:" + str(max(digits)) + \
      " sum:" + str(sum(digits)))  # minimum:1 maximum:10 sum:55
# 列表切片、遍历、复制
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])  # ['charles', 'martina', 'michael']
print(players[1:4])  # ['martina', 'michael', 'florence']
print(players[2:])  # ['michael', 'florence', 'eli']
print(players[-2:])  # ['florence', 'eli']
#############################################################
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 创建一个包含整个列表的切片
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My foods:" + str(my_foods))  # My foods:['pizza', 'falafel', 'carrot cake', 'cannoli']
print("Friend's foods:" + str(friend_foods))  # Friend's foods:['pizza', 'falafel', 'carrot cake', 'ice cream']

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # 这行不通
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My foods:" + str(my_foods))  # My foods:['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("Friend's foods:" + str(friend_foods))  # Friend's foods:['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
#############################################################
# 元组
# 不可变的列表（list），不能修改元组的值，但是能给元组变量赋值
dimensions = (200, 50, 40, 75)  # 使用圆括号标识元组
print(dimensions[0])  # 200
# 错误操作：dimensions[0] = 100
for dimension in dimensions:
    print(dimension, end=' ')  # 200 50 40 75

print("\nOriginal dimensions:" + str(dimensions))  # Original dimensions:(200, 50, 40, 75)
dimensions = (1, 2, 3)
print("Modified dimensions:" + str(dimensions))  # Modified dimensions:(1, 2, 3)

