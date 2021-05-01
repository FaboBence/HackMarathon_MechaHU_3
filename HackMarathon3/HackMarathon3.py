import cv2
import numpy as np
import matplotlib.pyplot as plt
from EasyFits import pre_process, fit_ellipse
from image_loader import *

if __name__ == "__main__":
    tiffs , pngs = load_images()
    done = []
    for i in tiffs:
        done.append(pre_process(i))
        print(fit_ellipse(done[-1]))
    show_images(done,pngs)
    #plt.imshow(tiffs[0], cmap="gray", vmin=0, vmax=256)
    #plt.show()
"""
img = cv2.imread("../marathon-thermofisher-challenge-master/data/train/3 Grid Cut-offs/2018-02-15 18.53.26.982000.tiff",-1)

img_blur = cv2.GaussianBlur(img,(39,39),0,borderType = cv2.BORDER_DEFAULT)
plt.imshow(img_blur, cmap="gray", vmin=0, vmax=50)
plt.show()

ret,thresh1 = cv2.threshold(img_blur,38,55,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap="gray", vmin=0, vmax=55)
plt.show()
#print(np.quantile(img,0.99))
#cv2.imshow("Image",img)
#cv2.waitKey(10000)
"""