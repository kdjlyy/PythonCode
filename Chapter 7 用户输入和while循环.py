# 第七章 用户输入和while循环
# 使用input()时，Python将用户输入解读为字符串， 可以用int()来转化
number = input("Please input a number：")
number = int(number)
if number % 2 == 0:
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")
# Please input a number：7
# 7 is odd.

# while循环
flag = True
while flag:
    number = input("Please input a number(number>0 and end with 0)：")
    number = int(number)
    if number == 0:
        flag = False  # 也可以用break
    elif number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")

# 使用while循环来处理列表和字典
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print("Verifying user: " + current_user)
print("Confirmed Users List: " + str(confirmed_users))
# Verifying user: candaces
# Verifying user: brain
# Verifying user: alice
# Confirmed Users List: ['candace', 'brain', 'alice']

# 删除包含特定值的所有列表元素
# 在Chpater 3中，学到了从列表中删除元素的方法：① del语句 ② pop() ③ remove()
# 用remove()可行是因为要删除的元素在列表中只出现了一次，要删除多个相同元素，可运用一个while循环
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)  # ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)  # ['dog', 'dog', 'goldfish', 'rabbit']

# 用户输入填充字典
message = {}
flag = True
while flag:
    name = input("Input your name:")
    num = input("Input a number:")
    message[name] = num
    tag = input("Keep on running? (yes or no):")
    if tag == 'no':
        for name, num in message.items():
            print(name + " -> " + num)
        break
# Input your name:Eric
# Input a number:12
# Keep on running? (yes or no):yes
# Input your name:Denali
# Input a number:666
# Keep on running? (yes or no):no
# Eric -> 12
# Denali -> 666
#










