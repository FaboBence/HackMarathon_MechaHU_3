import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import EllipseModel
from matplotlib.patches import Ellipse

def pre_process(img):
   # Image processing
   max_brightnes = np.max(img)
   # Blur
   img_blur = cv2.GaussianBlur(img,(25,25),0,borderType = cv2.BORDER_DEFAULT)
   # Thresholding
   ret, thresh16 = cv2.threshold(img_blur,int(max_brightnes/4),10,cv2.THRESH_BINARY)
      # Edge detection
   #kernel = np.array([[-1,-1,-1],[-1,8,-1], [-1,-1,-1]])
   thresh8 = thresh16.astype('uint8')
   edges = cv2.Canny(thresh8,9,11)
   #plt.imshow(edges, cmap="gray", vmin=0, vmax=256)
   #plt.show()
   return edges

def inner_noise_filtering(edge_img,xc,yc,a,b,theta):
    out_img = cv2.ellipse(edge_img,(int(xc),int(yc)),(int(a),int(b)),int(theta),0,360,(0,0,0),-1)
    return out_img

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
      theta = theta*180/3.14
      print(np.average(np.square(ell.residuals(edge_poins))))
      return xc, yc, a, b, theta
   except:
      return None 

if __name__ == "__main__":
   pre_process(cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.tiff",-1))
