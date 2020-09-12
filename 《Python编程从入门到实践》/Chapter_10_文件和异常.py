# 第十章 文件和异常
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)
"""
3.1415926535
  8979323846
  2643383279

"""
with open("pi_digits.txt") as file_object:
    for line in file_object:
        print(line.rstrip())  # rstrip()消除末尾空字符串
"""
3.1415926535
  8979323846
  2643383279
"""

# 创建一个包含文件各行内容的列表
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)  # ['3.1415926535\n', '  8979323846\n', '  2643383279\n']
for line in lines:
    print(line.rstrip())
"""
3.1415926535
  8979323846
  2643383279
"""
pi_string = ''
for line in lines:
    pi_string += line.strip()  # 用strip()就可以除去两边的空格
print(pi_string)
print(len(pi_string))
"""
3.141592653589793238462643383279
32
"""

# 写入文件
"""
open(filename, 'r/w/a/r+')提供了两个实参，第二个参数可以指定
只读模式('r')，未填写第二个参数默认为只读模式
写入模式('w')
附加模式('a')
读取和写入模式('r+')
"""


def read_content(file_name):
    with open(file_name) as file_contents:
        data = file_contents.read()
        print(data)


with open("programming.txt", "w") as file_object:
    file_object.write("*_*  *_*")
read_content("programming.txt")  # *_*  *_*

# 写入多行
filename = "programming.txt"
with open(filename, 'w') as file_object:
    file_object.write("I Love programming.")
    file_object.write("I Love creating new games.")
"""I Love programming.I Love creating new games."""
# write()函数不会在写入的文本末尾添加换行符，要想写入多行时可能不是想象的那样。

with open(filename, 'w') as file_object:
    file_object.write("I Love programming.\n")
    file_object.write("I Love creating new games.")
"""
I Love programming.
I Love creating new games.
"""

# 附加到文件(write()写入时不会覆盖之前的内容)
with open(filename, 'a') as file_object:
    file_object.write("\nThis is appended message.")
"""
I Love programming.
I Love creating new games.
This is appended message.
"""


# 异常 -- 使用try-except代码块
print("\nInput 2 number to divide them, 'q' to quit.")
while True:
    a = input("first num:")
    if a == 'q':
        break
    b = input("second number:")
    try:
        ans = int(a) / int(b)
    except ZeroDivisionError:
        print("can't divide by 0!")
    else:
        print(ans)
"""
Input 2 number to divide them, 'q' to quit.
first num:9
second number:3
3.0
first num:5
second number:0
can't divide by 0!
first num:q
"""

# 分析文本
title = "Alice in Wonderland"
print(title.split())
"""
['Alice', 'in', 'Wonderland']
"""
# split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）

# # 使用多个文件


def cnt_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        # print(words)
        ans = len(words)
        print("The file " + filename + " has " + str(ans) + " words.")


filename = "Alice.txt"
cnt_words(filename)
"""
The file Alice.txt has 65 words.
"""


filenames = ['Alice.txt', 'NotExist.txt', 'programming.txt']
for filename in filenames:
    cnt_words(filename)
"""
The file Alice.txt has 65 words.
The file NotExist.txt does not exist.
The file programming.txt has 12 words.
"""


"""
失败时一声不吭
try:
    --snip--
except:
    pass  # 这里用pass语句让python什么都不要做
else:
    --snip--
"""


# 存储数据

# json.dump(x, y) 将x存入y中， 配合json.load()
import json
number = [2, 3, 5, 7, 11, 13]
filename = "numbers.json"
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

with open(filename) as f_obj:
    num = json.load(f_obj)
    print(num)
"""
[2, 3, 5, 7, 11, 13]
"""






