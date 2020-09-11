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










