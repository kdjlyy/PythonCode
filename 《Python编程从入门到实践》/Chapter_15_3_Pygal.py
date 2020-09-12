"""
pygal是一个SVG图表库。SVG是一种矢量图格式。全称Scalable Vector Graphics -- 可缩放矢量图形。
"""
import pygal

# 用Pygal模拟掷骰子
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)  # randint(x, y)返回[x, y]之间随机整数


die = Die()
res = []
for roll_num in range(1000):
    ans = die.roll()
    res.append(ans)
# print(res)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = res.count(value)  # count [1-6]
    frequencies.append(frequency)

print(frequencies)
"""
[166, 158, 165, 163, 180, 168]
"""

# 绘制直方图
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')  # 选染成svg文件


# 同时掷两枚D6骰子
die1 = Die()
die2 = Die()
res = []
for roll_num in range(1000):
    ans = die1.roll() + die2.roll()
    res.append(ans)

frequencies = []
for value in range(2, die1.num_sides+die2.num_sides+1):
    frequency = res.count(value)
    frequencies.append(frequency)
print(frequencies)
"""
[32, 60, 94, 98, 135, 159, 146, 100, 93, 49, 34]
"""
hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')  # 选染成svg文件




