import cv2
import numpy as np


def count_red(filename):
    img = cv2.imread(filename)
    # set red thresh
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    lower_red1 = np.array([0, 43, 46])
    upper_red1 = np.array([10, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red) + cv2.inRange(hsv, lower_red1, upper_red1)
    # print(mask.shape[0]*mask.shape[1])
    return 2 * np.sum(mask)

def count_purple(filename):
    img = cv2.imread(filename)
    # set purple thresh
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    # print(mask.shape[0]*mask.shape[1])
    return 2 * np.sum(mask)

def count_blue(filename):
    img = cv2.imread(filename)
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([124, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # print(mask.shape[0]*mask.shape[1])
    return 2 * np.sum(mask)

def count_grey(filename):
    img = cv2.imread(filename)
    # set grey thresh
    lower_grey = np.array([0, 0, 46])
    upper_grey = np.array([180, 43, 220])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_grey, upper_grey)
    # print(mask.shape[0]*mask.shape[1])
    return np.sum(mask)

def count_black(filename):
    img = cv2.imread(filename)
    # set grey thresh
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_black, upper_black)
    # print(mask.shape[0]*mask.shape[1])
    return np.sum(mask)

def count_white(filename):
    img = cv2.imread(filename)
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    return np.sum(mask)*0.6

def count_color(filename):
    return np.array(
        [count_red(filename),
         count_grey(filename),
         count_purple(filename),
         count_blue(filename),
         count_black(filename),
         count_white(filename)]
    )

def mean_std_hsv(filename):
    img = cv2.imread(filename)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # print(np.mean(hsv[:,:,0]))
    return np.array([
        np.mean(hsv[:,:,0]),np.mean(hsv[:,:,1]),np.mean(hsv[:,:,2]),
        np.std(hsv[:, :, 0]), np.std(hsv[:, :, 1]), np.std(hsv[:, :, 2]),
    ])


if __name__ == '__main__':
    files = ["E://biototem//data//Benign//b096.tif", "E://biototem//data//InSitu/b095.tif",
             "E://biototem//data//Invasive//b066.tif", "E://biototem//data//Normal//b066.tif"]
    arr = mean_std_hsv(files[0])
    for img_file in files[1:]:
        c = mean_std_hsv(img_file)
        # c = count_color(img_file)
        arr = np.vstack((arr, c))

    print(arr[:,0])
    print(arr.shape)
    # print(c)



