from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from tqdm import tqdm

def count_f(filename):
    pics_list = []
    with open(filename,encoding='utf-8') as f:
        line = f.readline().rstrip('\n').split('//')[-1]
        pics_list.append(line)
        while line:
            line = f.readline().rstrip('\n').split('//')[-1]
            pics_list.append(line)
    return pics_list

if __name__=='__main__':
    labels = []
    df = pd.read_csv("E://biototem//开会//工作日志//image//20190826//pics03//ICIAR2018_BACH_dataset_micro_patient.csv")
    pics_list = {}
    filename = [# "E://biototem//开会//工作日志//image//20190826//pics04//class_0",
                "E://biototem//开会//工作日志//image//20190826//pics06//class_1",
                "E://biototem//开会//工作日志//image//20190826//pics06//class_2",
                "E://biototem//开会//工作日志//image//20190826//pics06//class_3",]
    for i in range(len(filename)):
        pics_list[i] = count_f(filename[i])
    for n in df.Histology:
        if n in pics_list[0]:
            labels.append(1)
        elif n in pics_list[1]:
            labels.append(2)
        elif n in pics_list[2]:
            labels.append(3)
        else:
            labels.append(0)
    df['labels'] = labels
    df.sort_values('Patient',inplace=True)

    df_file_list = pd.read_csv("E://biototem//ICIAR_visualization//file_list_edit.csv",index_col=0)
    # print(df_file_list.head(5))
    file_list = []
    print(df_file_list['pics_list'][df_file_list['pics_list']=='is047.tif'].index[0])
    main_color_array = np.load("E://biototem//开会//工作日志//image//20190826//pics06//main_color_array.npy")
    vec = []
    for n in df.Histology:
        i = df_file_list['pics_list'][df_file_list['pics_list']==str(n)].index[0]
        file_list.append(df_file_list.file_list[i])
        vec.append(list(main_color_array[i]))
    df['file_list'] = file_list
    df['vec'] = vec
    # df.to_csv('results.csv')

    print(set(df['Patient']))

    i = 0
    for p in list(set(df['Patient'])):
        path = './output/Patient_%s/' % str(p)
        folder = os.path.exists(path)
        if not folder: os.makedirs(path)
        for v in tqdm(df['vec'][df['Patient']==p]):
            # print(v[0:3])
            dominant_color = v[0:3]
            im = Image.new("RGB", (1, 1))
            im.putpixel((0, 0), (int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2])))
            plt.imshow(im)
            plt.savefig((path + str(df.Histology[i])).replace('tif','png'))
            # plt.show()
            i = i +1
