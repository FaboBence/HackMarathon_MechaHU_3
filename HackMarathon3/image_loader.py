import os
import cv2
import csv
import matplotlib.pyplot as plt

pre_filename = "../marathon-thermofisher-challenge-master/data/train/"
files = ["1 Easy Fits","2 Hardly Fittable","3 Grid Cut-offs","4 Illumination States 1","5 Illumination States 2",
         "6 Coma & Caustic","7 Generally Hard"]

def load_images(path = pre_filename+files[1-1]):
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
        for line in results:
            for i,data in enumerate(line):
                if type(data) != 'string':
                    data = round(data,2)
                if i < 6:
                    s.write(str(data)+',')
                else:
                    s.write(str(data)+'\n')

def show_images(tiffs, pngs=None):
    #print(len(tiffs))
    for i in range(len(tiffs)):
        f = plt.figure()
        f.add_subplot(1,2,1)
        plt.imshow(tiffs[i], cmap="gray", vmin=0, vmax=256)
        if pngs is not None:
            f.add_subplot(1,2,2)
            plt.imshow(pngs[i], cmap="gray", vmin=0, vmax=256)
        plt.show()

if __name__=="__main__":
    ti,pn = load_images()
    show_images(ti,pn)
