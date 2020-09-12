import matplotlib.pyplot as plt

# input_value = [1, 2, 3, 4, 5]
# squares_value = [1, 4, 9, 16, 25]
# plt.plot(input_value, squares_value, linewidth=3)
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=14)
# plt.show()


# # scatter()绘制散点图
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.scatter(x_values, y_values, s=30)  # s=100规定点的尺寸
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', s=10)
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  # 颜色映射
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1000, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png')





