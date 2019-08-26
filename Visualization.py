import os,sys
from PIL import Image
from dominant_color import get_dominant_color,plot_dominant_color
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from count_color import mean_std_hsv

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
    file_dir = "E://biototem//data/"
    file_list = read_file(file_dir)
    print(file_list)
    '''the domiant_color'''
    # color_x, color_y, color_z = [],[],[]
    # for img_file in tqdm(file_list):
    #     image = Image.open(img_file)
    #     dominant_color = get_dominant_color(img_file)
    #     color_x.append(dominant_color[0])
    #     color_y.append(dominant_color[1])
    #     color_z.append(dominant_color[2])
    # print(np.array([color_x,color_y,color_z]).T)
    # plot_dominant_color([color_x,color_y,color_z])

    '''the hsv color'''
    arr = mean_std_hsv(file_list[0])
    for img_file in file_list[1:]:
        c = mean_std_hsv(img_file)
        # c = count_color(img_file)
        arr = np.vstack((arr, c))
    # x = np.array(arr[:,0])
    # y = np.array(range(len(x)))
    # plt.scatter(x, y, alpha=0.6)
    # plt.show()

    for i in range(3):
        data = np.array(arr[:,i],dtype=int)
        print(data)
        plt.hist(data, bins=400, facecolor="blue", edgecolor="black", alpha=0.7)
        plt.ylabel('Frequency')

        if i==0:
            plt.xlabel('Hue')
            plt.title('Hue means hist')
            plt.savefig('./pics/Hue_means_hist'+'.png')
            plt.show()
        elif i==1:
            plt.xlabel('Saturation')
            plt.title('Saturation means hist')
            plt.savefig('./pics/Saturation_means_hist'+'.png')
            plt.show()
        elif i==2:
            plt.xlabel('Value')
            plt.title('Value means hist')
            plt.savefig('./pics/Value_means_hist'+'.png')
            plt.show()

    for i in range(3,6):
        data = np.array(arr[:,i],dtype=int)
        print(data)
        plt.hist(data, bins=400, facecolor="blue", edgecolor="black", alpha=0.7)
        plt.ylabel('Frequency')

        if i==3:
            plt.xlabel('Hue')
            plt.title('Hue std hist')
            plt.savefig('./pics/Hue_std_hist'+'.png')
            plt.show()
        elif i==4:
            plt.xlabel('Saturation')
            plt.title('Saturation std hist')
            plt.savefig('./pics/Saturation_std_hist'+'.png')
            plt.show()
        elif i==5:
            plt.xlabel('Value')
            plt.title('Value std hist')
            plt.savefig('./pics/Value_std_hist'+'.png')
            plt.show()

