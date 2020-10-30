import os
import numpy as np
import struct
from PIL import Image

# C:\Users\kdjlyy\Desktop\电子书(课件)\工程实践\数据集\HWDB1.1\HWDB1.1trn\1001.mpf
# C:\Users\kdjlyy\Desktop\slides\EngineeringPractice\DataSet\1.1_png


if __name__ == "__main__":
    # f = open("C:\\Users\\kdjlyy\\Desktop\\电子书(课件)\\工程实践\\数据集\\HWDB1.1\\HWDB1.1trn\\1001.mpf", 'rb')
    f = open('C:\\Users\\kdjlyy\\Desktop\\slides\\EngineeringPractice\\DataSet\\1.1\\1001-f.gnt', 'rb')
    header_size = 10
    while True:
        header = np.fromfile(f, dtype='uint8', count=header_size)
        if not header.size:
            break

        sample_size = header[0] + (header[1] << 8) + (header[2] << 16) + (header[3] << 24)
        tagcode = header[5] + (header[4] << 8)
        width = header[6] + (header[7] << 8)
        height = header[8] + (header[9] << 8)
        if header_size + width * height != sample_size:
            break

        image = np.fromfile(f, dtype='uint8', count=width * height).reshape((height, width))
        tagcode_unicode = str(struct.pack('>H', tagcode).decode('gbk')).rstrip("\00")  # 图片对应的汉字
        im = Image.fromarray(image)

        if tagcode_unicode in ['"', '/', '\\', ':', '*', '?', ':', '>', '<', '|', '.']:
            tagcode_unicode = "symbol"

        file_dir = "C:\\Users\\kdjlyy\\Desktop\\slides\\EngineeringPractice\\DataSet\\1.1_png\\" + tagcode_unicode
        # print(file_dir)
        #
        # os.mkdir(file_dir)

        if not os.path.exists(file_dir):
            print(file_dir)
            os.mkdir(file_dir)

        file_lists = os.listdir(file_dir)

        im.convert('RGB').save(file_dir + '\\' + str(len(file_lists)) + '.png')

