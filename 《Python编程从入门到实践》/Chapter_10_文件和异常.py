# 第十章 文件和异常
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())  # rstrip()消除末尾空字符串
# 3.1415926535
# 8979323846
# 2643383279
