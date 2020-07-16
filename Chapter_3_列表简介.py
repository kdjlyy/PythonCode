# 第三章 列表简介
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])  # trek
print(bicycles[0].title())  # Trek
print(bicycles[-1])  # specialized
########################################################
# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
# 在列表中添加元素 append()、insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  # insert()将‘ducati’存储到0这个位置
print(motorcycles)  # ['ducati', 'honda', 'yamaha', 'suzuki']
#从列表中删除元素 del语句、pop()、remove()
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  # ['yamaha', 'suzuki']

motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop()  # pop()可以弹出列表末尾元素
print(poped_motorcycle)  # suzuki
print(motorcycles)  # ['honda', 'yamaha']
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(1)  # pop(index)弹出列表任意位置元素
print(first_owned)  # yamaha
print(motorcycles)  # ['honda', 'suzuki']

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'ducati']
motorcycles.remove('ducati')  # 根据键值删除元素，remove()只删除第一个指定的值
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'ducati']
# 组织列表的方式
# list.sort()对列表进行永久性排序、sorted(list)对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 错误写法：print(cars.sort())，因为sort()无返回值
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)  # 按字母顺序逆向排序
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))  # ['toyota', 'subaru', 'bmw', 'audi']
########################################################
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']
print(len(cars))  # 4





