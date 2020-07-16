##############
# 第五章 if语句
##############
cars = ['audi', 'bmw', 'subaru', 'toyato']
for car in cars:
    if car == 'bmw':
        print(car.upper(), end=' ')
    else:
        print(car.title(), end=' ')  # Audi BMW Subaru Toyato

# 检查多个条件 and = &&  or = ||
age_0 = 21
age_1 = 22
print(age_0 >= 20 and age_1 >= 20)  # True
print(age_0 <=20 or age_1 > 23)  # False
# 用关键字in（not in）判断特定的值是否在（不在）列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('onions' in requested_toppings)  # True
print('pineapple' not in requested_toppings)  # False
###################################
empty_list = []
if empty_list:
    print("Not empty list")
else:
    print("Empty list")  # Empty list

available = [num for num in range(1, 11)]
requested = [3, 5, 9, 11]
for request in requested:
    if request in available:
        print(str(request) + ' -> #_#')
    else:
        print(str(request) + ' -> !_!')
# 3 -> #_#
# 5 -> #_#
# 9 -> #_#
# 11 -> !_!
