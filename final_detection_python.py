import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image

f = open("test3.txt","r")
height = 4032
width = 3024

content = f.readlines()
file_array = []
for row in content:
    file_array.append(row.split())
def convertFormat(file_array):
    height = 4032
    width = 3024
    dict_objects = {}
    for row in file_array:
        try:
#             float(row[1])
            l = int(row[1])
            print(l)
            t = int(row[2])
            r = int(row[3])

            b = int(row[4])

            bw = abs(r-l)
            bh = abs(t-b)
            print(bw)

            if(row[0] in dict_objects.keys()):
                dict_objects[row[0]].append([(l+bw/2.0),(t+bh/2.0),bw,bh])
            else:
                dict_objects[row[0]] = []
                dict_objects[row[0]].append([(l+bw/2.0),(t+bh/2.0),bw,bh])

        except:
            print("Invalid")
    return dict_objects

dic = convertFormat(file_array)


chair_array = np.array([[1,1],[1,1]])
person_array = np.ones(len(dic["person"]))*10000




for pers in dic["person"]:
    personalDist = 10000;
    lCount = 0
    tCount = 0
    for chair in dic["chair"]:
        a = np.array(pers[0:2])
        b = np.array(chair[0:2])
        dist = np.linalg.norm(a-b)
        if(dist<personalDist):
            personalDist = dist;
            closestChair = b;

    for chair in dic["chair"]:
        a = np.array(chair[0:2])
        if(closestChair[0] < a[0]):
            lCount+=1;
        if(closestChair[1] < a[1]):
            tCount+=1;
    if(lCount>=2):
        if(tCount>=2):
            chair_array[0][0] = 0;
        else:
            chair_array[1][0] = 0;
    else:
        if(tCount>=2):
            chair_array[0][1] = 0;
        else:
            chair_array[1][1] = 0;

def generateSaveImage(topleft,topright,bottomleft,bottomright):
    image = Image.new("RGB", (100, 200), "red")
    pixels = image.load()

    if (topleft==1):
        for i in range(50):
            for j in range(100):
                pixels[i,j] = (0,255,0)
    if (topright==1):
        for i in range(50):
            for j in range(100):
                pixels[50+i,j] = (0,255,0)
    if (bottomleft==1):
        for i in range(50):
            for j in range(100):
                pixels[i,j+100] = (0,255,0)
    if (bottomright==1):
        for i in range(50):
            for j in range(100):
                pixels[i+50,j+100] = (0,255,0)

    for i in range(100):
        pixels[i,99] = (255,255,255)
        pixels[i,100] = (255,255,255)
        pixels[i,101] = (255,255,255)

    for i in range(200):
        pixels[51,i] = (255,255,255)
        pixels[50,i] = (255,255,255)
        pixels[49,i] = (255,255,255)
    plt.imshow(image)
    image.save('genimage.jpg','JPEG')


generateSaveImage(chair_array[0,0],chair_array[0,1],chair_array[1,0],chair_array[1,1])
