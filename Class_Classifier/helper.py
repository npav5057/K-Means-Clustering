from random import choice
from math import hypot


def mean(Class):
    mn =[0,0]
    for data in Class:
        for j in range(2):
            mn[j] = mn[j]+data[j]
    for j in range(2):
        mn[j] = mn[j]/len(Class)
    return mn

def get_random_colour(number_of_colors):
    color = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)]
    return color




def get_Cluster(point,mean,k):
    min_dist=9999999.9
    index= -1
    for i in range(k):
        dist=hypot(point[0]-mean[i][0],point[1]-mean[i][1])
        if min_dist>dist:
            index=i
            min_dist = dist
    #print(index)
    return index,min_dist


def set_random_mean(data,K):
    means = []
    for i in range(K):
        means.append(choice(data))
    return means



def get_datapoints(file):
    f=open(file,"r")
    X=[]
    for line in f:
        a,b=line.split()
        X.append([float(a),float(b)])
    f.close()
    return X

def get_data(file):
    f=open(file,"r")
    X=[]
    flag = True
    for line in f:
        if flag is True:
            flag =False
        else:
            a,b=line.split()
            X.append([float(a),float(b)])
    f.close()
    return X
