import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import EllipseModel
from matplotlib.patches import Ellipse
#import scipy.signal as signal
def pre_process(img):
   # Image processing
   #img = cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.tiff",-1)
   #img = cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.png",2)
   #print(type(img_tiff[0][0]),"\n",type(img[0][0]))
   #*plt.imshow(img, cmap="gray", vmin=1000, vmax=1001)
   #*plt.show()
   max_brightnes = np.max(img)
   ret, thresh16 = cv2.threshold(img,int(max_brightnes/4),10,cv2.THRESH_BINARY)
      # Edge detection
   #kernel = np.array([[-1,-1,-1],[-1,8,-1], [-1,-1,-1]])
   thresh8 = thresh16.astype('uint8')
   edges = cv2.Canny(thresh8,9,11)
   #plt.imshow(edges, cmap="gray", vmin=0, vmax=256)
   #plt.show()
   return edges

def inner_noise_filtering():
    pass

   # Ellipse fitting
def fit_ellipse(edges):
   edges_coord = np.where(edges > 0)
   try :
      x, y = edges_coord[0], edges_coord[1]
      edge_poins = (y,x)
      edge_poins=np.array(edge_poins)
      edge_poins=np.transpose(edge_poins)
      ell = EllipseModel()
      ell.estimate(edge_poins)
      xc, yc, a, b, theta = ell.params
      #print(xc,yc)
      print(np.average(np.square(ell.residuals(edge_poins))))
      return xc, yc, a, b, theta
   except:
      return None 

if __name__ == "__main__":
   pre_process(cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.tiff",-1))
