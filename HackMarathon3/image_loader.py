import os
import cv2
import csv
import matplotlib.pyplot as plt

pre_filename = "../marathon-thermofisher-challenge-master/data/train/"
files = ["1 Easy Fits","2 Hardly Fittable","3 Grid Cut-offs","4 Illumination States 1","5 Illumination States 2",
         "6 Coma & Caustic","7 Generally Hard"]

def load_images(path = pre_filename+files[2-1]):
    pngs=[]
    tiffs = []
    names = []
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
