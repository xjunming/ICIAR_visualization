import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

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
    return np.sum(mask)

def count_purple(filename):
    img = cv2.imread(filename)
    # set purple thresh
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    # print(mask.shape[0]*mask.shape[1])
    return np.sum(mask)

def count_blue(filename):
    img = cv2.imread(filename)
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([124, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # print(mask.shape[0]*mask.shape[1])
    return np.sum(mask)

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
    return np.sum(mask)

def count_color(filename):
    return np.array(
        [count_red(filename),
         count_grey(filename),
         count_purple(filename),
         count_blue(filename),
         count_black(filename),
         count_white(filename)]
    )

def zoom_aug(img, zoom_var, seed=None):
    """Performs a random spatial zoom of a Numpy image array.

    # Arguments
        img: Numpy image array.
        zoom_var: zoom range multiplier for width and height.
        seed: Random seed.
    # Returns
        Zoomed Numpy image array.
    """
    scale = np.random.RandomState(seed).uniform(low=1 / zoom_var, high=zoom_var)
    print(scale)
    resized_img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    print(img.shape,resized_img.shape)
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.subplot(1,2,2)
    plt.imshow(resized_img)
    plt.show()
    return resized_img

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def calculate_means_std(img):
    
    h,s,v = [],[],[]
    for raw in range(img.shape[0]):
        for col in range(img.shape[1]):
            r,g,b = hsv2rgb(img[raw,col,0], img[raw,col,1], img[raw,col,2])
            if r > 200 and g > 200 and b > 200:  # white
                continue
                # pass
            elif  r > 210 and r < 230\
                    and g > 75 and g <95\
                    and b > 200 and b < 220:
                print('too red')
                continue
                # pass
            else:
                h.append(img[raw,col,0])
                s.append(img[raw,col,1])
                v.append(img[raw,col,2])
    h_means = np.mean(np.array(h))
    h_std = np.std(np.array(h))
    s_means = np.mean(np.array(s))
    s_std = np.std(np.array(s))
    v_means = np.mean(np.array(v))
    v_std = np.std(np.array(v))
    dominant_color = np.array([h_means, s_means, v_means])
    print('calculate_means_std', np.array(dominant_color))
    im = Image.new("RGB", (1, 1))
    im.putpixel((0, 0), (int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2])))
    plt.imshow(im)
    plt.show()
    return np.array([h_means, s_means, v_means,
                     h_std, s_std, v_std])

def mean_std_hsv(filename,zoom_in_size = 4):
    img = cv2.imread(filename)
    img = cv2.resize(img, None, fx=1/zoom_in_size, fy=1/zoom_in_size, interpolation=cv2.INTER_CUBIC)
    # vec = calculate_means_std(img)
    # print(vec)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # print(np.mean(hsv[:,:,0]))
    return calculate_means_std(hsv)


if __name__ == '__main__':
    files = ["E://biototem//data//Benign//b096.tif", "E://biototem//data//InSitu/b095.tif",
             "E://biototem//data//Invasive//b066.tif", "E://biototem//data//Normal//b066.tif"]
    arr = mean_std_hsv(files[0])
    for img_file in files[1:]:
        c = mean_std_hsv(img_file)
        # c = count_color(img_file)
        arr = np.vstack((arr, c))

    print(arr.shape)
    dominant_color = arr[3,0:3]
    print('dominant_color', np.array(dominant_color))
    # plot_dominant_color(np.array(dominant_color))
    im = Image.new("RGB", (1, 1))
    im.putpixel((0, 0), (int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2])))
    plt.imshow(im)
    plt.show()


