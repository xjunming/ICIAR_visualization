import os
from PIL import Image
from dominant_color import get_dominant_color,plot_dominant_color
import numpy as np
from sklearn.cluster import KMeans
from count_color import count_color


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

    ''' dominant_color '''
    # color_x, color_y, color_z = [],[],[]
    # for img_file in file_list:
    #     image = Image.open(img_file)
    #     dominant_color = get_dominant_color(img_file)
    #     color_x.append(dominant_color[0])
    #     color_y.append(dominant_color[1])
    #     color_z.append(dominant_color[2])
    # # plot_dominant_color([color_x,color_y,color_z])
    # print(dominant_color)
    # main_color_array = np.c_[
    #     np.array(color_x).reshape(len(color_x),1),
    #     np.array(color_y).reshape(len(color_y),1),
    #     np.array(color_z).reshape(len(color_z),1)
    # ]
    # # print(main_color_array)
    # print(main_color_array)

    ''' count_color '''
    print(file_list[0])
    main_color_array = count_color(file_list[0])
    for img_file in file_list[1:]:
        c = count_color(img_file)
        main_color_array = np.vstack((main_color_array,c))

    n_clusters = 4
    estimator = KMeans(n_clusters=n_clusters)
    estimator.fit(main_color_array)
    label_pred = estimator.labels_ #获取聚类标签
    centroids = estimator.cluster_centers_ #获取聚类中心
    inertia = estimator.inertia_ # 获取聚类准则的总和

    path = './classify'
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)
    class_name = ['./classify/class_' + str(i) for i in range(0, n_clusters)]
    # print(label_pred[label_pred==0])
    for i in range(max(label_pred) + 1):
        with open(class_name[i], 'w') as f:
            for item in [file_list[index] for index, val in enumerate(label_pred) if val == i]:
                f.write("%s\n" % item)