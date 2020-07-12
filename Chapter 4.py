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