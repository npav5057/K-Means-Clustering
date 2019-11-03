import helper as fun
import sys
from matplotlib import pyplot as plt

error =0.05

if __name__ == '__main__':

    k=int(sys.argv[2])
    if(sys.argv[1]=='LS'):
        data = fun.get_datapoints("Data1/Class1.txt")
        data = data + fun.get_datapoints("Data1/Class3.txt")
        data = data + fun.get_datapoints("Data1/Class2.txt")
    elif(sys.argv[1]=='NLS'):
        data = fun.get_data("Data2/mixed_data.txt")

    # print(len(data))
    # K points are chosen randomly from data as mean
    mean = fun.set_random_mean(data,k)

    itr = 0
    final_distortion=999999.9
    init_distortion=0.0
    while(abs(final_distortion-init_distortion)>error):
        cluster = [[] for i in range(k)]
        itr=itr+1
        init_distortion=final_distortion
        final_distortion=0
        for point in data:
            assigned_cluster , min_distortion = fun.get_Cluster(point,mean,k)
            cluster[assigned_cluster].append(point)
            final_distortion = final_distortion + min_distortion
        for i in range(k):
            mean[i]=fun.mean(cluster[i])
        print("Iteration:",itr,"     Distortion measure Error:",abs(final_distortion-init_distortion))


    colour=fun.get_random_colour(k)
    for t in range(k):
        for data in cluster[t]:
            plt.plot(data[0],data[1],color=colour[t],marker='o', markersize=1)

    plt.savefig(sys.argv[1]+"_cluster_"+str(k)+".png")
