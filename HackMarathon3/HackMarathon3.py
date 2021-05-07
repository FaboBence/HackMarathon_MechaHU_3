import cv2, time
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from EasyFits import *
from image_loader import *

if __name__ == "__main__":
    tiffs, pngs, names = load_images()
    done = []
    filtered = []
    results = []
    for i,tiff in enumerate(tiffs):
        start = time.time() # Measuring elapsed time
        # Edge detection
        done.append(pre_process(tiff))
        try:
            # First ellipse fit on raw edge detection data
            xc, yc, a, b, theta, R_square = fit_ellipse(done[-1])
            cv2.ellipse(pngs[i],(int(xc),int(yc)),(int(a),int(b)),int(theta),0,360,(255,0,0),3)
            print(R_square)

            # Noise filtering
            filtered_img = inner_noise_filtering(deepcopy(done[-1]),xc,yc,a,b,theta)
            filtered.append(filtered_img)
            xc, yc, a, b, theta, R_square = fit_ellipse(filtered_img)
            print(R_square)

            # Curve detection
            #xc, yc, a, b, theta, R_square = curve_detection(filtered_img)

            cv2.ellipse(pngs[i],(int(xc),int(yc)),(int(a),int(b)),int(theta),0,360,(0,255,0),3)
            end = time.time() # Measuring elapsed time
            results.append([names[i],xc,yc,a,b,theta,(end-start)*1000]) # Saving results
        except:
            end = time.time() # Measuring elapsed time
            results.append([names[i],'','','','','',(end-start)*1000]) # If we didn't find an ellipse results
            print("No ellipse found")
    create_csv("Results.csv", results)
    score = calculator("../marathon-thermofisher-challenge-master/data/ground_truths_train.csv","Results.csv")
    print("Score:",score)
    show_images(done,filtered, pngs)
    
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