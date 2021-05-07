import cv2, time
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from image_processing import *
from file_manipulation import *

def images(tiffs, filtered, pngs):
    for i in range(len(tiffs)):
        f = plt.figure()
        f.add_subplot(2,2,1)
        plt.imshow(tiffs[i], cmap="gray", vmin=0, vmax=256)
        f.add_subplot(2,2,2)
        plt.imshow(pngs[i], cmap="gray", vmin=0, vmax=600)
        f.add_subplot(2,2,3)
        plt.imshow(filtered[i], cmap="gray",vmin=0,vmax=256)
        plt.show()

if __name__ == "__main__":
    tiffs, pngs, names = load_images()
    pngs = []
    pngs = deepcopy(tiffs)
    done = []
    filtered = []
    results = []
    for i,tiff in enumerate(tiffs):
        pngs.append(cv2.cvtColor(deepcopy(tiff),cv2.COLOR_GRAY2RGB))
        start = time.time() # Measuring elapsed time
        # Edge detection
        done.append(pre_process(tiff))
        try:
            # First ellipse fit on raw edge detection data
            xc, yc, a, b, theta, R_square = fit_ellipse(done[-1])
            cv2.ellipse(pngs[i],(int(xc),int(yc)),(int(a),int(b)),int(theta),0,360,(255,0,0),3)
            #print(R_square)

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
    images(done,filtered, pngs)
