# 第二章 变量和简单数据类型
message = "hello python world!"
print(message.title())  # Hello Python World!
print(message.upper())  # HELLO PYTHON WORLD!
print(message.lower())  # hello python world!
##################################################
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)  # ada lovelace
print("Hello, " + full_name.title() + "!")  # Hello, Ada Lovelace!
message = "Hello, " + full_name.title() + "!"
print(message)  # Hello, Ada Lovelace!
##################################################
print("\n\tPython")
##################################################
# strip() 删除字符串两端空白部分
# lstrip() 删除字符串开头空白部分
# rstrip() 删除字符串末尾空白部分
favorite_language = "  Python Language "
print(favorite_language.strip())  # Python Language
print(favorite_language.lstrip())  # Python Language
print(favorite_language.rstrip())  # __Python Language
print(favorite_language.replace(" ", ""))  # PythonLanguage

age = 21
message = "Happy " + str(age) + "rd Birthday!"
print(message)
