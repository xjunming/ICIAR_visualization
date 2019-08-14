import cv2
import numpy as np

def count_red(filename):
    img = cv2.imread(filename)
    # set red thresh
    lower_red=np.array([156,43,46])
    upper_red=np.array([180,255,255])
    lower_red1 = np.array([0,43,46])
    upper_red1 = np.array([10,255,255])
    frame = img
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red) + cv2.inRange(hsv,lower_red1,upper_red1)
    
    # print(mask.shape[0]*mask.shape[1])
    return 2*np.sum(mask)

def count_grey(filename):
    img = cv2.imread(filename)
    # set grey thresh
    lower_grey=np.array([0,0,46])
    upper_grey=np.array([180,43,220])
    frame = img
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_grey, upper_grey)
    # print(mask.shape[0]*mask.shape[1])
    return np.sum(mask)

def count_purple(filename):
    img = cv2.imread(filename)
    # set purple thresh
    lower_purple=np.array([125,43,46])
    upper_purple=np.array([155,255,255])
    frame = img
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    # print(mask.shape[0]*mask.shape[1])
    return 2*np.sum(mask)

def count_blue(filename):
    img = cv2.imread(filename)
    lower_blue=np.array([78,43,46])
    upper_blue=np.array([124,255,255])
    frame = img
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # print(mask.shape[0]*mask.shape[1])
    return 2*np.sum(mask)


def count_color(filename):
    return np.array(
        [count_red(filename),
        count_grey(filename),
        count_purple(filename),
         count_blue(filename)]
    )


if __name__=='__main__':
    files = ['E://biototem//main_color\\train\\s//b096.tif', 'E://biototem//main_color\\train\\s//b099.tif', 'E://biototem//main_color\\train\\t//b066.tif', 'E://biototem//main_color\\train\\t//b095.tif']
    arr = count_color(files[0])
    for img_file in files[1:]:
        c = count_color(img_file)
        arr = np.vstack((arr,c))


    print(arr)
    print(c)



