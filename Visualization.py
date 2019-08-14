import os,sys
from PIL import Image
from dominant_color import get_dominant_color,plot_dominant_color
import numpy as np

def read_file(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir) :
        for file in files:
            if 'tif' in file:
                # print(root + file)  # 当前目录路径
                # print(file)  # 当前路径下所有非目录子文件
                file_list.append(str(root + '//' +  file))
    return file_list

if __name__=='__main__':
    # file_dir = '/cptjack/totem/Colon Pathology/openslide_test/ICIAR2018_BACH_Challenge/Train/Photos/'
    file_dir = 'E://biototem//main_color'
    file_list = read_file(file_dir)
    color_x, color_y, color_z = [],[],[]
    for img_file in file_list:
        image = Image.open(img_file)
        dominant_color = get_dominant_color(img_file)
        color_x.append(dominant_color[0])
        color_y.append(dominant_color[1])
        color_z.append(dominant_color[2])
    print(np.array([color_x,color_y,color_z]).T)
    plot_dominant_color([color_x,color_y,color_z])
