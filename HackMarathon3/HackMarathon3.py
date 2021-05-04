import cv2, time
import numpy as np
import matplotlib.pyplot as plt
from EasyFits import pre_process, fit_ellipse
from image_loader import *

if __name__ == "__main__":
    tiffs, pngs, names = load_images()
    done = []
    results = []
    for i,tiff in enumerate(tiffs):
        start = time.time() # Measuring elapsed time
        done.append(pre_process(tiff))
        try:
            xc, yc, a, b, theta = fit_ellipse(done[-1])
            end = time.time() # Measuring elapsed time
            results.append([names[i],xc,yc,a,b,theta,end-start]) # Saving results
            pngs[i] = cv2.ellipse(pngs[i],(int(xc),int(yc)),(int(a),int(b)),int(theta*180/3.14),0,360,(0,255,0),3)
            plt.imshow(pngs[i], vmin=0, vmax=256)
            #print("ez is lefutott")
        except:
            print("No ellipse found")
    create_csv("Results.csv", results)
    show_images(done,pngs)
    
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