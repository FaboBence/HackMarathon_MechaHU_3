import os
import cv2
import matplotlib.pyplot as plt

def load_images(path = "../marathon-thermofisher-challenge-master/data/train/1 Easy Fits"):
    pngs=[]
    tiffs = []
    for filename in os.listdir(path):
        file_n = os.fsdecode(filename)
        if file_n.endswith(".png"): 
            pngs.append(cv2.imread(os.path.join(path,filename),-1))
        elif file_n.endswith(".tiff"):
            tiffs.append(cv2.imread(os.path.join(path,filename),-1))
        else:
            print("???")
    return tiffs, pngs

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
