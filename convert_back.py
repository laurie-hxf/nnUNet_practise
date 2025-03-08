import os
import numpy as np
from PIL import Image

# 设置你的文件夹路径
folder = "/Users/laurie/Documents/nnunet_train/nnUNet/nnUNet_raw/Dataset001_avrdb/ouput"

for filename in os.listdir(folder):
    if filename.lower().endswith('.png'):
        filepath = os.path.join(folder, filename)
        img = Image.open(filepath)
        # 如果图片不是RGB模式，可先转换：img = img.convert("RGB")
        img_array = np.array(img)
        # 将所有像素值为1的元素替换为255
        img_array[img_array == 1] = 255
        # 转换回图片对象并保存覆盖原文件
        new_img = Image.fromarray(img_array)
        new_img.save(filepath)
