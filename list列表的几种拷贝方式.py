import copy

a = [[1, 2], 10, 20]

a1 = a  # 第1种
a2 = a[:]  # 第2种
a3 = list(a)  # 第3种
a4 = a * 1  # 第4种
a5 = copy.copy(a)  # 第5种
a6 = [x for x in a]  # 第6种
a7 = copy.deepcopy(a)  # 第7种

a.append(30)
a[0].append(3)

print('a:', a)
print('a1:', a1)
print('a2:', a2)
print('a3:', a3)
print('a4:', a4)
print('a5:', a5)
print('a6:', a6)
print('a7:', a7)
# ->
a: [[1, 2, 3], 10, 20, 30]
a1: [[1, 2, 3], 10, 20, 30]
a2: [[1, 2, 3], 10, 20]
a3: [[1, 2, 3], 10, 20]
a4: [[1, 2, 3], 10, 20]
a5: [[1, 2, 3], 10, 20]
a6: [[1, 2, 3], 10, 20]
a7: [[1, 2], 10, 20]

# a1 = a 表示 a1 和 a 指向同一个内存地址，只是名称不同。

# a2~a6 则是指向不同的列表，因为创建新的列表，所以原列表发生改变时，拷贝列表不变，但是里面元素本身的地址并没有改变，
# 所以如果子元素为列表时，子元素列表在拷贝时地址并不会发生变化，所以当原列表中子列表发生改变时，拷贝列表同样会发生改变。

# a7 是深度拷贝，所以无论列表中嵌套了几层列表，拷贝列表都不会随着原列表的改变而改变。