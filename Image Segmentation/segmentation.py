import cv2 as cv
import numpy as np
from random import randrange
from math import sqrt
from PIL import Image

error = 500
k=5
def set_mean(data,k):
    means=[]
    for i in range(k):
        x=randrange(0,row,5)
        y=randrange(0,col,5)
        means.append([int(data[x][y][0]),int(data[x][y][1]),int(data[x][y][2])])
    return means

def set_cluster_to_point(point,mean):
    index=-0.5
    min_d= 9999.9
    for i in range(k):
        dist = sqrt((int(point[0])-mean[i][0])**2 +(int(point[1])-mean[i][1])**2+(int(point[2])-mean[i][2])**2 )
        if(dist<min_d):
            min_d=dist
            index=i
    return min_d,index


if __name__ == '__main__':

    image= cv.imread('hill.jpg')
    [row,col,d]=image.shape
    print(row,col)
    #image resizing as factor of 0.5
    factor=0.5
    row=int(row*factor)
    col=int(col*factor)
    # print(row,col)
    image = cv.resize(image,(col,row))
    [row,col,d]=image.shape
    print(row,col)


    mean = set_mean(image,k)
    cluster = np.zeros((row,col), dtype=np.uint8)

    final=999999.9
    init=0.0
    itr=0
    while(abs(final-init)>error):
        itr=itr+1
        final=init
        init=0.0
        for i in range(row):
            for j in range(col):
                min_dist,cluster[i][j]= set_cluster_to_point(image[i][j],mean)
                init+=min_dist
        print("Itr:",itr," Error:",abs(final-init))
        mean = []
        cluster_size = []
        for i in range(k):
            mean.append([0,0,0])
            cluster_size.append(0)
        for i in range(row):
            for j in range(col):
                cluster_size[cluster[i][j]]+= 1
                mean[cluster[i][j]][0]+= int(image[i][j][0])
                mean[cluster[i][j]][1]+= int(image[i][j][1])
                mean[cluster[i][j]][2]+= int(image[i][j][2])

        for i in range(k):
            if(cluster_size[i]>0):
                mean[i][0]/=cluster_size[i]
                mean[i][1]/=cluster_size[i]
                mean[i][2]/=cluster_size[i]

    # End of Loop, Cluster identified
    data = np.zeros((row,col,3), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            data[i][j]=mean[cluster[i][j]]

    new_img = Image.fromarray(data, 'RGB')
    new_img.save('temp.jpg')
    img = cv.imread('temp.jpg')
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    cv.imwrite('output_'+str(k)+'.png', img)
