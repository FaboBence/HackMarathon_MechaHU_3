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
   ret, thresh16 = cv2.threshold(img_blur,int(max_brightnes/8),10,cv2.THRESH_BINARY)
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

def curve_detection(img):
    ret, labels = cv2.connectedComponents(img) # Searching for connected curves
    curves = []
    ellipses = []
    best_fit = None
    min_R = 10001
    max_len = 0
    for i in range(1,ret+1):
        tmp = np.where(labels == i, 1, 0)
        sum_tmp = np.sum(tmp)
        if sum_tmp > 30:
            curves.append(tmp)
            if sum_tmp > max_len:
                best_fit = curves[-1]
                max_len = sum_tmp
    try:

        xc,yc,a,b,theta,R_square = fit_ellipse(best_fit)
        best_fit = [xc,yc,a,b,theta,R_square]
    except:
        best_fit = None
    # Fitting an ellipse on every curve
    #for curve in curves:
    #    try:
    #        xc,yc,a,b,theta,R_square = fit_ellipse(curve)
    #        ellipses.append([xc,yc,a,b,theta,R_square])
    #        if R_square < min_R:
    #            best_fit = ellipses[-1]
    #            min_R = R_square
    #    except:
    #        pass
    if best_fit:
        return best_fit[:]
    return best_fit
    
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
      R_square = np.average(np.square(ell.residuals(edge_poins)))
      #print(R_square)
      if R_square > 10000:
          return None # No ellipse found
      return xc, yc, a, b, theta, R_square
   except:
      return None 

if __name__ == "__main__":
   pre_process(cv2.imread("../marathon-thermofisher-challenge-master/data/train/1 Easy Fits/2018-02-15 17.27.27.162000.tiff",-1))
