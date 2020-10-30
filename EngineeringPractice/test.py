import PIL.Image as Image
import os

IMAGES_PATH = 'C:\\Users\\kdjlyy\\Desktop\\slides\\EngineeringPractice\\DataSet\\pictures\\'  # 图片集地址
IMAGES_FORMAT = ['.png', '.jpg', '.JPG']  # 图片格式
IMAGE_SIZE_W = 50  # 每张小图片的宽
IMAGE_SIZE_H = 50  # 每张小图片的高
IMAGE_SAVE_PATH = 'final.jpg'  # 图片转换后的地址

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if os.path.splitext(name)[1] == item]
IMAGE_ROW = len(image_names) // 3+ 1  # 图片间隔，也就是合并成一张图后，一共有几行，在这里行是自适应的
IMAGE_COLUMN = 6  # 图片间隔，也就是合并成一张图后，一共有几列


# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE_W, IMAGE_ROW * IMAGE_SIZE_H))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上（除去最后一行）
    for y in range(1, IMAGE_ROW):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE_W, IMAGE_SIZE_H), Image.ANTIALIAS)  # 重塑（统一）照片的大小
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE_W, (y - 1) * IMAGE_SIZE_H))
            # im.paste(image, position)---粘贴image到im的position（左上角）位置。

    # 最后一行照片特殊处理
    for x in range(1, len(image_names) - IMAGE_COLUMN * (IMAGE_ROW - 1) + 1):
        from_image1 = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (IMAGE_ROW - 1) + x - 1]).resize(
            (IMAGE_SIZE_W, IMAGE_SIZE_H), Image.ANTIALIAS)  # 重塑照片的大小

        to_image.paste(from_image1, ((x - 1) * IMAGE_SIZE_W, (IMAGE_ROW - 1) * IMAGE_SIZE_H))

    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


image_compose()  # 调用函数

