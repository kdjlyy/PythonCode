# 第八章 函数

def greet():
    print("Hello!")
greet()  # Hello!

def greet2(username):
    print("Hello " + username.title() + "!")
greet2("jesse")  # Hello Jesse!

# 传递实参：①位置实参 ②关键字实参 ③默认值
#  ①位置实参:函数定义中的形参是基于实参的顺序。
def multiply(n1, n2):
    print(str(n1) + " * " + str(n2) + " = " + str(n1*n2))
multiply(11, 11)  # 11 * 11 = 121
#  ②关键字实参:传递给函数的是 名称-值 对。
multiply(n1=12, n2=12)  # 12 * 12 = 144

#  ③默认值
def describe_pet(pet_name, pet_type='cat'):  # 带默认值的形参应该放在最后
    print("I have a " + pet_type + ", named " + pet_name + ".")
describe_pet("猪皮")
describe_pet(pet_name="猪皮")
describe_pet("二狗", "dog")
describe_pet(pet_type="狗子", pet_name="二狗")
# I have a cat, named 猪皮.
# I have a cat, named 猪皮.
# I have a dog, named 二狗.
# I have a 狗子, named 二狗.

# 返回值
