# 第十六章 下载数据
import csv
from matplotlib import pyplot as plt

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)

#     for index, column_header in enumerate(header_now):
#         print(index, column_header)

    highs = []
    for row in reader:
        highs.append(row[1])
    print(highs)
    """
    [64, 71, 64, 59, 69, 62, 61, 55, 57, 61, 57, 59, 57, 61, 64, 61, 59, 63, 60, 57, 69, 63, 62, 59, 57, 57, 61, 59, 61, 61, 66]
    """
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    # 设置图形的格式
    plt.title("Daily high temperatures, July 2014")
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
