# 模块功能：
# 一个保存了400W条分词后的中文文本数据的文件，每条数据大概200-400个词，
# 现在需要统计输出总共的词汇量。
import os
from tqdm import tqdm
from collections import Counter

def get_sentence_words(path):
    files = os.listdir(path)  # os.listdir() 用于返回指定的文件夹包含的文件
    for file in files:
        file_path = os.path.join(path, file)  # 将多个路径组合后返回
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in tqdm(f, desc='read sentence_cuts'):  # tqdm可以不用,desc为进度条的标题
                line = line.strip().split('\t')
                # print(line)
                for s in line[1]:
                    if '\u4e00' <= s <= '\u9fff':
                        yield s
                # for word in line:
                #     if word[0] == "I":
                #         continue
                #     else:
                #         for s in word:
                #             if '\u4e00' <= s <= '\u9fff':
                #                 yield s

if __name__ == '__main__':
    words_gen = get_sentence_words('dataset')

    weight_dict = Counter(words_gen)  # counter() 计数，统计词频
    print('(中文个数)len(weight_dict)', len(weight_dict))
    total = 0
    for v in weight_dict.values():
        total += v
    print('(总字数)total words is %d' % total)

    print(weight_dict)
