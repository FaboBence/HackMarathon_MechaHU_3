import cv2
import numpy as np
import matplotlib.pyplot as plt
#import scipy.signal as signal
def pre_process(img):
   # Image processing
   #img = cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.tiff",-1)
   #img = cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.png",2)
   #print(type(img_tiff[0][0]),"\n",type(img[0][0]))
   #*plt.imshow(img, cmap="gray", vmin=1000, vmax=1001)
   #*plt.show()
   ret, thresh16 = cv2.threshold(img,1000,10,cv2.THRESH_BINARY)
      # Edge detection
   #kernel = np.array([[-1,-1,-1],[-1,8,-1], [-1,-1,-1]])
   thresh8 = thresh16.astype('uint8')
   edges = cv2.Canny(thresh8,9,11)
   plt.imshow(edges, cmap="gray", vmin=0, vmax=256)
   plt.show()
   return edges
   # Ellipse fitting
if __name__ == "__main__":
   pre_process(cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.tiff",-1))
