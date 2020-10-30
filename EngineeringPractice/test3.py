import PIL.Image as Image
import numpy as np
import os

IMAGES_PATH = 'C:\\Users\\kdjlyy\\Desktop\\slides\\EngineeringPractice\\DataSet\\pictures\\'  # 图片集地址

IMAGES_FORMAT = ['.png']  # 图片格式

IMAGE_SIZE_W = 60  # 每张小图片的宽
IMAGE_SIZE_H = 60  # 每张小图片的高

IMAGE_ROW = 3  # 行

IMAGE_COLUMN = 10  # 列

IMAGE_SAVE_PATH = 'final4.jpg'  # 图片转换后的地址

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
print(len(image_names))

# 简单的对于参数的设定和实际图片集的大小进行数量判断
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成图片的参数和要求的数量不能匹配！")


# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE_W, 2 * IMAGE_ROW * IMAGE_SIZE_H))  # 创建一个新图

    # 循环遍历，把每张图片按顺序粘贴到对应位置上

    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE_W, IMAGE_SIZE_H), Image.ANTIALIAS)  # 重塑（统一）照片的大小

            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE_W, (y - 1) * IMAGE_SIZE_H))
            # im.paste(image, position)---粘贴image到im的position（左上角）位置。

    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


image_compose()
