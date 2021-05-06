import os
import cv2
import numpy as np
import csv
import matplotlib.pyplot as plt

pre_filename = "../marathon-thermofisher-challenge-master/data/train/"
files = ["1 Easy Fits","2 Hardly Fittable","3 Grid Cut-offs","4 Illumination States 1","5 Illumination States 2",
         "6 Coma & Caustic","7 Generally Hard"]

def load_images(path = pre_filename+files[4-1]):
    pngs=[]
    tiffs = []
    names = []
    for file in files:
        path = pre_filename + file
        for filename in os.listdir(path):
            file_n = os.fsdecode(filename)
            if file_n.endswith(".png"): 
                pngs.append(cv2.imread(os.path.join(path,filename),-1))
            elif file_n.endswith(".tiff"):
                names.append(file_n)
                tiffs.append(cv2.imread(os.path.join(path,filename),-1))
            else:
                print("???")
    return tiffs, pngs, names

def create_csv(filename,results):
    with open(filename,'w',encoding='utf-8') as s:
        # Header
        s.write("filename,ellipse_center_x,ellipse_center_y,ellipse_majoraxis,ellipse_minoraxis,ellipse_angle,elapsed_time\n")
        # Data lines
        for line in results:
            for i,data in enumerate(line):
                try:
                    data = round(data,2)
                except:
                    pass
                if i < 6:
                    s.write(str(data)+',')
                else:
                    s.write(str(data)+'\n')

def calculator(ground_thruth_csv, results_csv):
    score = 0
    truths = []
    results = []
    with open(ground_thruth_csv,'r') as s:
        csv_reader = csv.reader(s, delimiter=',', quotechar='|')
        for i,row in enumerate(csv_reader):
            if i == 0:
                continue
            truths.append(row)
    with open(results_csv,'r') as s:
        csv_reader = csv.reader(s, delimiter=',', quotechar='|')
        for i,row in enumerate(csv_reader):
            if i == 0:
                continue
            results.append(row)
    # Point calculation
    for result in results:
        for truth in truths:
            if truth[0] == result[0]: # If file names match
                if truth[1]: # If ground truth image is not empty
                    if result[1]: # If resulting image is not empty
                        ground_img = np.zeros((int(truth[7]),int(truth[6])))
                        result_img = np.zeros((int(truth[7]),int(truth[6])))
                        cv2.ellipse(ground_img,(int(float(truth[1])),int(float(truth[2]))),(int(float(truth[3])),int(float(truth[4]))),int(float(truth[5])),0,360,1,-1)
                        cv2.ellipse(result_img,(int(float(result[1])),int(float(result[2]))),(int(float(result[3])),int(float(result[4]))),int(float(result[5])),0,360,1,-1)
                        # Area
                        ground_area = np.sum(ground_img)
                        result_area = np.sum(result_img)
                        # Overlap
                        overlap = ground_img + result_img
                        overlap_img = np.where(overlap > 1, 1, 0)
                        # Score
                        score += np.sum(overlap_img) / max(ground_area,result_area)
                    else:
                        score += 0
                else: # If ground truth image is empty
                    if result[1]: # If resulting image is not empty
                        score += 0
                    else:
                        score += 1
                break
    return score


def show_images(tiffs, filtered, pngs=None):
    #print(len(tiffs))
    for i in range(len(tiffs)):
        f = plt.figure()
        f.add_subplot(2,2,1)
        plt.imshow(tiffs[i], cmap="gray", vmin=0, vmax=256)
        if pngs is not None:
            f.add_subplot(2,2,2)
            plt.imshow(pngs[i], cmap="gray", vmin=0, vmax=256)
        f.add_subplot(2,2,3)
        plt.imshow(filtered[i], cmap="gray",vmin=0,vmax=256)
        plt.show()

if __name__=="__main__":
    ti,pn = load_images()
    show_images(ti,pn)
