import matplotlib.pyplot as plt
from random import choice


class RandowWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 所有漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，达到指定的次数
        while len(self.x_values) < self.num_points:
            # 决定前进方向及距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = RandowWalk()
rw.fill_walk()

# 设置绘图窗口的尺寸
plt.figure(figsize=(10, 6))

"""
不着色的绘图
plt.scatter(rw.x_values, rw.y_values, s=10)
"""

# 使用颜色映射给点着色
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=10)

# 突出显示起点和终点
plt.scatter(0, 0, c='orange', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

