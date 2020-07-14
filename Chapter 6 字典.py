# 第六章 字典
# 字典用放在方括号中的一系列键值对表示
alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])  # green
print(alien_0['point'])  # 5

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # {'color': 'green', 'point': 5, 'x_position': 0, 'y_position': 25}

# 删除键-值对
alien_0 = {'color': 'green', 'point': 5}
del alien_0['point']
print(alien_0)  # {'color': 'green'}
# 遍历字典--dic.items()
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_language.items():
    print(name.title() + " -> " + language)
# Jen -> python
# Sarah -> c
# Edward -> ruby
# Phil -> python

# items()方法返回一个键-值对列表(list)
print(favorite_language.items())  # dict_items([('jen', 'python'), ('sarah', 'c'), ('edward', 'ruby'), ('phil', 'python')])
# 遍历字典中所有的键--dic.keys()
for i in favorite_language:  # 遍历字典时，会默认遍历所有的键
    print(i, end=' ')  # jen sarah edward phil
print()
for name in favorite_language.keys():
    print(name, end=' ')  # jen sarah edward phil
print()

if 'phil' not in favorite_language.keys():
    print('phil no')
else:
    print('phil yes')  # phil yes
# 按顺序遍历字典中的所有键
for name in sorted(favorite_language.keys()):
    print(name.title(), end=' ')  # Edward Jen Phil Sarah
print()
# 遍历字典中的所有值--dic.values()
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for language in favorite_language.values():
    print(language, end=' ')  # python c ruby python
print()
# 对列表使用set()，可剔除重复项
for language in set(favorite_language.values()):
    print(language.title(), end=' ')  # Ruby C Python (与原list的相对位置可能会发生改变，因为set是无序的)
print()

language = list(language for language in favorite_language.values())  # python c ruby python
language2 = list(set(language))  # C Ruby Python
language2.sort(key=language.index)  # 按原序重新排列
for i in language2:
    print(i, end=' ')  # python c ruby
print()
# 字典列表
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# {'color': 'green', 'point': 5}
# {'color': 'yellow', 'point': 10}
# {'color': 'red', 'point': 15}

# 在字典中存储列表
favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_language.items():
    if len(languages) == 1:
        print(name.title() + "'s favorite language is:\n\t" + languages)
    else:
        print(name.title() + "'s favorite languages are:")
        for i in languages:
            print("\t" + i)
# Jen's favorite languages are:
# 	python
# 	ruby
# Sarah's favorite language is:
# 	c
# Phil's favorite languages are:
# 	python
# 	haskell

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
for username, user_info in users.items():
    print("Username: " + username)
    print("\tFull Name: " + user_info['first'] + " " + user_info['last'])
    print("\tLocation: " + user_info['location'] + "\n")
# Username: aeinstein
# 	Full Name: albert einstein
# 	Location: princeton
#
# Username: mcurie
# 	Full Name: marie curie
# 	Location: paris
#








