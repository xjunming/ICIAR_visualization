import colorsys
from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def get_dominant_color(img_file):
    # 读取图片
    image = Image.open(img_file)
    # 颜色模式转换，以便输出rgb颜色值
    image = image.convert('RGBA')

    # 生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))

    max_score = 0 # 原来的代码此处为None
    dominant_color = 0 # 原来的代码此处为None，但运行出错，改为0以后运行成功，原因在于在下面的score > max_score的比较中，max_score的初始格式不定

    scores,rs,gs,bs = [],[],[],[]
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # print(count)
        # 纯黑
        if a == 0:
            continue

        if ((r > 210) & (g > 210) & (b > 210)):
            continue
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]


        # Calculate the score, preferring highly saturated colors.
        # Add 0.1 to the saturation so we don't completely ignore grayscale
        # colors by multiplying the count by zero, but still give them a low
        # weight.
        score = (saturation + 0.1) * count
        scores.append(score)
        rs.append(r)
        gs.append(g)
        bs.append(b)

        if score > max_score:
            # print(saturation, count)
            max_score = score
            dominant_color = (r, g, b)

    scores,rs,gs,bs = np.array(scores),np.array(rs),np.array(gs),np.array(bs)
    # scores = (scores-np.min(scores))/(np.max(scores)-np.min(scores))
    print(np.multiply(scores,rs))
    dominant_color = (np.mean(np.multiply(scores,rs)),np.mean(np.multiply(scores,gs)),np.mean(np.multiply(scores,bs)))
    return dominant_color

def plot_dominant_color(arr,elev=45,azim=45):
    x, y, z = arr[0], arr[1], arr[2]
    ax = plt.subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlim(0, 255)
    ax.set_ylim(0, 255)
    ax.set_zlim(0, 255)
    plt.show()

if __name__=='__main__':
    img_file = 'train/t/test.jpg'
    dominant_color = get_dominant_color(img_file)
    print(np.array(dominant_color))
    # plot_dominant_color(np.array(dominant_color))
    # 画图
    im = Image.new("RGB", (1, 1))
    im.putpixel((0, 0), (int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2])))
    im1 = Image.open(img_file)
    plt.imshow(im)
    plt.imshow(im1)
    plt.axis('off')
    plt.show()
